#!/bin/bash
set -e

# Copy your cron schedule
crontab /app/cronjob

# Start cron
service cron start

# Print logs to container output
tail -f /var/log/cron.log
