# GC Secure Artifacts

Shared Services Canada (SSC) has initiated a one-year pilot project of [GC Secure Artifacts](https://artifacts-artefacts.devops.cloud-nuage.canada.ca), a secure, scalable, centralized artifact management service underpinned by the JFrog Enterprise+ platform, self-hosted on the GC Private Cloud. 

Available to all federal departments and agencies, this service represents SSC's initial venture into a unified DevSecOps service, designed to bolster software supply chain security and expedite delivery across the Government of Canada. Outcomes of this pioneering initiative will contribute to the decision-making process regarding the project's long-term sustainability and potential expansion.

For access to GC Secure Artifacts, please proceed by completing the [Secure Artifact Management Onboarding Form](https://forms-formulaires.alpha.canada.ca/en/id/cmavw8p4l006eyi01cx1qtxxd).

## Background

This service supports the Government of Canada's efforts to reduce duplication. While departments currently maintain independent Artifactory instances, a centralized approach provides potential access to advanced features. These features, such as JFrog Advanced Security and/or Runtime, could be cost-prohibitive for individual departments but become feasible through pooled resources. By offering a unified secure service, we can improve cybersecurity and delivery speed while creating potential for significant savings.

GC Secure Artifacts, by consolidating efforts across departments, aims to:

- **Reduce duplication**: Eliminate the need for each department to purchase and manage its own tools.
- **Strengthen national security**: Through standardizing controls and policies involving software supply chains.
- **Accelerate development**: Enables developer teams to reuse trusted components without waiting for manual security approvals.
- **Support compliance**: Maintains traceability throughout the Software Development Life Cycle (SDLC) to meet audit and policy demands.

For further insight into the GC Secure Artifacts initiative, below is an presentation (unclassified) previously presented at the Architectural Review Committee at SSC.

- [GC Secure Artifacts Presentation](https://gccloudone.blob.core.windows.net/artifacts-artefacts/unclassified/gc-secure-artifacts.pptx)

## Features

### JFrog Platform

JFrog Platform (Enterprise Plus) offers an enterprise-grade solution for publishing and consuming build artifacts and container images.

The platform provides:

* A centralized registry for internal builds and deployments
* Advanced access controls and repository segmentation
* Built-in vulnerability scanning (via JFrog Xray)
* Support for multiple package types (Docker, Maven, NPM, Nuget, Helm, etc.)

### Chainguard Secure Images

Chainguard is a robust security tool with no known Common Vulnerabilities and Exposures (CVEs), indicating a high level of safety. The images it provides are distroless, minimal, signed, and Software Bill of Materials (SBOM) enabled, serving as a secure-by-default base layer for application development.

These images have been set up as a pull through from Chainguard's registry to our JFrog Artifactory instance and available to anyone from within the GC.

The container images which are available:

*	Python
*	OpenJDK (JDK & JRE)
*	PowerShell
*	Node.js
*	ASP.NET Runtime
*	.NET Runtime
*	.NET SDK

## Additional Documentation

For more detailed information on our project standards and guidelines, kindly refer to the following documents:

- [Artifactory Standards](./docs/artifactory-standards.md)
- Additional documents will be uploaded soon

## Feedback and Contributions

We appreciate and welcome your inputs and suggestions to continuously improve this service to support departmental and/or agency needs. 

Feel free to share your feedback by emailing us at [devops.artifacts-artefacts.devops@ssc-spc.gc.ca](mailto:devops.artifacts-artefacts.devops@ssc-spc.gc.ca).

## Resources

* [Chainguard](https://chainguard.dev/)
* [JFrog Devops Platform](https://jfrog.com/)
* [jFrog Academy](https://academy.jfrog.com/)
