# Chainguard Images

Chainguard offers a broad catalogue of minimal, hardened container base images with a strong emphasis on security. Regularly updated, these images come with integrated SBOMs (Software Bill of Materials) and are maintained to ensure they contain no known security vulnerabilities at the moment of release.

## Background

By selecting Chainguard images as your base images, you can significantly cut down on the number of CVEs in your container. This is because commonplace risk-prone components are either eliminated or replaced with safer alternatives. This aligns with the GoC’s cyber security strategy to reduce vulnerabilities in our software supply chain.

Artifactory has been set up as a pull through from Chainguard's registry to our JFrog Artifactory instance and available to anyone from within the GC. In other words, Artifactory acts as a mirror for Chainguard images, enabling you to retrieve base images from a local trusted source instead of through the public internet. This not only enhances build speeds, but also sidesteps any potential rate limiting and/or network-related issues when pulling images.

The container images which are available:

* Python
* OpenJDK (JDK & JRE)
* PowerShell
* Node.js
* ASP.NET Runtime
* .NET Runtime
* .NET SDK

## Purpose

This document outlines the policies and procedures for working with Chainguard images.

## Policies and Procedures

### Using Chainguard Images

Artifactory’s container registry is set up through a Docker repository named `docker-chainguard-remote`, available as a pull-through cache.

To pull the Chainguard procured images, follow these steps:

```sh
# Login to Artifactory
docker login artifacts-artefacts.devops.cloud-nuage.canada.ca

# Pull Python
docker pull artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/python:3.13.3

# Pull Node
docker pull artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/node:23.11.0-slim
```

Utilizing the internal registry comes with the advantage of quicker and more reliable access if the image has been previously pulled. It will be served from Artifactory’s cache, and all downloads are automatically logged and scanned by JFrog XRay.
