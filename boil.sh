#!/bin/bash
mkdir -p etc public/{img,css,js} uploads/
mkdir -p logs
mkdir -p apps
chmod 0755 logs
touch etc/nginx.conf
touch etc/gunicorn.conf
touch  init.sh
chmod 0755 init.sh

NAME=webtech.conf
echo '#!/bin/bash' >> init.sh
echo "NAME=$NAME" >> init.sh
echo 'sudo ln -fs $PWD/etc/nginx.conf /etc/nginx/sites-enabled/$NAME' >> init.sh
echo 'sudo /etc/init.d/nginx restart' >> init.sh
echo 'sudo ln -fs $PWD/etc/gu-hello.py /etc/gunicorn.d/gu-hello.py' >> init.sh
echo 'sudo /etc/init.d/gunicorn restart' >> init.sh
