#!/bin/sh

# Some things are commented out below because they're handy to have
# but not essential for the chatr project.  In particular, if you
# are using this project, you probably already have git installed. ;)

apt-get install \
    wget curl \
    build-essential llvm \
    postgresql libpq-dev \
    redis-server nginx-full supervisor \
    libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libncurses5-dev \
    libpng-dev libjpeg-dev libtiff-dev libwebp-dev libfreetype6-dev \
    libxml2-dev libxslt1-dev \
    libevent-dev

# apt-get install \
#    git htop vim-nox avahi-daemon tmux module-assistant

cat >>~/.bash_profile <<EOD
export PATH="\$HOME/.pyenv/bin:\$PATH"
eval "\$(pyenv init -)"
eval "\$(pyenv virtualenv-init -)"
EOD
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
source ~/.bash_profile
