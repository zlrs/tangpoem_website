import os
import sys

SQLALCHEMY_TRACK_MODIFICATIONS = False

dev_uri = None
SQLALCHEMY_DATABASE_URI = os.getenv('FLASK_DATABASE_URI', dev_uri)

if SQLALCHEMY_DATABASE_URI is None:
    print("温馨提示：SQLALCHEMY配置出错，是否忘记设置`FLASK_DATABASE_URI`环境变量？")
    sys.exit(0)
elif SQLALCHEMY_DATABASE_URI is dev_uri:
    print("温馨提示：正在使用开发环境数据库URI")

# WTF_CSRF_ENABLED=False
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
# todo: 重写readme
# todo: 网站上线
