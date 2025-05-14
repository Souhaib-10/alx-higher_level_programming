#!/bin/bash
# Bash script take an URL, sends a request and dispaly size of the body
curl -s "$1" | wc -c
