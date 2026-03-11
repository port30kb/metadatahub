# metadatahub.eu

A linked data hub for cultural heritage metadata standards, vocabularies, and dataset catalogs. Serves both humans (HTML documentation) and machines (RDF, SPARQL, OAI-PMH) from the same URIs using W3C content negotiation.

## Architecture

Four lightweight components behind a Caddy reverse proxy:

- **Hugo** — Static site generator for human-readable pages and RDF serializations
- **Oxigraph** — Rust-based SPARQL 1.1 endpoint (~15 MB image)
- **Trifid** — Content negotiation layer by Zazuko (powers Switzerland's ld.admin.ch)
- **oai-pmh2** — OAI-PMH harvesting endpoint for K-samsok/Europeana integration

## Quick Start

```bash
# Prerequisites: Docker, Docker Compose, Hugo

# Build the Hugo site
cd hugo && hugo --minify && cd ..

# Start all services
docker compose up -d

# Load RDF data into Oxigraph
./scripts/build.sh
```

## Endpoints

| URL | Service | Description |
|-----|---------|-------------|
| `/` | Hugo | Homepage and documentation |
| `/vocab/*` | Hugo + Trifid | Vocabularies (content-negotiated) |
| `/dataset/*` | Hugo + Trifid | Dataset catalog (content-negotiated) |
| `/sparql` | Oxigraph | SPARQL 1.1 endpoint with YASGUI |
| `/oai` | oai-pmh2 | OAI-PMH harvesting endpoint |
| `/docs/*` | Hugo | Technical documentation |
| `/specs/*` | Hugo | Specification profiles |
| `/guides/*` | Hugo | Practical guides |

## Content Negotiation

Vocabulary and dataset URIs serve different representations based on the `Accept` header:

```bash
# HTML (browser default)
curl -H "Accept: text/html" https://metadatahub.eu/vocab/cidoc-crm/

# Turtle
curl -H "Accept: text/turtle" https://metadatahub.eu/vocab/cidoc-crm/

# JSON-LD
curl -H "Accept: application/ld+json" https://metadatahub.eu/vocab/cidoc-crm/

# RDF/XML
curl -H "Accept: application/rdf+xml" https://metadatahub.eu/vocab/cidoc-crm/
```

## Development

```bash
# Run Hugo dev server with live reload
cd hugo && hugo server -D

# Run full stack locally
docker compose up -d
```

## Directory Structure

```
metadatahub/
  caddy/           Caddyfile reverse proxy config
  hugo/            Hugo site (content, layouts, static assets)
    content/       Markdown + YAML source files
      vocab/       Vocabulary definitions
      dataset/     DCAT-AP catalog entries
      docs/        Technical documentation
      specs/       Specification profiles
      guides/      Practical guides
    layouts/       HTML + RDF output templates
    static/        CSS, images, static assets
  oxigraph/        SPARQL endpoint documentation
  trifid/          Trifid content negotiation config
  oai-pmh/         OAI-PMH endpoint (Dockerfile + config)
  scripts/         Build and data loading scripts
  .github/         CI/CD workflows
```

## License

Content: CC BY 4.0. Software: MIT.
