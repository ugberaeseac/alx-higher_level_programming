#!/bin/bash
# displays the size of the body of the response using cURL
curl -sI "$1" | grep Content-Length | cut -b 17-18
