package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import java.time.Instant;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

@SpringBootApplication
@RestController
public class App {

    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }

    @GetMapping("/")
    public Map<String, Object> healthCheck() {
        Map<String, Object> response = new HashMap<>();
        response.put("status", "healthy");
        response.put("service", "java-springboot-api");
        response.put("timestamp", Instant.now().toString());
        response.put("version", "1.0.0");
        return response;
    }

    @GetMapping("/api/info")
    public Map<String, Object> getInfo() {
        Map<String, Object> response = new HashMap<>();
        response.put("service", "GC Secure Artifacts Java Demo");
        response.put("description", "Minimal Spring Boot API for Chainguard/JFrog POC");
        response.put("features", Arrays.asList(
            "Chainguard base image",
            "JFrog Artifactory integration", 
            "Xray vulnerability scanning",
            "SBOM generation"
        ));
        response.put("javaVersion", System.getProperty("java.version"));
        response.put("springBootVersion", "3.2.1");
        return response;
    }

    @PostMapping("/api/echo")
    public Map<String, Object> echo(@RequestBody Map<String, Object> data) {
        Map<String, Object> response = new HashMap<>();
        response.put("received", data);
        response.put("timestamp", Instant.now().toString());
        return response;
    }
}