---
title: "Architecture Overview"
description: "How metadatahub.eu serves humans and machines from one domain using a hybrid Hugo + Oxigraph + Trifid + oai-pmh2 architecture."
date: 2024-09-01
tags:
  - architecture
  - linked-data
  - infrastructure
---

## Components

metadatahub.eu uses four lightweight, open-source components behind a Caddy reverse proxy:

| Component | Role | Image Size |
|-----------|------|------------|
| **Hugo** (via Nginx) | Static site generation for human-readable pages and RDF serializations | ~10 MB |
| **Oxigraph** | SPARQL 1.1 endpoint for machine queries | ~15 MB |
| **Trifid** | Content negotiation and linked data browsing | ~100 MB |
| **oai-pmh2** | OAI-PMH harvesting endpoint | ~50 MB |

## Request Flow

1. All requests arrive at **Caddy** (reverse proxy with automatic HTTPS)
2. Static documentation (`/docs/*`, `/specs/*`, `/guides/*`) is served directly from Hugo's pre-built files
3. Vocabulary and dataset URIs (`/vocab/*`, `/dataset/*`) are routed based on the `Accept` header:
   - `text/html` → Hugo's HTML pages
   - `text/turtle`, `application/ld+json`, `application/rdf+xml` → Trifid → Oxigraph
4. `/sparql` routes to Oxigraph's built-in SPARQL endpoint with YASGUI interface
5. `/oai` routes to the oai-pmh2 server

## Content Negotiation

The hub implements W3C-recommended content negotiation following the "Cool URIs for the Semantic Web" pattern. The same URI serves both humans and machines:

```
GET /vocab/cidoc-crm/E22_Human-Made_Object
Accept: text/html          → HTML documentation page
Accept: text/turtle        → Turtle RDF data
Accept: application/ld+json → JSON-LD data
```

## Data Pipeline

All data originates from Markdown + YAML source files in the Hugo content directory:

1. Hugo generates HTML pages and static RDF files (Turtle, JSON-LD, RDF/XML)
2. The same Turtle files are loaded into Oxigraph via SPARQL Graph Store Protocol
3. Dublin Core XML is extracted for OAI-PMH and loaded into SQLite
4. Everything is triggered by a single CI/CD pipeline on Git push
