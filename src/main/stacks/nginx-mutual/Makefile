THIS_FILE := $(lastword $(MAKEFILE_LIST))

SHELL := /bin/bash

.PHONY: init

all: init

init:
	bash ./env-init.sh

start:
	docker-compose up -d nginx

clean:
	docker-compose down
	rm -rf workspace

test.cURL:
	curl -v -k --key workspace/client.key --cert workspace/client.crt -H "Host: hello.service.local" https://localhost
test.cURL.fail:
	curl -v -k -H "Host: hello.service.local" https://localhost

test.python:
	docker-compose up client-python