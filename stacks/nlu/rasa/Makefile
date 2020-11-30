# OPTS = --user 1000:1000

build:
	cd images && docker-compose build

rasa-cli:
	docker run -it $(OPTS) -p 5005:5005 --rm -v $(PWD)/projects:/opt rasa-cli bash
