from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc


app = Flask(__name__)

db_name ='data1.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Sock(db.Model):
    __tablename__ = 'socks'
    
    do_Ph = db.Column(db.Float, primary_key=True)
    do_duc = db.Column(db.Float)
    
db.create_all()

@app.route('/')
def api():
    do_Ph = request.args.get('do_Ph')
    do_duc = request.args.get('do_duc')
    dbsock = Sock(do_Ph=do_Ph, do_duc=do_duc)
    try:
        db.session.add(dbsock)
        return db.session.commit()
    except exc.IntegrityError:
        db.session.rollback()
        return 'ok'
    
    
    

@app.route('/web')
def index():
    sock=Sock.query.all()[-1]
    doPh = sock.do_Ph
    doduc=sock.do_duc

    return render_template('index.html', doPh=doPh, doduc=doduc)
    

    
if __name__ == "__main__":
    app.run(debug=True) 