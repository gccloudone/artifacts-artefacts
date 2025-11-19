# Chainguard Hardened Container Images

**Purpose:** This page provides guidance for departments on securely consuming Chainguard-hardened container images through Shared Services Canada (SSC).

Chainguard offers a broad catalogue of minimal, hardened container base images with a strong emphasis on security. Regularly updated, these images come with integrated SBOMs (Software Bill of Materials) and are maintained to ensure they contain no known security vulnerabilities at the moment of release.

SSC has enabled secure, internal access to these images for departments across the Government of Canada (GC), supporting a more resilient software supply chain.

## Background

By selecting Chainguard images as base images, departments can significantly reduce the number of CVEs in their containers. Common risk-prone components are either eliminated or replaced with safer alternatives. This approach directly supports the Government of Canada’s Cyber Security Strategy by strengthening software supply chain security and reducing vulnerabilities.

Artifactory has been set up as a pull-through cache from Chainguard's registry to our JFrog Artifactory instance and is available to anyone within the GC. Artifactory acts as a mirror for Chainguard images, enabling teams to retrieve base images from a trusted internal source instead of from the public internet. This not only enhances build speeds but also avoids rate limits and potential network issues when pulling images.

## Policies and Procedures

This section outlines the policies and procedures for working with Chainguard images.

### Using Chainguard Images

Artifactory’s container registry is accessible through the Docker repository `docker-chainguard-remote`, which functions as a pull-through cache.

To pull Chainguard-procured images:

```sh
# Login to Artifactory
docker login artifacts-artefacts.devops.cloud-nuage.canada.ca

# Pull Python
docker pull artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/python:3.13.3

# Pull Node.js
docker pull artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/node:23.11.0-slim
```

Using the internal registry offers quicker and more reliable access. If the image has been previously pulled, it is served directly from Artifactory’s cache. Furthermore, all downloads are automatically logged and scanned by **JFrog XRay** for vulnerabilities.

Departments can also request to have designated users being B2B federated with SSC's enterprise tenant and then could gain direct access to the Chainguard Portal and set up their own pull based tokens. While this enables teams to explore the full image catalogue and manage access to container images directly, the preferred and most efficient method remains pulling images through GC Secure Artifacts.

#### Login Process to Chainguard Portal

The login process for users who wish to get direct access to the Chainguard Portal is as follows.

- User goes to https://console.chainguard.dev/auth/login
- Then they click "Use Your Identity Provider"
- Then they click "Use Organization Name"
- Then they type "ssc-spc.gc.ca"
- Then they click "Login with Provider"
- Then they get redirected to Entra ID

At which point once the user accounts are seen in the portal we usually elevate the user account to owner so those accounts can create their own pull tokens.

## Procurement

Chainguard has provided **Shared Services Canada (SSC)** with a list of all departments currently signed up to consume their container images.

To streamline procurement and maximize value across GC, we are actively working towards a "pooled" approach. In this model, SSC will act as the central repository, enabling all participating departments with container image needs to access and share resources. This collaborative strategy promotes efficiency while allowing licensing costs to decrease as the total quantity of images purchased increases, resulting in cost savings over time.

Chainguard licensing is based on a per-image model, which includes access to all supported versions of each image. To view the complete directory of over 1,750 hardened container images, including supported versions, SBOMs, comparisons to upstream CVEs, and other critical details.

