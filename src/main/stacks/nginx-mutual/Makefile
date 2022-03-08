THIS_FILE := $(lastword $(MAKEFILE_LIST))

SHELL := /bin/bash

.PHONY: build

all: build

build:
	bash ./env-init.sh

start:
	docker-compose up -d

clean:
	docker-compose down
	rm -rf workspace

test.cURL:
	curl -v -k --key workspace/client.key --cert workspace/client.crt https://localhost
test.cURL.fail:
	curl -v -k https://localhost
