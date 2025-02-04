from market import app, db
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import SignupForm, LoginForm

@app.route('/')
@app.route('/home') 
def home_page(): 
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)   

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    form= SignupForm()

    if form.validate_on_submit():
        user_to_create= User(username=form.username.data,
                            email_address= form.email_address.data,
                            password= form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        flash('Registered Successfully!')
        return redirect(url_for('home_page'))
        
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash (f'There was an error in creating account: {err_msg}', category='danger' )
         
    return render_template('signup.html', form=form)

@app.route('/error404tnf')
def users_page():
    all_users = User.query.all()
    return render_template('users.html', users= all_users)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Registered Successfully!')
        return redirect(url_for('home_page'))
    else:
        return render_template('login.html', form=form)    




