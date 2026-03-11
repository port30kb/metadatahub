---
title: "Example Museum Collection"
description: "A sample DCAT-AP dataset entry describing a museum's digitized collection metadata, published via the Helix CMS."
date: 2024-09-01
type: dataset
publisher: "Example Museum"
license: "https://creativecommons.org/publicdomain/zero/1.0/"
theme: "http://publications.europa.eu/resource/authority/data-theme/EDUC"
spatial: "http://sws.geonames.org/2661886/"
accrualPeriodicity: "http://publications.europa.eu/resource/authority/frequency/MONTHLY"
standards:
  - DCAT-AP
tags:
  - museum
  - collection
  - DCAT-AP
  - open-data
distributions:
  - id: "turtle"
    title: "RDF Turtle dump"
    accessURL: "https://metadatahub.eu/dataset/example-museum-collection/index.ttl"
    downloadURL: "https://metadatahub.eu/dataset/example-museum-collection/index.ttl"
    mediaType: "text/turtle"
  - id: "jsonld"
    title: "JSON-LD dump"
    accessURL: "https://metadatahub.eu/dataset/example-museum-collection/index.jsonld"
    downloadURL: "https://metadatahub.eu/dataset/example-museum-collection/index.jsonld"
    mediaType: "application/ld+json"
---

## Overview

This is a sample dataset catalog entry demonstrating how Helix-published museum collections are described using the DCAT-AP vocabulary. The dataset contains digitized object metadata from the Example Museum.

## Access

- **SPARQL**: Query this dataset via the [SPARQL endpoint](/sparql)
- **OAI-PMH**: Harvest records via the [OAI-PMH endpoint](/oai?verb=ListRecords&metadataPrefix=oai_dc)
- **Download**: Available as [Turtle](index.ttl) and [JSON-LD](index.jsonld)

## DCAT-AP Compliance

This entry conforms to DCAT-AP 3.0 and can be validated using the [EU DCAT-AP SHACL Validator](https://www.itb.ec.europa.eu/shacl/dcat-ap/upload).
