FROM beyondray/kbengine-mysql
MAINTAINER beyondray <yangzhilei01@corp.netease.com>

ENV USERNAME=beyondray
ENV MYSQL_ALLOW_EMPTY_PASSWORD yes
WORKDIR /kbengine/assets

COPY  ./schema.sql .
COPY  ./config.sh .
COPY  ./res ./res
COPY  ./scripts ./scripts

EXPOSE 20013
EXPOSE 20015

ENTRYPOINT ["sh", "./config.sh"]
CMD ["/bin/bash"] 
