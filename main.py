from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
# from app import db

app=Flask(__name__)
app.config.from_object(DevConfig)
db=SQLAlchemy(app)
# SQLAlchemy会从app的配置中读取信息，自动连接到数据库

class User(db.Model):
	# __tablename__='user_table_name'
	# # 将表命名为user_table_name

	id=db.Column(db.Integer(),primary_key=True)
	username=db.Column(db.String(255))
	password=db.Column(db.String(255))

	# def __init__(self, username):
	# 	self.username=username

	# def _repr__(self):
	# 	return "<User '{}'>".format(self.username)
		

@app.route('/')
def home():
    return '<h1>Hello world</h1>'

if __name__=='__main__':
    app.run()