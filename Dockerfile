FROM python:3.9-bookworm

USER root
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get update && apt-get dist-upgrade -y
RUN apt-get install -yq --no-install-recommends chromium
WORKDIR /opt
RUN python3 -m venv venv && /bin/bash -c "source /opt/venv/bin/activate"
RUN pip3 install selenium
COPY screenshot.py /opt/screenshot.py

RUN groupadd -r nonroot && \
  useradd -m -r -g nonroot -d /home/nonroot -s /usr/sbin/nologin -c "Nonroot User" nonroot && \
  chown -R nonroot:nonroot /home/nonroot && \
  usermod -a -G sudo nonroot && echo 'nonroot:nonroot' | chpasswd

USER nonroot 
ENTRYPOINT [ "python3", "/opt/screenshot.py" ]
