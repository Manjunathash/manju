from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Manju@20@localhost/flask_orm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True

db = SQLAlchemy(app)

class CreateTable(db.Model):
    __tablename__='orm_table'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(30))

@app.route('/write')
def write():
    name="Chinmay"
    password = "12345"
    insert_data = CreateTable(name = name,password = password)
    save_to_database = db.session
    try:
        save_to_database.add(insert_data)
        save_to_database.commit()
        return ("SUCCESS : Data Saved !")
    except:
        save_to_database.rollback()
        save_to_database.flush()
        return ("ERROR : Data cannot be saved")

if __name__ =='__main__':
    db.create_all()
    app.run(debug=True)