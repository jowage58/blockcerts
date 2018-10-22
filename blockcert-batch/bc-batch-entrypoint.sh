#!/bin/bash
set -e

echo "downloading S3 batch directory"
echo "aws s3 cp --recursive s3://fs.blockcerts.poc/batch/20181024/ /var/blockcerts/"

echo "running cert-issuer on the following unsigned certs"
ls -l /var/blockcerts/unsigned_certificates

cert-issuer -c /var/blockcerts/config/conf.ini

echo "uploading signed blockcerts to S3"
ls -l /var/blockcerts/blockchain_certificates
echo "aws s3 cp --recursive /var/blockcerts/blockchain_certificates s3://fs.blockcerts.poc/certs/"
