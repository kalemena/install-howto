FROM maven:3.6.3-adoptopenjdk-14

COPY [ ".", "/opt/service/" ]

WORKDIR /opt/service/

RUN mvn clean install dependency:copy-dependencies

CMD java -cp ./target/tock-kotlin-websocket-0.0.1-SNAPSHOT.jar:./target/dependency/* StartWebsocketWithLocalhostKt