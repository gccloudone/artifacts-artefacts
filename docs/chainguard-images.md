# Chainguard Hardened Container Images

Chainguard offers a broad catalogue of minimal, hardened container base images with a strong emphasis on security. Regularly updated, these images come with integrated SBOMs (Software Bill of Materials) and are maintained to ensure they contain no known security vulnerabilities at the moment of release.

## Background

By selecting Chainguard images as your base images, you can significantly reduce the number of CVEs in your containers. This is because commonplace risk-prone components are either eliminated or replaced with safer alternatives. This initiative aligns with the Government of Canada's (GC’s) Cyber Security Strategy to safeguard software supply chains and reduce vulnerabilities.

Artifactory has been set up as a pull-through cache from Chainguard's registry to our JFrog Artifactory instance and is available to anyone within the GC. Artifactory acts as a mirror for Chainguard images, enabling teams to retrieve base images from a trusted internal source instead of from the public internet. This not only enhances build speeds but also avoids rate limits and potential network issues when pulling images.

## Policies and Procedures

This document outlines the policies and procedures for working with Chainguard images.

### Using Chainguard Images

Artifactory’s container registry is set up through a Docker repository named `docker-chainguard-remote`, which operates as a pull-through cache. To pull Chainguard-procured images, follow these steps:

```sh
# Login to Artifactory
docker login artifacts-artefacts.devops.cloud-nuage.canada.ca

# Pull Python
docker pull artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/python:3.13.3

# Pull Node.js
docker pull artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/node:23.11.0-slim
```

Using the internal registry offers quicker and more reliable access. If the image has been previously pulled, it is served directly from Artifactory’s cache. Furthermore, all downloads are automatically logged and scanned by **JFrog XRay** for vulnerabilities.

## Procurement

Chainguard has provided **Shared Services Canada (SSC)** with a list of all departments currently signed up to consume their container images. 

To streamline procurement and maximize value across GC, we are actively working towards a "pooled" approach. In this model, SSC will act as the central repository, enabling all participating departments with container image needs to access and share resources. This collaborative strategy promotes efficiency while allowing licensing costs to decrease as the total quantity of images purchased increases, resulting in cost savings over time.

Chainguard licensing is based on a per-image model, which includes access to all supported versions of each image. To view the complete directory of over 1,750 hardened container images, including supported versions, SBOMs, comparisons to upstream CVEs, and other critical details.

Please visit the [Chainguard image directory](https://images.chainguard.dev/directory?category=all).

### Next Steps and Your Input

SSC is still evaluating how Chainguard procurement could work going forward and would appreciate everyone's input on our proposed model. Your feedback will be shared with Senior Management and directly contribute to shaping the final offering.

To assist in understanding our plans and facilitate discussions, we have attached two decks:

- [Chainguard Progress Deck](https://gccloudone.blob.core.windows.net/artifacts-artefacts/unclassified/chainguard-progress-deck.pptx)
- [Chainguard Technical Deck](https://gccloudone.blob.core.windows.net/artifacts-artefacts/unclassified/chainguard-technical-deck.pptx)

We would love to hear your feedback and/or any questions you might have!

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

| **Image Name**               | **Renewal Date** | **Department**   | **Notes**                                      |
|------------------------------|------------------|------------------|------------------------------------------------|
| external-dns-iamguarded      | TBD              | CSE              | For managing external DNS records              |
| kafka-iamguarded             | TBD              | CSE              | For distributed messaging systems              |
| kube-state-metrics-iamguarded| TBD              | CSE              | Monitors Kubernetes cluster state              |
| logstash-iamguarded          | TBD              | CSE              | For data collection and processing             |
| minio-iamguarded             | TBD              | CSE              | High-performance object storage                |
| mongodb-iamguarded           | TBD              | CSE              | NoSQL database                                 |
| mongodb-sharded-iamguarded   | TBD              | CSE              | Sharded MongoDB cluster                        |
| nginx-iamguarded             | TBD              | CSE              | High-performance web server/proxy              |
| rabbitmq-iamguarded          | TBD              | CSE              | For message queuing and communication          |
| thanos-iamguarded            | TBD              | CSE              | For highly available Prometheus setup          |
| fluent-bit-iamguarded        | TBD              | CSE              | Log processor and forwarder                    |
| grafana-iamguarded           | TBD              | CSE              | For monitoring and visualization               |
| grafana-loki-iamguarded      | TBD              | CSE              | Log aggregation and querying                   |
| grafana-operator-iamguarded  | TBD              | CSE              | Manages Grafana instances in Kubernetes.       |
| kube-prometheus-iamguarded   | TBD              | CSE              | Monitors Kubernetes with Prometheus            |
| metalb-iamguarded            | TBD              | CSE              | Load balancer for Kubernetes                   |
| neo4j-iamguarded             | TBD              | CSE              | Graph database                                 |
| oauth2-proxy-iamguarded      | TBD              | CSE              | Authentication proxy for OAuth2                |
| opensearch-iamguarded        | TBD              | CSE              | Search and analytics engine                    |
| solr-iamguarded              | TBD              | CSE              | Search platform for structured data            |
| vault-iamguarded             | TBD              | CSE              | Secrets management tool                        |
| postgres                     | TBD              | CCCS             | Relational database system                     |
| Kubernetes-event-exporter    | TBD              | CCCS             | Monitors and exports Kubernetes events         |
| nginx-controller             | TBD              | CCCS             | Manages NGINX deployments                      |
| external-dns                 | TBD              | CCCS             | For managing external DNS records              |
| oauth2-proxy                 | TBD              | CCCS             | Authentication proxy for OAuth2                |
| httpd                        | TBD              | NRCAN            | Apache HTTP server                             |
| neo4j                        | TBD              | NRCAN            | Graph database                                 |
| nginx                        | TBD              | NRCAN            | High-performance web server/proxy              |
| postgis                      | TBD              | NRCAN            | Geospatial database extension for PostgreSQL   |
| pytorch                      | TBD              | NRCAN            | Open-source machine learning framework         |
| geoserver                    | TBD              | NRCAN            | Open-source server for geospatial data         |
| osgeo/gdal                   | TBD              | NRCAN            | Geospatial Data Abstraction Library            |
| qgis                         | TBD              | NRCAN            | Geographic Information System software         |
| grass-gis                    | TBD              | NRCAN            | Open-source geographic information system      |
| pygeoapi                     | TBD              | NRCAN            | Standards-based geospatial data API            |
| Nginx Ingress Controller     | TBD              | Service Canada   | Manages routing traffic in Kubernetes          |
| Cert Manager                 | TBD              | Service Canada   | Automates creation/renewal of TLS certificates |
| Valkey                       | TBD              | Service Canada   | Manages secure key and certificate storage     |

## Frequently Asked Questions

**Q. Can’t the Government of Canada build similar functionality internally?**

While this is possible, developing an equivalent to Chainguard's offering would require significant time, resources, and specialized expertise. A formal business value assessment is currently underway to evaluate the time, cost, and potential challenges involved in developing a comparable solution.

**Q. Have other governments implemented similar solutions?**

Yes, many governments have implemented similar solutions. For example, **Gov.UK** has adopted hardened container images as a key element of their security practices. Adam Moss of the UK’s Department for Work and Pensions (DWP) has shared how this initiative improved their security posture and saved considerable time. Mr. Moss is available to present insights at upcoming events to help inform our decisions.
