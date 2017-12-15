# Monitoring docker stack

This is an aggregate of many resources out there to run some monitoring stack.

## Simple telegraf + grafana + influxdb

`docker-compose` includes `telegraf`, `grafana` and `influxdb`.

### Usage

* Start the stack

```bash
$ docker-compose up -d
...
$ docker exec -it monitoring_influxdb_1 bash
root@bb69221ac8fe:/# influx
Visit https://enterprise.influxdata.com to register for updates, InfluxDB server management, and monitoring.
Connected to http://localhost:8086 version 0.9.6.1
InfluxDB shell 0.9.6.1
> create database telegraf;
...
> create database SensorData;
...
> show databases;
name: databases
---------------
name
SensorData
telegraf
_internal

> 
```

* Open your brower to: __http://localhost:3000/__
* Use the username/password: __kalemena/kalemena__
* Select the __System__ dashboard

## resources

* [InfluxDB doc](https://docs.influxdata.com/influxdb/v1.2/introduction/getting_started/) 

*