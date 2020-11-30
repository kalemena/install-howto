
build:
	cd images && docker-compose build

rasa-cli:
	docker run -it --user 1000:1000 --rm -v $(PWD)/projects:/opt rasa-cli bash
