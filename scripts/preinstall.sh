apt-get install \
    wget curl git htop vim-nox avahi-daemon tmux \
    build-essential llvm \
    postgresql libpq-dev \
    redis-server nginx supervisor \
    libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libncurses5-dev \
    libpng-dev libjpeg-dev libtiff-dev libwebp-dev libfreetype6-dev \
    libxml2-dev libxslt1-dev \
    libevent-dev
cat >>~/.bash_profile <<EOD
export PATH="\$HOME/.pyenv/bin:\$PATH"
eval "\$(pyenv init -)"
eval "\$(pyenv virtualenv-init -)"
EOD
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
source ~/.bash_profile
