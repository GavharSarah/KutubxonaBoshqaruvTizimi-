import psycopg2
db_config={
    "port":"5432",
    "host":"localhost",   
    "database":"kutubxona" ,
    "user":"kutubxonachi",
    "password":"12345678"
     }

conn=psycopg2.connect(**db_config)
cursor=conn.cursor()    
cursor.execute(query="insert into authors (full_name) values ('Abdurahmon Abdullayev'),('Abdulloh Abdushukorov')")
conn.commit()
print(" info inserted into  Table'authors' created successfully.")
