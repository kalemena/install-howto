
init:
	mkdir -p data/influxdb

start: init
	docker-compose up -d

stop:
	docker-compose stop

down:
	docker-compose down

clean:
	docker-compose down --volumes