#!/bin/bash
set -e

echo "$(date): Running entrypoint script"

echo "Arg 1==[${1}]"
echo "Arg 2==[${2}]"
echo "Arg 3==[${3}]"

echo "downloading S3 batch directory"
echo "aws s3 cp --recursive ${BC_BATCHDIR_S3URL} /var/blockcerts/"

echo "running cert-issuer on the following unsigned certs"
ls -l /var/blockcerts/unsigned_certificates

#cert-issuer -c /var/blockcerts/config/conf.ini

echo "uploading signed blockcerts to S3"
# ls -l /var/blockcerts/blockchain_certificates
echo "aws s3 cp --recursive /var/blockcerts/blockchain_certificates ${BC_CERTDIR_S3URL}"

echo "$(date): done"
