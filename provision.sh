#!/usr/bin/env bash

echo "Setting Timezone & Locale to $3 & en_US.UTF-8"

sudo ln -sf /usr/share/zoneinfo/$3 /etc/localtime
sudo apt-get install -qq language-pack-en
sudo locale-gen en_US
sudo update-locale LANG=en_US.UTF-8 LC_CTYPE=en_US.UTF-8

echo "Repair tty log message"
sudo sed -i "/tty/!s/mesg n/tty -s \\&\\& mesg n/" /root/.profile

# in order to avoid the message
# ==> default: dpkg-preconfigure: unable to re-open stdin: No such file or directory
# use "> /dev/null 2>&1 inorder to redirect stdout to /dev/null"
# for more info see http://stackoverflow.com/questions/10508843/what-is-dev-null-21

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
sudo apt-get install -y sqlite

echo ">>> Installing RabbitMQ"

apt-get -y install erlang-nox
echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -
apt-get update
apt-get install -y rabbitmq-server


echo ">>> Installing Node"
sudo apt-get install -y npm
curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
sudo apt-get install -y nodejs

echo ">>> Installing pip"
sudo apt-get install -y python3-pip
sudo apt-get install -y python-pip

echo "Installing virtualenv"
sudo pip install virtualenv

echo ">>> Installing Nginx"
sudo apt-get install -y nginx

echo ">>> Installing Git"
sudo apt-get -y install git

echo ">>> Installing Anaconda"
wget http://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh

echo ">>> Installing ZSH"
sudo apt-get -y install zsh
sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

echo ">>> Installing essentials for Python 3.5.2"
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz
sudo tar xzf Python-3.5.2.tgz
cd Python-3.5.2
sudo ./configure
sudo make altinstall

