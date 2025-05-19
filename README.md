# GC Secure Artifact Management

Shared Services Canada (SSC) has initiated a one-year pilot project of [GC Secure Artifacts](https://artifacts-artefacts.devops.cloud-nuage.canada.ca), a secure, scalable, centralized artifact management service underpinned by the JFrog Enterprise+ platform, self-hosted on the GC Private Cloud. Available to all federal departments, this service represents SSC's initial venture into a unified DevSecOps service, designed to bolster software supply chain security and expedite delivery across the Government of Canada. Outcomes of this pioneering initiative will contribute to the decision-making process regarding the project's long-term sustainability and potential expansion.

For access to GC Secure Artifacts, please proceed by completing the [Secure Artifact Management Onboarding Form](https://forms-formulaires.alpha.canada.ca/en/id/cmapffzfp00v9xb017pnmyb94).

## Background

For further insight into the GC Secure Artifacts initiative, below is an presentation (unclassified) previously presented at the Architectural Review Committee at SSC.

- [GC Secure Artifacts Presentation](https://gccloudone.blob.core.windows.net/artifacts-artefacts/unclassified/gc-secure-artifacts.pptx)

## Features

GC Secure Artifacts provides:

* **Artifactory**: A reliable, multi-tenant repository for managing all software components, including open-source, proprietary, and custom-built.

* **Xray**: Performs real-time scanning for vulnerabilities and license compliance, ensuring that only safe and approved code is deployed to production.

GC Secure Artifacts, by consolidating efforts across departments, aims to:

1. **Reduce duplication**: Eliminate the need for each department to purchase and manage its own tools.

2. **Strengthen national security**: Through standardizing controls and policies involving software supply chains.

3. **Accelerate development**: Enables developer teams to reuse trusted components without waiting for manual security approvals.

4. **Support compliance**: Maintains traceability throughout the Software Development Life Cycle (SDLC) to meet audit and policy demands.

> This service aligns with the Government of Canada's initiative on reducing duplication. Currently, many departments have each procured independently an Artifactory instance. However, centralizing procurement could provide us access to advanced features such as JFrog Advanced Security and/or Runtime. By offering a single secure, scalable service for all departments, we can consolidate independently procured instances. This would lead to significant annual savings for the Government of Canada while enhancing cybersecurity and delivery speed.

## Additional Documentation

For more detailed information on our project standards and guidelines, kindly refer to the following documents:

- [Artifactory Standards](./docs/artifactory-standards.md)
- Additional documents will be uploaded soon

## Feedback and Contributions

We appreciate and welcome your inputs and suggestions to continuously improve this service to support departmental and/or agency needs. Feel free to share your feedback by emailing us at [devops.artifacts-artefacts.devops@ssc-spc.gc.ca](mailto:devops.artifacts-artefacts.devops@ssc-spc.gc.ca).

## Resources

* [Chainguard](https://chainguard.dev/)
* [jFrog Devops Platform](https://jfrog.com/)
* [jFrog Academy](https://academy.jfrog.com/)
