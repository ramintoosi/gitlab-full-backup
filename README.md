## EASY Gitlab Full Backup
Clone your private gitlab projects, before its too late!


## HOW TO USE
install python-gitlab
~~~
pip install --upgrade python-gitlab
~~~
add your [access token](https://gitlab.com/profile/personal_access_tokens) to [config.cfg](config.cfg)
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

NOTE: I assume that you are clonning with your ssh key otherwise please edit [back.py](backup.py) based on your preferred way.
~~~
python back.py
~~~
