#!/bin/bash
docker rm -f control-panel
docker build --tag=web_control_panel .
docker run -p 9999:9999 --name=control-panel web_control_panel