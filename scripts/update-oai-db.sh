#!/usr/bin/env bash
set -euo pipefail

# Update the OAI-PMH SQLite database from Hugo content files.
# Extracts Dublin Core metadata from front matter and creates OAI-PMH records.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
OAI_DB="$PROJECT_ROOT/oai-pmh/data/oai.sqlite"
CONTENT_DIR="$PROJECT_ROOT/hugo/content"

# Escape a value for safe inclusion in XML text content (& must come first).
xml_escape() {
    local s=$1
    s=${s//&/&amp;}
    s=${s//</&lt;}
    s=${s//>/&gt;}
    printf '%s' "$s"
}

echo "  Initializing OAI-PMH database: $OAI_DB"

# Create/reset the database
sqlite3 "$OAI_DB" <<'SQL'
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    identifier TEXT UNIQUE NOT NULL,
    datestamp TEXT NOT NULL,
    setSpec TEXT,
    metadata TEXT NOT NULL,
    deleted INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS sets (
    setSpec TEXT PRIMARY KEY,
    setName TEXT NOT NULL
);

-- Insert default sets
INSERT OR REPLACE INTO sets (setSpec, setName) VALUES ('vocab', 'Vocabularies');
INSERT OR REPLACE INTO sets (setSpec, setName) VALUES ('dataset', 'Datasets');

-- Clear existing records for rebuild
DELETE FROM records;
SQL

# Process vocabulary content files
for md_file in "$CONTENT_DIR"/vocab/*.md; do
    [ -f "$md_file" ] || continue
    filename=$(basename "$md_file" .md)
    [ "$filename" = "_index" ] && continue

    # Extract front matter fields using simple grep/sed
    title=$(grep -m1 '^title:' "$md_file" | sed 's/^title: *"\?\(.*\)"\?$/\1/' | sed 's/"$//')
    description=$(grep -m1 '^description:' "$md_file" | sed 's/^description: *"\?\(.*\)"\?$/\1/' | sed 's/"$//')
    date=$(grep -m1 '^date:' "$md_file" | sed 's/^date: *//')
    creator=$(grep -m1 '^creator:' "$md_file" | sed 's/^creator: *"\?\(.*\)"\?$/\1/' | sed 's/"$//')

    # Escape XML special characters so the metadata stays well-formed.
    title=$(xml_escape "$title")
    description=$(xml_escape "$description")
    creator=$(xml_escape "$creator")

    identifier="oai:metadatahub.eu:vocab/$filename"
    datestamp="${date:-$(date -I)}"

    # Build Dublin Core XML
    dc_xml="<oai_dc:dc xmlns:oai_dc=\"http://www.openarchives.org/OAI/2.0/oai_dc/\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\">"
    dc_xml="$dc_xml<dc:title>$title</dc:title>"
    dc_xml="$dc_xml<dc:description>$description</dc:description>"
    [ -n "${creator:-}" ] && dc_xml="$dc_xml<dc:creator>$creator</dc:creator>"
    dc_xml="$dc_xml<dc:date>$datestamp</dc:date>"
    dc_xml="$dc_xml<dc:identifier>https://metadatahub.eu/vocab/$filename</dc:identifier>"
    dc_xml="$dc_xml<dc:type>Vocabulary</dc:type>"
    dc_xml="$dc_xml</oai_dc:dc>"

    sqlite3 "$OAI_DB" "INSERT INTO records (identifier, datestamp, setSpec, metadata) VALUES ('$identifier', '$datestamp', 'vocab', '$(echo "$dc_xml" | sed "s/'/''/g")');"
    echo "  Added: $identifier"
done

# Process dataset content files
for md_file in "$CONTENT_DIR"/dataset/*.md; do
    [ -f "$md_file" ] || continue
    filename=$(basename "$md_file" .md)
    [ "$filename" = "_index" ] && continue

    title=$(grep -m1 '^title:' "$md_file" | sed 's/^title: *"\?\(.*\)"\?$/\1/' | sed 's/"$//')
    description=$(grep -m1 '^description:' "$md_file" | sed 's/^description: *"\?\(.*\)"\?$/\1/' | sed 's/"$//')
    date=$(grep -m1 '^date:' "$md_file" | sed 's/^date: *//')
    publisher=$(grep -m1 '^publisher:' "$md_file" | sed 's/^publisher: *"\?\(.*\)"\?$/\1/' | sed 's/"$//')

    # Escape XML special characters so the metadata stays well-formed.
    title=$(xml_escape "$title")
    description=$(xml_escape "$description")
    publisher=$(xml_escape "$publisher")

    identifier="oai:metadatahub.eu:dataset/$filename"
    datestamp="${date:-$(date -I)}"

    dc_xml="<oai_dc:dc xmlns:oai_dc=\"http://www.openarchives.org/OAI/2.0/oai_dc/\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\">"
    dc_xml="$dc_xml<dc:title>$title</dc:title>"
    dc_xml="$dc_xml<dc:description>$description</dc:description>"
    [ -n "${publisher:-}" ] && dc_xml="$dc_xml<dc:publisher>$publisher</dc:publisher>"
    dc_xml="$dc_xml<dc:date>$datestamp</dc:date>"
    dc_xml="$dc_xml<dc:identifier>https://metadatahub.eu/dataset/$filename</dc:identifier>"
    dc_xml="$dc_xml<dc:type>Dataset</dc:type>"
    dc_xml="$dc_xml</oai_dc:dc>"

    sqlite3 "$OAI_DB" "INSERT INTO records (identifier, datestamp, setSpec, metadata) VALUES ('$identifier', '$datestamp', 'dataset', '$(echo "$dc_xml" | sed "s/'/''/g")');"
    echo "  Added: $identifier"
done

echo "  OAI-PMH database updated: $(sqlite3 "$OAI_DB" 'SELECT COUNT(*) FROM records;') records"
