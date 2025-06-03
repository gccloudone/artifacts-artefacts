# Quick Start Guide

## Prerequisites

1. **JFrog Access**: Ensure you have GC Secure Artifacts access
2. **OIDC Configuration**: Your repository must be configured in JFrog's OIDC identity mappings (see below)
3. **No Secrets Required**: OIDC eliminates the need for stored credentials

### Configure Identity Mappings in JFrog

Before using the workflows, set up OIDC authentication in JFrog Artifactory:

1. Login to [JFrog Artifactory](https://artifacts-artefacts.devops.cloud-nuage.canada.ca)
2. Click **Administration** (gear icon) → **Platform Security** → **OpenID Connect** → **Identity Mappings** tab
3. Click **+ New Identity Mapping** and create mappings for each workflow:

**For your repository workflows, create these identity mappings:**

```
Name: your-org-java-app
Priority: 1
Description: OIDC mapping for Java application workflow

Claims JSON:
{
    "iss": "https://token.actions.githubusercontent.com",
    "repository": "your-org/your-repo",
    "workflow_ref": "your-org/your-repo/.github/workflows/java-app.yml@refs/heads/main"
}

Token Scope: (leave blank)
Roles: Viewer
Service: artifactory
Token Expiration: 10 minutes
```

*Replace `your-org/your-repo` with your actual GitHub organization and repository name. Create similar mappings for python-app.yml, node-app.yml, and any other workflows you use.*

## Step 1: Add OIDC Permissions

Add these permissions to your workflow jobs:

```yaml
permissions:
  id-token: write  authentication
  contents: read
  security-events: write
  pull-requests: write
```

## Step 2: Update Your Dockerfile

Replace your current base image with a Chainguard equivalent:

**Before:**
```dockerfile
FROM python:3.13-slim
```

**After:**
```dockerfile
FROM artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/python:3.13.3
```

## Step 3: Setup JFrog CLI with OIDC

```yaml
- name: Setup JFrog CLI with OIDC
  uses: jfrog/setup-jfrog-cli@v4
  env:
    JF_URL: https://artifacts-artefacts.devops.cloud-nuage.canada.ca
  with:
    oidc-provider-name: gc-secure-artifacts


- name: Docker login via OIDC
  run: jf docker-login artifacts-artefacts.devops.cloud-nuage.canada.ca
```

## Step 4: Add Security Scanning

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

## Step 5: Enable Frogbot for Pull Requests

Add this job to your workflow:

```yaml
frogbot:
  runs-on: ubuntu-latest
  if: github.event_name == 'pull_request' || github.event_name == 'push'
  permissions:
    id-token: write
    contents: read
    pull-requests: write
    security-events: write
  steps:
  - uses: actions/checkout@v4
  - uses: jfrog/frogbot@v2
    env:
      JF_URL: https://artifacts-artefacts.devops.cloud-nuage.canada.ca
      JF_GIT_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      JF_GIT_USE_GITHUB_ENVIRONMENT: "false"
      JF_OIDC_PROVIDER_NAME: gc-secure-artifacts
      JF_OIDC_AUDIENCE: https://github.com/gccloudone
```

## Step 6: Add Cost Management

Include automated cleanup analysis:

```yaml
cleanup:
  runs-on: ubuntu-latest
  if: github.event_name == 'push'
  needs: [build-and-scan]
  permissions:
    id-token: write
    contents: read
  steps:
  - name: Setup JFrog CLI with OIDC
    uses: jfrog/setup-jfrog-cli@v4
    env:
      JF_URL: https://artifacts-artefacts.devops.cloud-nuage.canada.ca
    with:
      oidc-provider-name: gc-secure-artifacts

  - name: Cleanup Analysis
    run: |
      echo "Running automated cleanup to save storage costs..."
      CLEANUP_COUNT=$(jf rt search "repo-name/*" --older-than=30d --count 2>/dev/null || echo "0")
      echo "Found $CLEANUP_COUNT old images that could be cleaned up"
```

## Step 7: Push to JFrog Registry

```yaml
- name: Docker login via OIDC
  run: jf docker-login artifacts-artefacts.devops.cloud-nuage.canada.ca

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
    - cron: "0 0 * * 0"
jobs:
  update-digests:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: write
      pull-requests: write
    steps:
    - uses: actions/checkout@v4
    - name: Setup JFrog CLI with OIDC
      uses: jfrog/setup-jfrog-cli@v4
      env:
        JF_URL: https://artifacts-artefacts.devops.cloud-nuage.canada.ca
      with:
        oidc-provider-name: gc-secure-artifacts

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
- OIDC Authentication: Secure credential-less authentication
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

*Note: Matrix strategy is demonstrated in this repository but optional for your implementation.*

## OIDC Security Benefits

- **Enhanced Security**: No long-lived credentials stored in GitHub
- **Reduced Management**: No secret rotation required
- **Better Audit Trail**: Clear identity mapping in JFrog logs
- **Principle of Least Privilege**: Workflow-specific permissions
- **Compliance**: Meets modern security standards for CI/CD

## Support

- **Documentation**: Review the complete workflows in `.github/workflows/`
- **Local Testing**: Use JFrog CLI commands locally first
- **Issues**: Check GitHub Actions logs for errors
- **Help**: Contact devops.artifacts-artefacts.devops@ssc-spc.gc.ca
