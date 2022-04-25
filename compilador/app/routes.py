from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app.process.lexico import lexica

@app.route('/')
@app.route('/index')
def index():
    user = { 'username' : 'Bruna' }
    return render_template('index.html', title='Compilador', user=user)

@app.route('/entradas', methods=['GET', 'POST'])
def entradas():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f''' Enviado {form.entrada.data}''')
        processos = lexica(form.entrada.data)
        print(processos)
        return render_template('processed.html', processos=processos)
    return render_template('entradas.html', form=form)