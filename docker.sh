#!/bin/bash
docker run --add-host=host.docker.internal:host-gateway -p 10337:10337 inferable/l1m:latest
