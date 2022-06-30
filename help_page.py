import pygame
import button
bg_img=pygame.image.load('img1/help.jpg')
bg_img=pygame.transform.scale(bg_img,(800,800))
back_img=pygame.image.load('img1/back.png')
back_img=pygame.transform.scale(back_img,(50,50))
back=button.Button(170,130,back_img,1)
def loop(screen):
	loop=True
	while loop:
		screen.blit(bg_img,(0,0))
		if back.draw(screen):
			loop=False
			pygame.time.delay(200)
			pass
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				loop=False
		pygame.display.update()


		pass