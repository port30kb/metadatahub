FROM php:8.3-apache

RUN apt-get update && apt-get install -y \
    libsqlite3-dev \
    && docker-php-ext-install pdo_sqlite \
    && rm -rf /var/lib/apt/lists/*

# Install oai-pmh2 via Composer
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/html
COPY composer.json .
RUN composer install --no-dev --optimize-autoloader || true

COPY index.php .
COPY config.php .

RUN chown -R www-data:www-data /var/www/html
RUN a2enmod rewrite

EXPOSE 80
