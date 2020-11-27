FROM kalemena/node-red:latest

RUN npm i   node-red-contrib-telegrambot;

USER root

ADD [ "*.yaml", "*.json", "/apis/" ]

# Tock Bot API
RUN cd /apis \
    && api-spec-converter -f openapi_3 -t swagger_2 /apis/Swagger_TOCKWebConnector.yaml > tock-api-bot.json \
    && node-red-nodegen tock-api-bot.json --category samples \
    && cd node-red-contrib-tock-web-bot-connector-api \
    && npm link \
    && cd /opt/node-red \
    && npm link node-red-contrib-tock-web-bot-connector-api \
    && chown -R nodered:nodered /opt/node-red/node_modules/node-red-contrib-tock-web-bot-connector-api

# Tock NLP API
RUN cd /apis \
    && api-spec-converter -f openapi_3 -t swagger_2 /apis/nlp.yaml > tock-api-nlp.json \
    && node-red-nodegen tock-api-nlp.json --category samples \
    && cd node-red-contrib-tock-nlp-api \
    && npm link \
    && cd /opt/node-red \
    && npm link node-red-contrib-tock-nlp-api \
    && chown -R nodered:nodered /opt/node-red/node_modules/node-red-contrib-tock-nlp-api

# Tock Admin API
RUN cd /apis \
    && api-spec-converter -f openapi_3 -t swagger_2 /apis/admin.yaml > tock-api-admin.json \
    && node-red-nodegen tock-api-admin.json --category samples \
    && cd node-red-contrib-tock-nlp-admin-api \
    && npm link \
    && cd /opt/node-red \
    && npm link node-red-contrib-tock-nlp-admin-api \
    && chown -R nodered:nodered /opt/node-red/node_modules/node-red-contrib-tock-nlp-admin-api

USER nodered
