FROM rasa/rasa-sdk:latest 

# USER developer as 1000
RUN mkdir -p /home/developer && \
    echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:1000:" >> /etc/group && \
    chown developer:developer -R /home/developer && \
    chown developer:developer -R /opt

USER developer
ENV HOME /home/developer
WORKDIR /home/developer

COPY ./requirements-actions.txt /home/developer/ 
COPY ./ /home/developer/actions

RUN pip install -r requirements-actions.txt 
