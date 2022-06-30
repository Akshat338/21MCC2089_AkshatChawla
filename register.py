import pygame
import button
import textbox
import label
import mysql.connector
bg_img=pygame.image.load('img1/background2.jpg')
bg_img=pygame.transform.scale(bg_img,(800,800))
register_img=pygame.image.load('img1/register.png')
register_img=pygame.transform.scale(register_img,(250,80))
button2=button.Button(260,700,register_img,1)
back_img=pygame.image.load('img1/back.png')
back_img=pygame.transform.scale(back_img,(50,50))
back=button.Button(150,90,back_img,1)
BG= (144,201,120)
def draw_bg(screen):
	screen.blit(bg_img,(0,0))
	

	pass
def register(uname,email_id,cpassword_val,password_val):	
	conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="shortcut_jump")
	cursor=conn.cursor()
	if email_id=='':
		msg="Email is compulsary"
		return msg,False
	elif uname=='':
		msg="User name is compulsary"
		return msg,False
	elif password_val!=cpassword_val or cpassword_val=='' or password_val=='':
		msg="Password doesn't match"
		return msg,False
		pass	
	else:
		cursor.execute("select email from users")
		record=cursor.fetchall()
		for rec in record:
			if rec[0]==email_id:
				msg="Email already exists"
				return msg,False
		cursor.execute("insert into users (username,email,password) values(%s,%s,%s)",(uname,email_id,password_val))
		conn.commit()
		cursor.close()
		conn.close()
		msg='Register sucessfully'
		return msg,True

def loop(screen):
	login=True
	check=True
	username=textbox.Textbox(screen,450,300,200,40)
	email=textbox.Textbox(screen,450,400,200,40)
	password=textbox.Textbox(screen,450,500,200,40)
	cpassword=textbox.Textbox(screen,450,600,200,40)

	while login:
	
		draw_bg(screen)
		username.draw('simple')
		email.draw('simple')
		cpassword.draw('password')
		password.draw('password')
		#label.draw('Sign Up',(255,255,255),250,70,screen,60,'Arial Black')
		#label.draw('Email* :',(255,255,255),400,150,screen,28,'Cambria')
		#label.draw('User Name* :',(255,255,255),150,150,screen,28,'Cambria')
		#label.draw('Country :',(255,255,255),400,250,screen,28,'Cambria')
		#label.draw('Gender :',(255,255,255),150,250,screen,28,'Cambria')
		#label.draw('Password* :',(255,255,255),150,350,screen,28,'Cambria')
		#label.draw('Confirm Password* : ',(255,255,255),400,350,screen,28,'Cambria')
		if check==False:
			label.draw(msg,(0,0,255),250,220,screen,28,'Cambria')
		if back.draw(screen):
			login=False
		pos=pygame.mouse.get_pos()
		username.update(pos)
		uname=username.gettext()
		email.update(pos)
		email_id=email.gettext()
		cpassword.update(pos)
		cpassword_val=cpassword.gettext()
		password.update(pos)
		password_val=password.gettext()
		if button2.draw(screen):
			msg,check=register(uname,email_id,cpassword_val,password_val)
			if check==True:
				login=False
				pass
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pass
			if event.type==pygame.KEYDOWN:
				username.user_input(event)
				email.user_input(event)
				cpassword.user_input(event)
				password.user_input(event)
		pygame.display.update()