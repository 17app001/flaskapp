https://www.youtube.com/watch?v=aY5Ygawb9Tk

conda create -n flaskenv
pip install flask
pip install flask_SQLAlchemy
pip install mysqlclient



## 需增加
- app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:12345678@localhost/flaskapp'
- app.app_context().push()