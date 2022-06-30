import pygame
import mysql.connector

def create_guest():
	
	conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="shortcut_jump")
	cursor=conn.cursor()
	cursor.execute("insert into users (username,email) values('','')")
	conn.commit()
	cursor.execute("select * from users where email=''")
	record=cursor.fetchall()
	for rec in record:
		gid=rec[0]
	guest_name="Guest"+f'{gid}'	
	cursor.execute("update users set username=%s,email=%s where id=%s",(guest_name,guest_name,gid))
	conn.commit()
	cursor.close()
	conn.close()
	gid,name,record=get_data(guest_name)
	return gid,name,record


def get_data(guest_name):
	guest=guest_name
	conn1=mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="shortcut_jump")
	cursor1=conn1.cursor()
	cursor1.execute(f"select * from users where email='{guest}'")
	record=cursor1.fetchall()
	for rec in record:
		gid=rec[0]
		name=rec[1]
	return gid,name,record	
	cursor1.close()
	conn1.close()
	