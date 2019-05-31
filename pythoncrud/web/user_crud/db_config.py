from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'rootroot'
app.config['MYSQL_DATABASE_DB'] = 'python_test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'rootroot'
#app.config['MYSQL_DB'] = 'python_test'

#mysql = MySQL(app)
