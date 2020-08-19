#!/bin/bash
# code status
curl -sI $1 | grep 'HTTP/1.0' | cut -d ' ' -f 2 
