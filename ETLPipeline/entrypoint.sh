#!/bin/bash

echo "Fui executado"

printenv >> /etc/environment

# python3 /app/etl.py
cron -f