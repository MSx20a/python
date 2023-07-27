FROM centos

#4-6行是為了解決CentOS 8在2021/12/31已被官方停止更新而無法獲得新的開發資源，所以要先將CentOS更新
RUN cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y nginx mongodb-server
RUN yum clean all

#配置Nginx
#複製nginx.conf文件到/etc/nginx/conf.d目錄底下，並將它命名為default.conf，docker運行時將以此作爲配置文件
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

#啟動MongoDB服務
RUN systemctl enable mongod

#配置對外阜號Nginx:80，mongodb:27017
EXPOSE 80 27017

#指定啟動容器時執行的命令
CMD service nginx start && /usr/bin/mongod --fork --logpath /var/log/mongodb.log --config /etc/mongod.conf

#service nginx start，用於在Linux中啟動Nginx
#MongoDB在Linux上的安裝路徑：/usr/bin/mongod
#--fork在後台運行；--logpath日誌文件路徑
#MongoDB服務紀錄文件路徑：/var/log/mongodb.log
#--config /etc/mongod.conf指定使用mongod.conf作為MongoDB的配置文件
#在Linux上MongoDB的文件配置通常位於/etc目錄下的mongod.conf中
