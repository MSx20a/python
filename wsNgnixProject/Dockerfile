FROM ubuntu:22.04


RUN apt-get update && \
    apt-get install gnupg curl && \
    apt-key adv --keyserver hpk://keyserver.ubuntu:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4 && \
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -sc)/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list && \
    apt-get update && \
    apt-get install -y nginx mongodb-org && \
    apt-get clean

# 配置Nginx
# 複製nginx.conf文件到/etc/nginx/conf.d目錄底下，並將它命名為default.conf，docker運行時將以此作爲配置文件
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
# COPY nginx.conf /etc/nginx/conf.d/default.conf

#配置MongoDB
RUN mkdir -p /data/db

#配置對外阜號Nginx:80，mongodb:27017
EXPOSE 80 27017

#指定啟動容器時執行的命令
CMD service nginx start && mongod --fork --logpath /var/log/mongodb.log && tail -f /dev/null

#service nginx start，用於在Linux中啟動Nginx
#讓MongoDB --fork在後台運行；--logpath日誌文件路徑
#MongoDB服務紀錄文件路徑：/var/log/mongodb.log
#--config /etc/mongod.conf指定使用mongod.conf作為MongoDB的配置文件
#在Linux上MongoDB的文件配置通常位於/etc目錄下的mongod.conf中
