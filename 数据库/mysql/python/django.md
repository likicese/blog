# django

``` bash
django-admin startproject mysite  # 创建工程
python manage.py startapp polls  # 创建app

python manage.py makemigrations  # 创建建表语句
python manage.py migrate  # 创建数据库

python manage.py createsuperuser  # 创建超级用户
```

## setting.py
``` conf
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
```