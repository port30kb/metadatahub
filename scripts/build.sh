#!/usr/bin/env bash
set -euo pipefail

# Build script for metadatahub.eu
# Runs Hugo build, loads data into Oxigraph, and updates OAI-PMH database.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
HUGO_DIR="$PROJECT_ROOT/hugo"
OAI_DATA_DIR="$PROJECT_ROOT/oai-pmh/data"

OXIGRAPH_URL="${OXIGRAPH_URL:-http://localhost:7878}"

echo "=== Building metadatahub.eu ==="

# Step 1: Generate data files from YAML
echo "[1/4] Generating data files..."
python3 "$SCRIPT_DIR/generate-geologic-timescale.py"
python3 "$SCRIPT_DIR/generate-example-data.py"
python3 "$SCRIPT_DIR/generate-nordic-techniques.py"
python3 "$SCRIPT_DIR/generate-nordic-institutions.py"
python3 "$SCRIPT_DIR/generate-nordic-places.py"
python3 "$SCRIPT_DIR/generate-nordic-art-movements.py"
python3 "$SCRIPT_DIR/generate-nordic-rights.py"
python3 "$SCRIPT_DIR/generate-nordic-iconography.py"
python3 "$SCRIPT_DIR/generate-nordic-mappings.py"

# Step 2: Build Hugo site
echo "[2/4] Building Hugo site..."
cd "$HUGO_DIR"
hugo --minify
echo "  Hugo build complete: $(find public -name '*.html' | wc -l) HTML files generated"

# Step 3: Load RDF data into Oxigraph
echo "[3/4] Loading RDF data into Oxigraph..."
TURTLE_FILES=$(find "$HUGO_DIR/public" -name "*.ttl" -type f 2>/dev/null || true)
if [ -n "$TURTLE_FILES" ]; then
    # Clear existing data
    curl -s -X POST "$OXIGRAPH_URL/update" \
        -H "Content-Type: application/sparql-update" \
        -d "CLEAR ALL" || echo "  Warning: Could not clear Oxigraph (may not be running)"

    # Load each Turtle file
    for ttl_file in $TURTLE_FILES; do
        echo "  Loading: $ttl_file"
        curl -s -X POST "$OXIGRAPH_URL/store" \
            -H "Content-Type: text/turtle" \
            --data-binary "@$ttl_file" || echo "  Warning: Failed to load $ttl_file"
    done
    echo "  Loaded $(echo "$TURTLE_FILES" | wc -l) Turtle files"
else
    echo "  No Turtle files found to load"
fi

# Step 4: Update OAI-PMH SQLite database
echo "[4/4] Updating OAI-PMH database..."
mkdir -p "$OAI_DATA_DIR"
"$SCRIPT_DIR/update-oai-db.sh"

echo "=== Build complete ==="
