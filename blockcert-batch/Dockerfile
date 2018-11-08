FROM python:3.6.6-alpine3.8

WORKDIR /var/blockcerts

COPY bc-batch-entrypoint.sh ./bc-batch-entrypoint.sh

# Following 2 copy commands are just for testing, the config
# and unsigned certs would normally be downloaded from S3.
COPY config/ ./config/
COPY unsigned_certificates/ ./unsigned_certificates/

RUN apk add --update \
        bash \
        ca-certificates \
        gcc \
        gmp-dev \
        libffi-dev \
        libressl-dev \
        linux-headers \
        make \
        musl-dev \
        python3-dev \
        tar \
    && pip3 install --upgrade pip setuptools \
    && pip3 install awscli \
    && pip3 install cert-issuer \
    && rm -rf /var/cache/apk/* \
    && rm -rf /root/.cache \
    && chown -R nobody:nobody /var/blockcerts \
    && chmod 755 /var/blockcerts/bc-batch-entrypoint.sh

USER nobody

ENTRYPOINT ["/var/blockcerts/bc-batch-entrypoint.sh"]
