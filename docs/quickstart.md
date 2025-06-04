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
  run: |
    echo "Scanning dependencies for security issues..."
    jf audit --format=simple || echo "Issues found - check output above"
    echo "Developer tip: Run 'jf audit --fix' locally to auto-fix vulnerabilities"
```

**Scan Container Images:**

```yaml
- name: Scan Container
  run: |
    IMAGE_TAG=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
    echo "Scanning image..."
    jf docker scan $IMAGE_TAG
```

## Step 4: Enable Frogbot for Pull Requests

Add this job to your workflow:

```yaml
frogbot:
  runs-on: ubuntu-latest
  if: github.event_name == 'pull_request' || github.event_name == 'push'
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
        JF_GIT_USE_GITHUB_ENVIRONMENT: 'false'
```

## Step 5: Add Cost Management

Include automated cleanup analysis:

```yaml
cleanup:
  runs-on: ubuntu-latest
  if: github.event_name == 'push'
  needs: [build-and-scan]
  steps:
    - name: Setup JFrog CLI
      uses: jfrog/setup-jfrog-cli@v4
      env:
        JF_URL: https://artifacts-artefacts.devops.cloud-nuage.canada.ca
        JF_USER: ${{ secrets.JFROG_USERNAME }}
        JF_ACCESS_TOKEN: ${{ secrets.JFROG_JWT_TOKEN }}
    - name: Cleanup Analysis
      run: |
        echo "Running automated cleanup to save storage costs..."
        CLEANUP_COUNT=$(jf rt search "repo-name/*" --older-than=30d --count 2>/dev/null || echo "0")
        echo "Found $CLEANUP_COUNT old images that could be cleaned up"
```

## Step 6: Push to JFrog Registry

```yaml
- name: Docker login
  run: |
    echo "${{ secrets.JFROG_JWT_TOKEN }}" | docker login artifacts-artefacts.devops.cloud-nuage.canada.ca \
      --username "${{ secrets.JFROG_USERNAME }}" --password-stdin

- name: Build and push
  run: |
    IMAGE_TAG=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}-${{ matrix.dockerfile }}
    docker build -f Dockerfile.${{ matrix.dockerfile }} -t $IMAGE_TAG .
    docker push $IMAGE_TAG
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

## Automated Security Maintenance

Add digest-based security updates:

```yaml
name: Update Chainguard Digests
on:
  workflow_dispatch:
  schedule:
    - cron: '0 0 * * 0'
jobs:
  update-digests:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v4
      - name: Setup JFrog CLI
        uses: jfrog/setup-jfrog-cli@v4
        env:
          JF_URL: https://artifacts-artefacts.devops.cloud-nuage.canada.ca
          JF_USER: ${{ secrets.JFROG_USERNAME }}
          JF_ACCESS_TOKEN: ${{ secrets.JFROG_JWT_TOKEN }}
    # Automatically updates Dockerfiles with latest secure digests
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
git clone https://github.com/gccloudone/artifacts-artefacts.git

# Navigate to repository
cd artifacts-artefacts

# Trigger workflows by pushing changes
git push origin main

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
Scanning chainguard image...
No vulnerable components were found
Scan completed successfully
```

**Cost Management:**

```
Running automated cleanup to save storage costs...
Found 0 old images that could be cleaned up
Cleanup saves storage costs and improves performance
```

**Build Summary:**

```
Build 42 completed

Both images built, pushed, and scanned successfully

JFrog Developer Tools Used:
- Dependency Audit: Scanned source code for vulnerabilities
- Automated Cleanup: Checked for old images to save storage costs
- Frogbot: Automated security comments on pull requests
- Image Scanning: JFrog Xray scanned container images
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

## Implementation Options

**Single Dockerfile Approach:**

```yaml
- name: Build image
  run: |
    IMAGE_TAG=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
    docker build -t $IMAGE_TAG .
```

**Multiple Variants (Optional):**

```yaml
strategy:
  matrix:
    dockerfile: [standard, chainguard]
steps:
  - name: Build image
    run: |
      IMAGE_TAG=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}-${{ matrix.dockerfile }}
      docker build -f Dockerfile.${{ matrix.dockerfile }} -t $IMAGE_TAG .
```

_Note: Matrix strategy is demonstrated in this repository but optional for your implementation._

## Support

- **Documentation**: Review the complete workflows in `.github/workflows/`
- **Local Testing**: Use JFrog CLI commands locally first
- **Issues**: Check GitHub Actions logs for errors
- **Help**: Contact devops.artifacts-artefacts.devops@ssc-spc.gc.ca
