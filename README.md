## EASY Gitlab Full Backup
Clone your private gitlab projects, before its too late!


## HOW TO USE
install python-gitlab
~~~
pip install --upgrade python-gitlab
~~~
add your access token to [config.cfg](config.cfg)
~~~

[global]
default = gitlab
ssl_verify = true
timeout = 5

[gitlab]
url = https://gitlab.com/
private_token = YOUR_ACCESS_TOKEN
api_version = 4
~~~
run full backup
~~~
python back.py
~~~
