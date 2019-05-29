from flask import flash, redirect, url_for, render_template
from . import app, db
from . import models, forms


@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.SearchForm()
    if form.validate_on_submit():
        name = form.name.data
        poetries = models.Poets.query.filter_by(name=name).first().poetries

        # flash('Your message have been sent to the world!')
        return render_template('index.html', form=form, poetries=poetries, poet=name)

    name = '李世民'
    poetries = models.Poets.query.filter_by(name=name).first().poetries
    return render_template('index.html', form=form, poetries=poetries, poet=name)

