from app import db


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(120), index=True, unique=False)
    roomnumber = db.Column(db.String(6), index=True, unique=False)
    admissionnumber = db.Column(db.String(10), index=True, unique=False)
    mobile = db.Column(db.String(13), index=True, unique=False)
    review = db.Column(db.String(500), index=True, unique=False)
    
    # Tells how to print the class object
    # Helpful for debugging
    def __repr__(self):
        return '<Student {}>'.format(self.admissionnumber)    
