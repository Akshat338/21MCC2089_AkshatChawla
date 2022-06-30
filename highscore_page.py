import pygame
import button
import mysql.connector
import label
bg_img=pygame.image.load('img1/highscorebackground.jpg')
bg_img=pygame.transform.scale(bg_img,(800,800))
back_img=pygame.image.load('img1/back.png')
back_img=pygame.transform.scale(back_img,(50,50))
back=button.Button(170,50,back_img,1)
def loop(screen):
	loop=True
	while loop:
		screen.blit(bg_img,(0,0))
		
		conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="shortcut_jump")
		cursor=conn.cursor()
		cursor.execute("select username,score from users order by score desc limit 10")
		record=cursor.fetchall()
		i=0
		for rec in record:
			label.draw(f'{rec[0]}',(0,0,0),260,150+i,screen,28,'Joker Man')
			label.draw(f'{rec[1]}',(0,0,0),520,150+i,screen,28,'Joker Man')
			i+=60
			pass
		if back.draw(screen):
			loop=False
			pygame.time.delay(200)
			pass
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				loop=False
		pygame.display.update()


		pass