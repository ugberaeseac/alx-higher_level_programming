#!/bin/bash
# send request to URL and display all HTTP methods server will accept
curl -sI "$1" | grep Allow | cut -f2- -d " "
