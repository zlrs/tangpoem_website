# 唐诗搜索网站
一个搜索唐诗的网站，唐诗数据库来自Github项目[全唐诗数据库](https://github.com/hxgdzyuyi/tang_poetry)

## checkout submodule
本项目使用git子模块(git submodule)引用sql数据。为了获取数据，首先需要初始化子模块。初始化子模块有几种方法。

1. 通过Github Desktop 克隆项目的，这会自动进行子模块的初始化。

2. 克隆项目时加上`--recurse-submodules`参数：`git clone <repo> --recurse-submodules`

3. 运行以下命令:
```
git submodule init
git submodule update
```
最终data/文件夹下有.sql文件就行了

## 安装依赖
本项目使用pipenv管理依赖。

在项目根目录运行：`pipenv install`

有可能会提示python版本不符，可以手动指定python版本或安装路径
- `pipenv install --python 3.7`
- `pipenv --python path\to\python`

## 设置数据库URI
```
cd <project_root>
echo FLASK_DATABASE_URI="mysql+pymysql://root:password@localhost/database" > .env
```

## 运行开发服务器
`pipenv run flask run`

Happy pythoning!
