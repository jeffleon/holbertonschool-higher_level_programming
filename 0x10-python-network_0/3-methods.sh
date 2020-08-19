#!/bin/bash
# Display the options accept
curl -siX OPTIONS $1 | grep "Allow:" | cut -d " " -f 2-
