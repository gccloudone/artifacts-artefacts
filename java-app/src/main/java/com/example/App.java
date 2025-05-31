package com.example;

import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpExchange;
import java.io.*;
import java.net.InetSocketAddress;
import java.time.Instant;
import java.util.concurrent.Executors;

public class App {
    private static final int PORT = 8080;
    
    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(PORT), 0);
        
        // Health check endpoint
        server.createContext("/", exchange -> {
            String response = String.format("""
                {
                  "status": "healthy",
                  "service": "java-demo-api",
                  "timestamp": "%s",
                  "version": "1.0.0",
                  "message": "Comparing Chainguard vs Traditional Docker images"
                }
                """, Instant.now().toString());
            
            sendJsonResponse(exchange, response);
        });
        
        // Info endpoint
        server.createContext("/api/info", exchange -> {
            String response = String.format("""
                {
                  "service": "GC Secure Artifacts Java Demo",
                  "description": "Demonstrating Chainguard vs Traditional Docker images",
                  "features": [
                    "Pure Java HTTP server",
                    "Multi-stage build comparison",
                    "Security posture demonstration",
                    "Image size comparison",
                    "SBOM generation ready"
                  ],
                  "javaVersion": "%s",
                  "containerInfo": {
                    "user": "%s",
                    "workdir": "%s"
                  }
                }
                """, 
                System.getProperty("java.version"),
                System.getProperty("user.name"),
                System.getProperty("user.dir"));
            
            sendJsonResponse(exchange, response);
        });
        
        // Echo endpoint for testing
        server.createContext("/api/echo", exchange -> {
            if ("POST".equals(exchange.getRequestMethod())) {
                String body = new String(exchange.getRequestBody().readAllBytes());
                String response = String.format("""
                    {
                      "received": "%s",
                      "timestamp": "%s",
                      "length": %d
                    }
                    """, escapeJson(body), Instant.now().toString(), body.length());
                
                sendJsonResponse(exchange, response);
            } else {
                exchange.sendResponseHeaders(405, 0);
                exchange.close();
            }
        });
        
        server.setExecutor(Executors.newFixedThreadPool(4));
        server.start();
        
        System.out.println("Java Demo API started on port " + PORT);
        System.out.println("Available endpoints:");
        System.out.println("   GET  /          - Health check");
        System.out.println("   GET  /api/info  - Service information"); 
        System.out.println("   POST /api/echo  - Echo service");
        System.out.println("Compare image sizes with: docker images | grep demo");
    }
    
    private static void sendJsonResponse(HttpExchange exchange, String response) throws IOException {
        exchange.getResponseHeaders().set("Content-Type", "application/json");
        exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
        exchange.sendResponseHeaders(200, response.getBytes().length);
        try (OutputStream os = exchange.getResponseBody()) {
            os.write(response.getBytes());
        }
    }
    
    private static String escapeJson(String input) {
        return input.replace("\"", "\\\"").replace("\n", "\\n").replace("\r", "\\r");
    }
}