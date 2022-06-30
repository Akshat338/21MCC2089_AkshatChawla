import pygame
import button
import textbox

import label
import register
import mysql.connector
bg_img=pygame.image.load('img1/background3.jpg')
bg_img=pygame.transform.scale(bg_img,(800,800))
login_img=pygame.image.load('img1/login.png')
login_img=pygame.transform.scale(login_img,(150,80))
back_img=pygame.image.load('img1/back.png')
back_img=pygame.transform.scale(back_img,(50,50))
register_img=pygame.image.load('img1/register.png')
register_img=pygame.transform.scale(register_img,(150,80))


button1=button.Button(200,620,login_img,1)
button2=button.Button(400,620,register_img,1)
back=button.Button(170,170,back_img,1)

BG= (144,201,120)
def draw_bg(screen):
	screen.blit(bg_img,(0,0))
	

	pass
def checkdata(username,password,screen):
	record=[]
	uid=0
	uname=0
	
	if username=='':
		msg1="Email is empty"
		return False,record,msg1
		pass
	else:	
		conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="shortcut_jump")
		cursor=conn.cursor()
		cursor.execute("select * from users where email=%s AND password=%s",(username,password))
		record=cursor.fetchall()
		if record:
			msg2="Login Sucessfull"
			return True,record,msg2
		else:
			msg3="Email & password does not match"
			return False,record,msg3
		cursor.close()
		conn.close()	
			
def loop(screen):
	login=True
	username=textbox.Textbox(screen,380,430,280,40)
	password=textbox.Textbox(screen,380,550,280,40)
	check=True
	record=[]
	while login:
		draw_bg(screen)
		username.draw('simple')
		password.draw('password')
	  #	label.draw('Login',(255,255,255),250,150,screen,60,'Arial Black')
	  #	label.draw('Email :',(255,255,255),170,230,screen,36,'Cambria')
	  #	label.draw('Password: ',(255,255,255),170,320,screen,36,'Cambria')
		if check==False:
			label.draw(msg,(255,0,0),280,280,screen,18,'Cambria')
			pass
		pos=pygame.mouse.get_pos()
		username.update(pos)
		password.update(pos)
		if button1.draw(screen):
			uname=username.gettext()
			passw=password.gettext()
			checklogin,record,msg=checkdata(uname,passw,screen)
			if checklogin:
				check=True
				return True,True,record
			else:	
				check=False
		if button2.draw(screen):
			register.loop(screen)
		if back.draw(screen):
			return False,True,record
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				return False,False,record
			if event.type==pygame.KEYDOWN:
				username.user_input(event)
				password.user_input(event)

		pygame.display.update()
				

	pass