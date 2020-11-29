FROM python:3.8

# https://rasa.com/docs/rasa/installation/

WORKDIR /opt

RUN pip3 install rasa \
    && rasa telemetry disable

# https://rasa.com/docs/rasa/playground/
# https://rasa.com/docs/rasa/command-line-interface
# https://rasa.com/docs/rasa/custom-actions

# CMD rasa init
CMD /bin/bash