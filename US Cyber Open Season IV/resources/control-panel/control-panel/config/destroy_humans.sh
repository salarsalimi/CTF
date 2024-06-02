#!/bin/sh

check_status() {
    curl -s localhost:3000/status
}

destroy_humans() {
    curl -s localhost:3000/destroy
}

if [ "$#" -gt 0 ]; then
    $*
else
    echo -e "Destroy Humans option selected. Please choose 'check_status' or 'destroy_humans'."
fi