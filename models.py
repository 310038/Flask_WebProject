from exts import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True) #設置(主鍵)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(100), nullable=False,unique=True)
    join_time = db.Column(db.DateTime,default=datetime.now)
    # 小心datetime.now()，不用()。如果是傳入datetime.now()的話，傳入的是一個值。而因為我們要傳入的是一個函數，
    # 而不是函數的值