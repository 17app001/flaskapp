from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:12345678@localhost/flaskapp'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://admin:me516888@database-1.cr1dzex4jzdk.ap-northeast-1.rds.amazonaws.com/flaskapp'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='asdasderiedfslkf%^%^%'

db=SQLAlchemy(app)
app.app_context().push()

class Book(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    author=db.Column(db.String(100),nullable=False)
    price=db.Column(db.Float)

    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price


@app.route('/')
def index():
    books=Book.query.all()
    return render_template('./index.html',books=books)

@app.route('/add/',methods=['POST'])
def insert_book():
    if request.method=='POST':
        book=Book(
            title=request.form.get('title'),
            author=request.form.get('author'),
            price=request.form.get('price')
        )
        db.session.add(book)
        db.session.commit()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
