from app import app, db
from app.models import Review
from flask import render_template, request, flash, redirect, url_for
import sys
import json

@app.route('/', methods=['GET', 'POST'])
def session():
    if request.method == 'GET':
        reviews = Review.query.all()
        reviews.reverse()
        return render_template('home.html', reviews=reviews, staff=0)

@app.route('/staff', methods=['GET', 'POST'])
def staff():
    if request.method == 'GET':
        reviews = Review.query.all()
        reviews.reverse()
        return render_template('home.html', reviews=reviews, staff=1)
    
# Login for staff users
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        if request.form["username"] == 'staff' and request.form["password"] == 'shravan':
            return redirect(url_for('staff')) # This staff does not give value to the parameter (when used as session, staff=1)
        else:
            flash("Incorrect username or password. Try again!")
            return render_template('login.html')
    
@app.route('/review', methods=['GET', 'POST'])
def review():
    if request.method == 'GET':
        return render_template('contactus.html')
    elif request.method == 'POST':
        message = Review(
                name = request.form["name"],\
                roomnumber = request.form["roomnumber"],\
                admissionnumber = request.form["admissionnumber"],\
                mobile = request.form["mobile"],\
                review = request.form["review"]
                )
        try:
            db.session.add(message)
            db.session.commit()
            flash('Your review has been sent to the concerned authorities!')
        except Exception as e:
            print("\n FAILED entry")
            print(e)
            sys.stdout.flush()
        reviews = Review.query.all()
        reviews.reverse()
        return redirect(url_for('session'))

@app.route('/review/delete/<id>', methods=['POST'])
def reviewdelete(id):
    if request.method == 'POST':
        db.session.query(Review).filter_by(id=id).delete()
        db.session.commit()
        
        reviews = Review.query.all()
        reviews.reverse()
        return redirect(url_for('staff'))