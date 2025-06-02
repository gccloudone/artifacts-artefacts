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

        server.createContext("/", exchange -> {
            String response = """
                {
                  "status": "healthy",
                  "service": "java-demo-api",
                  "timestamp": "%s",
                  "version": "1.0.0"
                }
                """.formatted(Instant.now().toString());

            sendResponse(exchange, response, 200);
        });

        server.createContext("/api/info", exchange -> {
            String response = """
                {
                  "service": "Java Demo",
                  "javaVersion": "%s",
                  "user": "%s",
                  "workdir": "%s"
                }
                """.formatted(
                    escapeJson(System.getProperty("java.version")),
                    escapeJson(System.getProperty("user.name")),
                    escapeJson(System.getProperty("user.dir")));

            sendResponse(exchange, response, 200);
        });

        server.createContext("/api/echo", exchange -> {
            try {
                if ("POST".equals(exchange.getRequestMethod())) {
                    String body = new String(exchange.getRequestBody().readAllBytes());
                    String response = """
                        {
                          "received": "%s",
                          "timestamp": "%s",
                          "length": %d
                        }
                        """.formatted(escapeJson(body), Instant.now().toString(), body.length());

                    sendResponse(exchange, response, 200);
                } else {
                    sendResponse(exchange, "{\"error\": \"Method not allowed\"}", 405);
                }
            } catch (Exception e) {
                sendResponse(exchange, "{\"error\": \"Internal server error\"}", 500);
            }
        });

        server.setExecutor(Executors.newFixedThreadPool(4));
        server.start();

        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            System.out.println("Shutting down server...");
            server.stop(5);
        }));

        System.out.println("Server started on port " + PORT);
    }

    private static void sendResponse(HttpExchange exchange, String response, int code) throws IOException {
        exchange.getResponseHeaders().set("Content-Type", "application/json");
        exchange.sendResponseHeaders(code, response.getBytes().length);
        try (OutputStream os = exchange.getResponseBody()) {
            os.write(response.getBytes());
        }
    }

    private static String escapeJson(String input) {
        if (input == null) return "";
        return input
            .replace("\\", "\\\\")
            .replace("\"", "\\\"")
            .replace("\n", "\\n")
            .replace("\r", "\\r")
            .replace("\t", "\\t");
    }
}
