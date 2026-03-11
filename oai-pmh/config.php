<?php

return [
    'repositoryName' => 'metadatahub.eu — Cultural Heritage Metadata Hub',
    'baseURL' => 'https://metadatahub.eu/oai',
    'adminEmail' => 'admin@metadatahub.eu',
    'database' => '/var/www/data/oai.sqlite',
    'metadataPrefix' => [
        'oai_dc' => [
            'schema' => 'http://www.openarchives.org/OAI/2.0/oai_dc.xsd',
            'namespace' => 'http://www.openarchives.org/OAI/2.0/oai_dc/',
        ],
        'lido' => [
            'schema' => 'http://www.lido-schema.org/schema/v1.1/lido-v1.1.xsd',
            'namespace' => 'http://www.lido-schema.org',
        ],
    ],
];
