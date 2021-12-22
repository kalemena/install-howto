
##########################
# Initialize Environment
##########################

init: init-images init-influxdb2 init-telegraf init-grafana

init-images:
	echo "Initialize: Pull Images ..."
	docker-compose pull

init-influxdb2:
	echo "Initialize: Setup InfluxDB ..."
	# For information only
	mkdir -p etc/influxdb2
	docker run --rm influxdb:2.0.7 influxd print-config > etc/influxdb2/config-default.yml
	cp -n etc/influxdb2/config-default.yml etc/influxdb2/config.yml
	# Volumes
	#docker-compose up -d influxdb2
	#sleep 10s
	#docker-compose influxdb2 down

init-telegraf:
	echo "Initialize: Setup Telegraf ..."
	# For information only
	mkdir -p etc/telegraf
	docker run --rm telegraf telegraf config | tee etc/telegraf/telegraf-default.conf > /dev/null
	cp -n etc/telegraf/telegraf-default.conf etc/telegraf/telegraf.conf

init-grafana:
	echo "Initialize: Setup Grafana ..."
	# mkdir -p var/lib/grafana
	# mkdir -p var/log/grafana

##########################
# Test Environment
##########################

test.influxdb:
	docker-compose exec influxdb influx

##########################
# Manage Environment
##########################

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