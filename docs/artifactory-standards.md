# Artifactory Standards

Standards for the management of Artifactory.

## Background

Shared Services Canada (SSC) is implementing a 1-year experiment of operating a Government of Canada centralized Artifactory instance. The results of this experiment will feed into a decision of whether to renew/continue the project.

## Purpose

This document outlines the policies and procedures of operating the centralized Artifactory instance.

## Policies and Procedures

### Configuration Management

1. **Configuration as Code**

   All configuration of Artifactory and/or X-Ray shall be performed using the Configuration as Code [repository](https://github.com/gccloudone/artifacts-configuration) hosted in the GC Cloud One organization on GitHub, to the extent supported by the JFrog Terraform modules.

### User Management

2. **Centralized Authentication**

   Users will authenticate using Single Sign-On (SSO) from the 163ENT Entra ID tenant.

   - Users not already in the 163ENT tenant must request an invite [here](https://forms-formulaires.alpha.canada.ca/en/id/cmapffzfp00v9xb017pnmyb94)

3. **Local Accounts**

   Local accounts will not be utilized, except for any break glass accounts.

4. **Administrators**

   The number of “global administrators” should be limited to at-most 3 individuals.

### Project Management

5. **Project Eligibility**

   The following entities are eligible for a Project in Artifactory

   - Government of Canada Department or Agency
   - Shared Services Canada (SSC) Service Line

6. **Project Naming**

   Projects must be named with the entity’s name.

   Project Keys will use the entity’s official acronym (e.g., ssc, statcan)

   - SSC Service Lines shall be named `SSC – [Service Line]`. Keys are prefixed with `ssc-`

7. **Project Ownership**

   Projects must have at least 2 administrators and should ideally have 3.

   - Projects with no active administrators are to be removed once identified.
   - Project Administrators must notify by [email](mailto:devops.artifacts-artefacts.devops@ssc-spc.gc.ca) when an administrator departs their organization or when changing roles. If the total number of administrators will drop to 1, the Project Administrators must identify a new administrator.

8. **Project Management**

   Project Administrators are responsible for managing all aspects of their project, including:

   - Repository management
   - User permissions
   - Retention periods

9. **Project Support**

   Project Administrators are expected to be the “first-line” support for their organization, and will be the contact point for escalations to SSC.

10. **Project Quotas**

    Projects should have a default quota for 200GB, expandable upon request.

### Repository Management

11. **Repository Naming**

    Repositories should follow the naming convention: `[org]-[group]-[project]-[type]-[locator]`, where:

    - [org] represents the owning entity (this is automatically prefixed)
    - [group] represents the group within the owning entity (this is automatically prefixed for SSC Service Lines)
    - [project] represents the project the repository belongs to (optional)
    - [type] represents the repository type (e.g., docker, debian, helm)
      - For OS distributions, `type` may be replaced by the OS name (e.g., ubuntu)
    - [locator] represents the locator. Values are:
      - remote
      - local
      - federated
      - virtual (value is omitted in the repository name)

12. **Common Repositories**

    SSC will configure common repositories for use by all projects to prevent duplication across all organisations.

    - Common repositories include:
      - Operating System distributions (e.g., Debian, Ubuntu, RedHat Enterprise Linux)
      - Common Community Repositories (e.g., Maven, PyPI, Docker Hub, Quay.io, Helm)
      - Common repositories will follow a different naming convention than normal repositories, `[type]-[locator]`

## Contact Us

If you have any questions or feedback, feel free to reach out to us at [email](mailto:devops.artifacts-artefacts.devops@ssc-spc.gc.ca).
