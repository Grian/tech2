#!/bin/bash
mkdir -p etc public/{img,css,js} uploads/
mkdir -p logs
mkdir -p apps
chmod 0755 logs
touch etc/nginx.conf
touch  init.sh
chmod 0755 init.sh
sudo /etc/init.d/mysql start

NAME=webtech.conf
echo '#!/bin/bash' >> init.sh
echo "NAME=$NAME" >> init.sh
echo 'sudo ln -fs $PWD/etc/nginx.conf /etc/nginx/sites-enabled/$NAME' >> init.sh
#echo 'sudo rm /etc/nginx/sites-enabled/default' >> init.sh
echo 'sudo /etc/init.d/nginx restart' >> init.sh
echo 'sudo ln -fs $PWD/etc/gu-hello.py /etc/gunicorn.d/gu-hello.py' >> init.sh
echo 'sudo ln -fs $PWD/etc/gu-ask.py /etc/gunicorn.d/gu-ask.py' >> init.sh
echo 'sudo /etc/init.d/gunicorn restart' >> init.sh
