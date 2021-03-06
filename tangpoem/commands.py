import click
from . import app, db
from sqlalchemy import text  # todo: 看着text函数定义


@app.cli.command()
def build_db():
    """
    Create database and execute sql after drop.
    Note: This command may fail due to imappropriate models defination. Using 
    `mysql -u root -p <db> < data/tang.sql` to create tables is most recommanded.
    """
    click.confirm('This operation will drop existing tables and data, do you want to continue?', abort=True)
    db.drop_all()
    click.echo('Dropped tables.')

    db.create_all()  # 创建数据库结构

    sql = ''  # 导入唐诗
    for line in open("../data/tang_poetry.sql"):
        sql += line
        if sql.strip().endswith(';'):
            db.session.execute(text(sql))
            sql = ''
    db.session.commit()