- [Chainguard image directory](https://images.chainguard.dev/directory?category=all).

### Next Steps and Your Input

SSC is still evaluating how Chainguard procurement could work going forward and would appreciate everyone's input on our proposed model. Your feedback will be shared with Senior Management and directly contribute to shaping the final offering.

To assist in understanding our plans and facilitate discussions, we have attached two decks:

- [Chainguard Progress Deck](https://gccloudone.blob.core.windows.net/artifacts-artefacts/unclassified/chainguard-progress-deck.pdf)
- [Chainguard Technical Deck](https://gccloudone.blob.core.windows.net/artifacts-artefacts/unclassified/chainguard-technical-deck.pdf)

We would love to hear your feedback and any questions you may have:

- [devops.artifacts-artefacts.devops@ssc-spc.gc.ca](mailto:devops.artifacts-artefacts.devops@ssc-spc.gc.ca)

### Procured Chainguard Images

The following hardened container images have already been procured:

| **Image Name**       | **Renewal Date** | **Department** | **Notes**                         |
|----------------------|------------------|----------------|-----------------------------------|
| Python               | 2026-03-01       | SSC            | For Python-based applications     |
| ASP.NET Runtime      | 2026-03-01       | SSC            | For .NET ASP.NET-based frameworks |
| .NET Runtime         | 2026-03-01       | SSC            | General-purpose .NET runtime      |
| .NET SDK             | 2026-03-01       | SSC            | For .NET software development     |
| PowerShell           | 2026-03-01       | SSC            | For PowerShell scripting          |
| OpenJDK (JDK & JRE)  | 2026-03-01       | SSC            | Java runtime and development kit  |

### Potential Chainguard Images

The following hardened container images are under active consideration:

| **Image Name**               | **Renewal Date** | **Department**   | **Type**    | **Notes**                                      |
|------------------------------|------------------|------------------|-------------|------------------------------------------------|
| external-dns-iamguarded      | TBD              | CSE              | Helm        | For managing external DNS records              |
| kafka-iamguarded             | TBD              | CSE              | Helm        | For distributed messaging systems              |
| kube-state-metrics-iamguarded| TBD              | CSE              | Helm        | Monitors Kubernetes cluster state              |
| logstash-iamguarded          | TBD              | CSE              | Helm        | For data collection and processing             |
| minio-iamguarded             | TBD              | CSE              | Helm        | High-performance object storage                |
| mongodb-iamguarded           | TBD              | CSE              | Helm        | NoSQL database                                 |
| mongodb-sharded-iamguarded   | TBD              | CSE              | Helm        | Sharded MongoDB cluster                        |
| nginx-iamguarded             | TBD              | CSE              | Helm        | High-performance web server/proxy              |
| rabbitmq-iamguarded          | TBD              | CSE              | Helm        | For message queuing and communication          |
| thanos-iamguarded            | TBD              | CSE              | Helm        | For highly available Prometheus setup          |
| fluent-bit-iamguarded        | TBD              | CSE              | Helm        | Log processor and forwarder                    |
| grafana-iamguarded           | TBD              | CSE              | Helm        | For monitoring and visualization               |
| grafana-loki-iamguarded      | TBD              | CSE              | Helm        | Log aggregation and querying                   |
| grafana-operator-iamguarded  | TBD              | CSE              | Helm        | Manages Grafana instances in Kubernetes.       |
| kube-prometheus-iamguarded   | TBD              | CSE              | Helm        | Monitors Kubernetes with Prometheus            |
| metalb-iamguarded            | TBD              | CSE              | Helm        | Load balancer for Kubernetes                   |
| neo4j-iamguarded             | TBD              | CSE              | Helm        | Graph database                                 |
| oauth2-proxy-iamguarded      | TBD              | CSE              | Helm        | Authentication proxy for OAuth2                |
| opensearch-iamguarded        | TBD              | CSE              | Helm        | Search and analytics engine                    |
| solr-iamguarded              | TBD              | CSE              | Helm        | Search platform for structured data            |
| vault-iamguarded             | TBD              | CSE              | Helm        | Secrets management tool                        |
| postgres                     | TBD              | CCCS             | Application | Relational database system                     |
| Kubernetes-event-exporter    | TBD              | CCCS             | Application | Monitors and exports Kubernetes events         |
| nginx-controller             | TBD              | CCCS             | Application | Manages NGINX deployments                      |
| external-dns                 | TBD              | CCCS             | Application | For managing external DNS records              |
| oauth2-proxy                 | TBD              | CCCS             | Application | Authentication proxy for OAuth2                |
| httpd                        | TBD              | NRCAN            | Application | Apache HTTP server                             |
| neo4j                        | TBD              | NRCAN            | Application | Graph database                                 |
| nginx                        | TBD              | NRCAN            | Application | High-performance web server/proxy              |
| postgis                      | TBD              | NRCAN            | Application | Geospatial database extension for PostgreSQL   |
| pytorch                      | TBD              | NRCAN            | Application | Open-source machine learning framework         |
| geoserver                    | TBD              | NRCAN            | Application | Open-source server for geospatial data         |
| osgeo/gdal                   | TBD              | NRCAN            | Application | Geospatial Data Abstraction Library            |
| qgis                         | TBD              | NRCAN            | Application | Geographic Information System software         |
| grass-gis                    | TBD              | NRCAN            | Application | Open-source geographic information system      |
| pygeoapi                     | TBD              | NRCAN            | Application | Standards-based geospatial data API            |
| Nginx Ingress Controller     | TBD              | Service Canada   | Application | Manages routing traffic in Kubernetes          |
| Cert Manager                 | TBD              | Service Canada   | Application | Automates creation/renewal of TLS certificates |
| Valkey                       | TBD              | Service Canada   | Application | Manages secure key and certificate storage     |
| falco-no-driver              | TBD              | SSC              | Application | Monitor and Capture Linux Kernel Events        |
| sysdig                       | TBD              | SSC              | Application | Monitor and Capture Container Events           |
 

## Frequently Asked Questions

**Q. Can’t the Government of Canada build similar functionality internally?**

While this is possible, developing an equivalent to Chainguard's offering would require significant time, resources, and specialized expertise. A formal business value assessment is currently underway to evaluate the time, cost, and potential challenges involved in developing a comparable solution.

**Q. Have other governments implemented similar solutions?**

Yes, many governments have implemented similar solutions. For example, **Gov.UK** has adopted hardened container images as a key element of their security practices. Adam Moss of the UK’s Department for Work and Pensions (DWP) has shared how this initiative improved their security posture and saved considerable time. Mr. Moss is available to present insights at upcoming events to help inform our decisions.
