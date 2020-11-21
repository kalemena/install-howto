FROM kalemena/node-red:latest

USER root

ADD [ "*.yaml", "*.json", "/apis/" ]

# Tock API
RUN cd /apis \
    && api-spec-converter -f openapi_3 -t swagger_2 /apis/Swagger_TOCKWebConnector.yaml > tock-api.json \
    && node-red-nodegen tock-api.json --category samples \
    && cd node-red-contrib-tock-web-bot-connector-api \
    && npm link \
    && cd /opt/node-red \
    && npm link node-red-contrib-tock-web-bot-connector-api \
    && chown -R nodered:nodered /opt/node-red/node_modules/node-red-contrib-tock-web-bot-connector-api

USER nodered
