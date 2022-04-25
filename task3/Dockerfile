FROM ubuntu:latest

#VARS
ENV APACHE_RUN_USER=www-data
ENV APACHE_RUN_GROUP=www-data
ENV SITES_DIR=/var/www/www-data/
ENV SITES_AVAILABLE_DIR=/etc/apache2/sites-available/
ENV SITES_ENABLED_DIR=/etc/apache2/sites-enabled/

# apache2 port in container
EXPOSE 8080

#install apache2
RUN apt update && apt install -y apache2

# remove default sites directory and create our directory
RUN rm -rf /var/www/*
RUN mkdir -p ${SITES_DIR}site1
COPY ./site1 ${SITES_DIR}site1
RUN chown -R www-data.www-data $SITES_DIR

# remove default virtualhosts config files
# and copy our file
WORKDIR $SITES_AVAILABLE_DIR
RUN rm *.conf
COPY ./configs/vhost_site1.conf $SITES_AVAILABLE_DIR

#create new links enable -> available
WORKDIR $SITES_ENABLED_DIR
RUN rm *.conf
RUN ln -s ${SITES_AVAILABLE_DIR}vhost_site1.conf ./vhost_site1.conf

#change listening port
RUN sed -i 's/Listen 80/Listen 8080/g' /etc/apache2/ports.conf

#start apache2
CMD apache2ctl -D FOREGROUND

#build and start
#docker build -t makandrey/task3
#docker run -dit --name my-apache2 -p 8080:8080 makandrey/task3
#test:
#localhost:8080
#127.0.0.1:8080
#site1.local:8080 (config DNS server or add to /etc/hosts)
#www.site1.local:8080 (config DNS server or add to /etc/hosts)