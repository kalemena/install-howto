
init:
	docker-compose pull

	# prepare influxDB
	mkdir -p var/lib/influxdb
	mkdir -p etc/influxdb
	docker run --rm influxdb influxd config | tee etc/influxdb/influxdb.conf > /dev/null
	touch var/lib/.influx_history

	docker run -it --rm \
		--user 1000:1000 \
		-e INFLUXDB_HTTP_AUTH_ENABLED=true \
        -e INFLUXDB_ADMIN_USER=default \
        -e INFLUXDB_ADMIN_PASSWORD=password \
        -v $(CURDIR)/var/lib/influxdb:/var/lib/influxdb \
        -v $(CURDIR)/etc/influxdb/scripts:/docker-entrypoint-initdb.d \
        influxdb /init-influxdb.sh

start: 
	docker-compose up -d

stop:
	docker-compose stop

down:
	docker-compose down

clean:
	docker-compose down --volumes