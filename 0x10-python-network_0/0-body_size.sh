#!/bin/bash
# sends a request to URL
# displays the size of the body of the response
# Must use cURL

curl -sI "$1" | grep Content-Length | cut -b 17-18
