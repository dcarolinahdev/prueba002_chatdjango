# chat django 3.1

_Curso platzi de django 3.1 usando python 3.8.5 sobre ubuntu 20.04_

## Database Settings

```
sudo -u postgres psql
CREATE DATABASE dbchatttest;
CREATE USER chatadmin WITH PASSWORD 'chatpasswd';
GRANT ALL PRIVILEGES ON DATABASE dbchatttest TO chatadmin;
\q

python manage.py createsuperuser
Username: adminchat
Email address: adminchat@example.com
Password: testchat
```

#### Users for test

```
User: crivera
Password: cr123456
Carmen Rivera
crivera@example.com

User: lmendez
Password: lm123456
Liliana Mendez
lmendez@example.com
```

By [dcarolinahdev](https://github.com/dcarolinahdev)