import pygame 
vec=pygame.math.Vector2

class Textbox:
    """docstring for Textbox"""
    def __init__(self, surface,x,y,width,height,state='',color=(176,176,176),active_color=(255,255,255),border=True,
        border_color=(0,0,0),border_width=2,text_name='jokerman',text_size=20,text_color=(0,0,0)):
        self.x = x
        self.y = y
        self.pos = vec(x,y)
        self.width = width
        self.height = height
        self.surface=surface
        self.image = pygame.Surface((width,height))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.state = state
        self.color = color
        self.active_color = active_color
        self.border = border
        self.border_color = border_color
        self.border_width = border_width
        self.text = []
        self.font_name = text_name
        self.font_size = text_size
        self.text_color=text_color
        self.cursor_pos=0
        self.active=False
        self.hovered=False
        self.click=False
    def update(self,pos):
        if self.is_hovered(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.click=True
            self.hovered=True
            self.active=True
        else:
            if pygame.mouse.get_pressed()[0] == 1:
                self.click=False
            self.hovered=False
            self.active=False
    def draw(self,typ):
        if self.border:
            
            if self.click:
                self.image.fill((0,0,255))
                pygame.draw.rect(self.image,self.active_color,(self.border_width,self.border_width,self.width-(self.border_width*2),self.height-(self.border_width*2)))
            else:
                self.image.fill((0,0,0))
                pygame.draw.rect(self.image,self.active_color,(self.border_width,self.border_width,self.width-(self.border_width*2),self.height-(self.border_width*2)))
        else:
            if self.active:
                self.image.fill(self.active_color)
            else:
                self.image.fill(self.color)
        if len(self.text)>0:
            self.show_text(typ)
        self.surface.blit(self.image,self.pos)
    def is_hovered(self,pos):
        if pos[0]>self.pos.x and pos[0]<self.pos.x+self.width:
            if pos[1]>self.pos.y and pos[1]<self.pos.y+self.height:
                
                return True

        return False
    def show_text(self,typ):
        text=''.join(self.text)
        ptext=''
        font=pygame.font.SysFont(self.font_name,self.font_size)
        if typ=='password':
        	for x in text:
        		ptext=ptext+'*'
        	text=font.render(ptext,False,self.text_color)
        else:	
        	text=font.render(text,False,self.text_color)
        size=text.get_size()
        
        if size[0]+10>self.width+10:
            x,y=self.width-(size[0]+10),(self.height//2)-(size[1]//2)
        else:
            x,y=10,(self.height//2)-(size[1]//2)
        pos=(x,y)
        self.image.blit(text,pos)
    def gettext(self):
        data=''
        for x in range(0,len(self.text)):
            data=data+self.text[x]
        return data
        pass
    def user_input(self,event):
        if self.click:
            if event.key != 13 and event.key != 273 and event.key != 274 and event.key != 275 and event.key != 276 and event.key != 8 and event.key != 127:
                self.text.insert(self.cursor_pos,event.unicode)
                self.cursor_pos+=1
            elif event.key==8 and self.cursor_pos>0 and len(self.text)>0:
                del self.text[self.cursor_pos-1]
                self.cursor_pos-=1





                
            
            