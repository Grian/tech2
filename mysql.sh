#!/bin/sh
mysql -uroot mysql -e 'create database tech'
mysql -uroot mysql -e 'create user tech'
mysql -uroot mysql -e 'grant all on tech.* to tech'
mysql -uroot mysql -e 'alter database tech character set utf8'
cd ask
./manage.py syncdb
