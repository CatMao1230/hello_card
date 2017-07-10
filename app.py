from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    name = TextField('name:', validators=[validators.required()])
    account = TextField('account:', validators=[validators.required()])
    dept = TextField('dept:', validators=[validators.required()])
    position = TextField('position:', validators=[validators.required()])
    other = TextField('other:', validators=[validators.required()])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        name=request.form['name']
        account=request.form['account']
        dept=request.form['dept']
        position=request.form['position']
        other=request.form['other']
 
        if form.validate():
            return render_template('result.html', name = name, account = account, dept = dept, position = position, other = other)
        else:
            flash('All the form fields are required. ')
 
    return render_template('index.html', form=form)
 
if __name__ == "__main__":
    app.run()
