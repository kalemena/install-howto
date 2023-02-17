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

build:
	docker-compose build

start: 
	docker-compose up -d

logs:
	docker-compose logs -f

stop:
	docker-compose stop

down:
	docker-compose down

clean:
	docker-compose down --volumes