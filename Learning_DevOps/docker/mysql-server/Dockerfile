FROM ubuntu:latest

ADD ./mysql-setup.sh /tmp/mysql-setup.sh
RUN /bin/sh /tmp/mysql-setup.sh

EXPOSE 3306
CMD ["/usr/sbin/mysqld"]


