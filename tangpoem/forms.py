from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class SearchForm(FlaskForm):
    name = StringField('诗人姓名', validators=[DataRequired(), Length(1, 40)], description='请输入诗人的姓名')  # 诗人名字
    # body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField('搜索诗歌')
