from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask('tangpoem')
bootstrap = Bootstrap(app)
app.config.from_pyfile('settings.py')

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)

from . import views, models, commands


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Poets=models.Poets, Poetries=models.Poetries)


