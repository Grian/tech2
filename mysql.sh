#!/bin/sh
mysql -uroot mysql -e 'create database tech'
mysql -uroot mysql -e 'create user tech'
mysql -uroot mysql -e 'grant all on tech.* to tech'
