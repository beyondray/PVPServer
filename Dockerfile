FROM beyondray/kbengine-mysql
MAINTAINER beyondray <yangzhilei01@corp.netease.com>

ENV USERNAME=beyondray
ENV MYSQL_ALLOW_EMPTY_PASSWORD yes
WORKDIR ~/kbengine-1.1.0/assets/

COPY  ./schema.sql .
COPY  ./res .
COPY  ./scripts .

RUN service mysql start && \
mysql < ./schema.sql && \
echo service mysql status

CMD ["sh", "./start_server.sh"]

