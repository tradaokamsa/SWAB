from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db_name ='sockmarket.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Sock(db.Model):
    __tablename__ = 'socks'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    do_Ph = db.Column(db.Float)
    nhiet_do = db.Column(db.Float)
    do_duc = db.Column(db.Float)
    


@app.route('/inventory/<status>')
def inventory(status):
    socks = Sock.query.filter_by(status=status).order_by(Sock.do_Ph).all() 
    return render_template('index.html', socks=socks, status=status)

if __name__ == "__main__":
    app.run(debug=True) 