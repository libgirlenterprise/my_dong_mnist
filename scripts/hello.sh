#!/bin/bash
curl -X POST \
     http://$1/api/v1/hello \
     -H 'Content-Type: application/json' \
     -d '""'
