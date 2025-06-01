# Quick Start Guide

## Prerequisites

1. **JFrog Access**: Ensure you have GC Secure Artifacts access
2. **Repository Secrets**: Configure these in your GitHub repository:
   - `JFROG_USERNAME`: Your Artifactory username
   - `JFROG_JWT_TOKEN`: Your Artifactory access token

## Step 1: Update Your Dockerfile

Replace your current base image with a Chainguard equivalent:

**Before:**
```dockerfile
FROM python:3.13-slim
```

**After:**
```dockerfile
FROM artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/python:3.13.3
```

## Step 2: Add JFrog CLI to Your Workflow

```yaml
- name: Setup JFrog CLI
  uses: jfrog/setup-jfrog-cli@v4
  env:
    JF_URL: https://artifacts-artefacts.devops.cloud-nuage.canada.ca
    JF_USER: ${{ secrets.JFROG_USERNAME }}
    JF_ACCESS_TOKEN: ${{ secrets.JFROG_JWT_TOKEN }}
```

## Step 3: Add Security Scanning

**Scan Dependencies:**
```yaml
- name: Scan Dependencies
  run: jf audit --format=simple
```

**Scan Container Images:**
```yaml
- name: Scan Container
  run: jf docker scan your-image:tag
```

## Step 4: Enable Frogbot for Pull Requests

Add this job to your workflow:

```yaml
frogbot:
  runs-on: ubuntu-latest
  if: github.event_name == 'pull_request'
  permissions:
    contents: read
    pull-requests: write
    security-events: write
  steps:
  - uses: actions/checkout@v4
  - uses: jfrog/frogbot@v2
    env:
      JF_URL: https://artifacts-artefacts.devops.cloud-nuage.canada.ca
      JF_ACCESS_TOKEN: ${{ secrets.JFROG_JWT_TOKEN }}
      JF_GIT_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Step 5: Push to JFrog Registry

```yaml
- name: Docker login
  run: |
    echo "${{ secrets.JFROG_JWT_TOKEN }}" | docker login artifacts-artefacts.devops.cloud-nuage.canada.ca \
      --username "${{ secrets.JFROG_USERNAME }}" --password-stdin

- name: Build and push
  run: |
    docker build -t artifacts-artefacts.devops.cloud-nuage.canada.ca/your-repo/your-app:${{ github.sha }} .
    docker push artifacts-artefacts.devops.cloud-nuage.canada.ca/your-repo/your-app:${{ github.sha }}
```

## Available Chainguard Images

Use these image paths in your Dockerfiles:

**Java:**
```dockerfile
# JDK for building
FROM artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/jdk:openjdk-21

# JRE for runtime
FROM artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/jre:openjdk-21
```

**Python:**
```dockerfile
FROM artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/python:3.13.3
```

**Node.js:**
```dockerfile
FROM artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/node:24.1.0
```

## Local Development

**Install JFrog CLI:**
```bash
# Configure CLI
jf config add --url=https://artifacts-artefacts.devops.cloud-nuage.canada.ca

# Test connection
jf rt ping

# Scan your project
jf audit

# Get fix suggestions
jf audit --fix
```

**Pull Chainguard Images:**
```bash
# Login
docker login artifacts-artefacts.devops.cloud-nuage.canada.ca

# Pull image
docker pull artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/python:3.13.3
```

## Testing This Repository

Run the examples in this repository:

```bash
# Clone repository
git clone [repository-url]

# Trigger workflows
git push origin artifacts-artefacts/jfrog-cgd-demo

# Check GitHub Actions for results
```

## What You'll See

**JFrog CLI Output:**
```
Scanning dependencies for security issues...
No issues found
Developer tip: Run 'jf audit --fix' locally to auto-fix vulnerabilities
```

**Container Scan Results:**
```
Scanning image...
No vulnerable components were found
Scan completed successfully
```

**Cost Management:**
```
Running automated cleanup to save storage costs...
Found 0 old images that could be cleaned up
```

## Common Commands

**Dependency Scanning:**
```bash
jf audit                    # Scan dependencies
jf audit --fix             # Get fix suggestions
jf audit --format=json     # JSON output
```

**Container Operations:**
```bash
jf docker scan image:tag   # Scan container
jf docker push image:tag   # Push to registry
```

**Repository Management:**
```bash
jf rt search "repo/*"                    # Search artifacts
jf rt delete "repo/*" --older-than=30d   # Clean old artifacts
```

## Support

- **Documentation**: Review the complete workflows in `.github/workflows/`
- **Local Testing**: Use JFrog CLI commands locally first
- **Issues**: Check GitHub Actions logs for errors
- **Help**: Contact devops.artifacts-artefacts.devops@ssc-spc.gc.ca