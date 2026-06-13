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
# Read paths NUL-delimited so filenames with spaces/newlines are handled safely.
TURTLE_FILES=()
while IFS= read -r -d '' ttl_file; do
    TURTLE_FILES+=("$ttl_file")
done < <(find "$HUGO_DIR/public" -name "*.ttl" -type f -print0 2>/dev/null)

if [ "${#TURTLE_FILES[@]}" -gt 0 ]; then
    # Clear existing data (-f makes curl fail on HTTP errors so we can detect them)
    if ! curl -sf -X POST "$OXIGRAPH_URL/update" \
        -H "Content-Type: application/sparql-update" \
        -d "CLEAR ALL"; then
        echo "  Warning: Could not clear Oxigraph (may not be running)"
    fi

    # Load each Turtle file, counting only the ones that succeed.
    loaded=0
    for ttl_file in "${TURTLE_FILES[@]}"; do
        echo "  Loading: $ttl_file"
        if curl -sf -X POST "$OXIGRAPH_URL/store" \
            -H "Content-Type: text/turtle" \
            --data-binary "@$ttl_file"; then
            loaded=$((loaded + 1))
        else
            echo "  Warning: Failed to load $ttl_file"
        fi
    done
    echo "  Loaded $loaded of ${#TURTLE_FILES[@]} Turtle files"
else
    echo "  No Turtle files found to load"
fi

# Step 4: Update OAI-PMH SQLite database
echo "[4/4] Updating OAI-PMH database..."
mkdir -p "$OAI_DATA_DIR"
"$SCRIPT_DIR/update-oai-db.sh"

echo "=== Build complete ==="
