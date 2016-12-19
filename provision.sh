#!/usr/bin/env bash

apt-get update
echo ">>> Installing Apache"
apt-get install -y apache2

if ! [ -L /var/www ]; then
  rm -rf /var/www
  ln -fs /vagrant /var/www
fi

echo ">>> Installing SQLite Server"

# Install SQLite Server
# -qq implies -y --force-yes
sudo apt-get install -qq sqlite

echo ">>> Installing RabbitMQ"

apt-get -y install erlang-nox
wget http://www.rabbitmq.com/rabbitmq-signing-key-public.asc
apt-key add rabbitmq-signing-key-public.asc
echo "deb http://www.rabbitmq.com/debian/ testing main" > /etc/apt/sources.list.d/rabbitmq.list
apt-get update
apt-get install -y rabbitmq-server

rabbitmqctl add_user $1 $2
rabbitmqctl set_permissions -p / $1 ".*" ".*" ".*"

echo ">>> Installing Node"
sudo apt-get update
sudo apt-get install npm
curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
sudo apt-get install -y nodejs

echo ">>> Installing pip"
sudo apt-get install python3-pip

echo ">>> Installing Nginx"
sudo apt-get update
sudo apt-get install nginx

