<?php

/**
 * OAI-PMH endpoint for metadatahub.eu
 *
 * This file bootstraps the oai-pmh2 server with our configuration.
 * Records are loaded from a SQLite database populated by the CI/CD pipeline.
 */

require_once __DIR__ . '/vendor/autoload.php';

$config = require __DIR__ . '/config.php';

// Initialize the OAI-PMH server
// The oai-pmh2 library handles all OAI-PMH verbs:
// Identify, ListMetadataFormats, ListSets, ListIdentifiers,
// ListRecords, and GetRecord
try {
    $server = new \OCC\OaiPmh2\Server($config);
    $server->run();
} catch (\Exception $e) {
    http_response_code(500);
    header('Content-Type: text/xml; charset=utf-8');
    echo '<?xml version="1.0" encoding="UTF-8"?>';
    echo '<error>' . htmlspecialchars($e->getMessage()) . '</error>';
}
