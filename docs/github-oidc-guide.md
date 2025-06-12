# Authenticate GitHub Actions with JFrog OIDC 

## 1. Introduction

In modern CI/CD pipelines, storing long‑lived tokens or API keys in repository secrets is both risky and burdensome. Workload‑based identity (WBID) leverages OpenID Connect (OIDC) to issue short‑lived, audience‑restricted tokens on‑the‑fly. When GitHub Actions needs to interact with JFrog (e.g., Artifactory), WBID allows your workflow to request a JSON Web Token (JWT) from GitHub’s OIDC provider, then exchange it directly with JFrog for a temporary access token—without embedding any static credentials.

This tutorial will:

1. Explain the benefits of using workload‑based identity for secure authentication.
2. Walk through creating identity mappings in JFrog.
3. Provide a sample GitHub Actions workflow that fetches a JFrog access token and runs CLI commands.

> **Tip:** Anyone with admin access to a JFrog instance and `owner` rights in a GitHub org (or admin rights in a personal repo) can follow these steps. The instructions assume your JFrog version is 7.94.1 or newer.

---

## 2. Why Workload‑Based Identity?

1. **No More Long‑Lived Secrets**: Static tokens or API keys, when leaked or rotated insufficiently, become major security risks. WBID issues tokens valid for just a few minutes.
2. **Least‑Privilege Access**: Through identity mappings, you grant each workflow only the precise permissions it needs (e.g., push to a specific repository path). A compromised runner cannot perform arbitrary operations.
3. **Automatic Rotation & Auditing**: Because JFrog OIDC tokens expire quickly, there’s no need to rotate secrets manually. JFrog logs every token exchange—providing a clear audit trail of which workflow pulled artifacts or published packages.
4. **Simplified Revocation**: If you remove or modify an identity mapping, any tokens issued under the old mapping immediately stop working.
5. **Better Developer Experience**: Teams can focus on writing workflows without worrying about creating or managing API keys in each GitHub org.

---

## 3. Prerequisites

1. **JFrog Platform Access**: Project Admin privileges in FFrog . 
2. **GitHub Repository**: In an organization‑owned repo, you need `owner` role in your GitHub org; in a personal repo, you need admin (or repo admin) rights to set up repository settings and enable OIDC in workflows.
4. **JFrog CLI**: We’ll use the `jfrog/setup-jfrog-cli@v4` action, which automatically handles OIDC under the hood.
5. **Basic JSON Familiarity**: You’ll create small JSON objects for claims mapping.

---

## 4. Create Identity Mappings in JFrog

Your JFROG admin has already created the Github Action identity provider. As a Project admin you must create the Project Maappings.

An identity mapping tells JFrog which OIDC claims to inspect and how to translate them into JFrog permissions or project scopes.

1. In JFrog, navigate to **Administration → General Management → Manage Integrations → Your OIDC integration → Identity Mappings**.
2. Click **Add Identity Mapping** and choose **Global** or **Project** scope:

   * **Global**: Applies across all projects.
   * **Project**: Applies only to the selected project (e.g., `myteam-project`).
3. Fill in the fields:

   * **Name**: e.g., `myorg-datahub-images`.
   * **Priority**: `1` (highest). Lower numbers take precedence.
   * **Description**: “Allow GitHub Actions from my‑org/datahub‑images to pull/push packages.”
   * **Claims JSON**: Match fields in the JWT. Example:

     ```json
     {
       "iss": "https://token.actions.githubusercontent.com",
       "repository": "my‑org/datahub‑images",
       "workflow": "build-and-publish"
     }
     ```

     * `"iss"` must be exactly `https://token.actions.githubusercontent.com`.
     * `"repository"` must match your GitHub repo in `owner/repo` format (case sensitive).
     * `"workflow"` is the workflow filename without `.yml` or `.yaml`. If your file is `.github/workflows/build-and-publish.yml`, GitHub sets `"workflow": "build-and-publish"`.
   * **Token Scope** (for Global): Choose **User**, **Group**, or **Admin**. In Project scope, select one or more project roles (e.g., `Project Admin`).
   * **Services**: Select which JFrog services this mapping applies to (e.g., `artifactory.*` or “All”).
   * **Expiration Time**: Defaults to `1` (one minute). You can raise up to `1440` (24 hours). We recommend 5–10 minutes.
4. Click **Save** to finalize the mapping.

> **Quick Sanity Check:** After saving, verify the mapping appears under Global or Project. If it’s project‑scoped, ensure the correct project is selected.

---

## 5. Configure Your GitHub Actions Workflow

Below is a generic example to copy into `.github/workflows/ci‑jfrog.yml` in your repo:



### 5.1 How This Workflow Works

1. **Permissions**: `id-token: write` lets GitHub issue an OIDC JWT. Without it, `setup-jfrog-cli` can’t fetch a token.
2. **`jfrog/setup-jfrog-cli@v4`**:

   * Calls `core.getIDToken()` to request a JWT from GitHub’s OIDC endpoint.
   * Exchanges that JWT against JFrog’s `/access/api/v1/oidc/token` using your `oidc-provider-name`.
   * JFrog validates the token’s claims against your identity mapping. If they match, it returns a short‑lived access token.
   * The action injects that token into the CLI environment so subsequent `jf` commands authenticate automatically.
3. **Subsequent `jf` calls**: Once configured, run any `jf` commands (`jf rt ping`, `jf rt u`, `jf rt download`, `jf rt bce`, `jf rt bag`, `jf rt bp`) without manual token handling.

> **Note:** You do **not** need to `export JF_ACCESS_TOKEN` manually—`setup-jfrog-cli` configures everything.

