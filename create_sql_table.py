import mysql.connector as mc
mydatabase=mc.connect(host="localhost",user="root",passwd="3613642",database="week5")
#passwd is your sql passwd
#THERE SHOULD ALREADY EXIST A DATABASE OF ANY NAME
cursor=mydatabase.cursor()

cursor.execute("CREATE TABLE recipes(Id INT ,name VARCHAR(30),description VARCHAR(30),category_id INT ,chef_id INT, created_by VARCHAR(30));") 
mydatabase.commit()
