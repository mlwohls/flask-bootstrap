from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, AuthKeys
import psycopg2
# from hc_database import AutoBase, Candidate

# # packages for automapping
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session


#############################

app = Flask(__name__)

### Connection For APP Database #########
engine = create_engine('postgresql://mlwohls2:12temp34@bootstrap-db.chwr0n3sezpi.us-east-1.rds.amazonaws.com/flask_bootstrap')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

####### Connection for HC Database #######
# db2 = create_engine('postgresql://udemeb02aj6tg6:p17p03n8l7pr0t8lvsfk1crol6d@ec2-52-201-127-122.compute-1.amazonaws.com/dalsteca66kgv9')
# AutoBase.prepare(db2, reflect=True)
# DB2Session = sessionmaker(db2)
# session_hc = DB2Session()

print "Connecting to HC Database"
try:
    conn = psycopg2.connect(host="ec2-52-201-127-122.compute-1.amazonaws.com", database="dalsteca66kgv9", user="udemeb02aj6tg6", password="p17p03n8l7pr0t8lvsfk1crol6d")
    cur = conn.cursor()
    print "HC DB Connected Successfully"
except:
    print "HC DB Connection Error"
    quit()

cur.execute(''' SELECT id FROM candidates''')
cand_pull = cur.fetchall()
cand_count = str(len(cand_pull))


@app.route('/')
def index():
    output = ""
    output += "<html><body>"
    output += "<h1>"
    output += cand_count
    output +=  "</h1>"
    output += "</body></html>"
    return output
    # return render_template('index.html')

@app.route('/user/new', methods=['GET', 'POST'])
def newUser():
    if request.method == 'POST':
        newUser = User(name = request.form['name'], password = request.form['password'])
        session.add(newUser)
        session.commit()
        flash("new user created - MLW")
        return render_template('index.html')

# Task 1: Create route for newMenuItem function here

# @app.route('/restaurants/<int:restaurant_id>/new', methods=['GET', 'POST'])
# def newMenuItem(restaurant_id):
#     if request.method == 'POST':
#         newItem = MenuItem(name = request.form['name'], restaurant_id = restaurant_id)
#         session.add(newItem)
#         session.commit()
#         flash("new menu item created - MLW")
#         return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
#     else:
#         return render_template('newmenuitem.html', restaurant_id = restaurant_id)
#     return "page to create a new menu item. Task 1 complete!"
#
# # Task 2: Create route for editMenuItem function here
#
# @app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit', methods = ['GET', 'POST'])
# def editMenuItem(restaurant_id, menu_id):
# 	editedItem = session.query(MenuItem).filter_by(id = menu_id).one()
# 	if request.method == 'POST':
# 		if request.form['name']:
# 			editedItem.name = request.form['name']
# 		session.add(editedItem)
# 		session.commit()
# 		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
# 	else:
# 		#USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
# 		return render_template('editmenuitem.html', restaurant_id = restaurant_id, menu_id = menu_id, i = editedItem)
#
# # Task 3: Create a route for deleteMenuItem function here
#
# @app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete', methods = ['GET','POST'])
# def deleteMenuItem(restaurant_id, menu_id):
# 	itemToDelete = session.query(MenuItem).filter_by(id = menu_id).one()
# 	if request.method == 'POST':
# 		session.delete(itemToDelete)
# 		session.commit()
# 		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
# 	else:
# 		return render_template('deletemenuitem.html', item = itemToDelete, restaurant_id = restaurant_id)



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
