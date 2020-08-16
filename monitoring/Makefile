
init:
	docker-compose pull
	# prepare influxDB
	mkdir -p var/lib/influxdb
	mkdir -p etc/influxdb
	docker run --rm influxdb influxd config | tee etc/influxdb/influxdb.conf > /dev/null

start: 
	docker-compose up -d

stop:
	docker-compose stop

down:
	docker-compose down

clean:
	docker-compose down --volumes