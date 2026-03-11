# Oxigraph Configuration

Oxigraph runs as a Docker container with data persisted in a named volume.

## Loading Data

Data is loaded via the SPARQL Graph Store Protocol:

```bash
# Load a single Turtle file
curl -X POST http://localhost:7878/store \
  -H "Content-Type: text/turtle" \
  --data-binary @file.ttl

# Clear all data
curl -X POST http://localhost:7878/update \
  -H "Content-Type: application/sparql-update" \
  -d "CLEAR ALL"

# Query
curl http://localhost:7878/query \
  -H "Accept: application/sparql-results+json" \
  --data-urlencode "query=SELECT * WHERE { ?s ?p ?o } LIMIT 10"
```

## YASGUI Interface

Oxigraph includes a built-in YASGUI SPARQL query editor at `http://localhost:7878/`.
