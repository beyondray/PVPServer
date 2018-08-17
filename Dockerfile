FROM beyondray/kbengine-mysql
MAINTAINER beyondray <yangzhilei01@corp.netease.com>

ENV USERNAME=beyondray
ENV MYSQL_ALLOW_EMPTY_PASSWORD yes
WORKDIR /kbengine/assets

COPY  ./schema.sql .
COPY  ./res ./res
COPY  ./scripts ./scripts

RUN service mysql start && \
mysql < ./schema.sql && \
echo service mysql status 

ENTRYPOINT ["sh", "./start_server.sh"] 
CMD [""] 
