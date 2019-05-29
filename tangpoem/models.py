from . import app, db


class Poets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)

    poetries = db.relationship('Poetries')  # 定义关系属性，它不是数据库的字段，而是快捷查询。relationship函数的第一个参数是关联表对应的类名。


class Poetries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poet_id = db.Column(db.Integer, db.ForeignKey('poets.id'), nullable=True)
    title = db.Column(db.String, nullable=True)
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
    # todo: 定义双向关系， back_populates 属性
