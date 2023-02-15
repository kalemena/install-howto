##########################
# Initialize Environment
##########################

init: init-env init-images

init-env:
	echo "Initialize: Folders ..."
	cp .env-example src/.env

init-images:
	echo "Initialize: Pull Images ..."
	docker-compose pull
