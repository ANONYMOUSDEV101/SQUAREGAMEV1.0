import os
import time
import random
import pygame
pygame.init()
height = 700
width = 700
blue = (0,0,255)
red=(255,0,0)
green=(0,255,0)
white=(255,255,255)
black=(0,0,0)
clock=pygame.time.Clock()
player=pygame.image.load("pointer.png")
laser=pygame.image.load("laser.png")
laser2=pygame.image.load("laser2.png")
companion=pygame.image.load("poiner.png")
reds=pygame.image.load("test.png")
shield=pygame.image.load("shield.png")
shieldimg=pygame.image.load("shieldimage.png")
text=pygame.font.SysFont("comicsanisms",40)
win=pygame.display.set_mode((height,width))
pygame.display.set_caption("SQUAREGAME")
def play():
	text=pygame.font.SysFont("comicsanisms",40)
	game = True
	x = 250
	velocity = 10
	a=-100
	b=-100
	se = 0
	energy = 1000
	y = 250
	shieldp = 0
	text1=text.render("X: %s, Y: %d"  %(x,y)  ,True, white)
	bot = 0
	times = 0
	timek = 0
	e = 250
	fu = 0
	k = 250
	timeb = 0
	timef = 0
	timeshield = 0
	dash = 0
	bots = 1
	fight = 0
	fightf = 0
	fighta = 0
	o = 400
	j = 300
	com = 0
	l = random.randrange(0,800)
	m = l
	shielda = 0
	collect = 0
	score = 0
	while game:
		if timek == 3:
			timek = 0
		text4=text.render("Time: %s" %(timeb),True,white)
		text2=text.render("Score: %s" %(score),True,white)
		text3=text.render("ENERGY: %s" %(energy),True,white)
		text1=text.render("X: %s, Y: %s" %(x,y),True,white)

		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game = False
				pygame.quit()
				
		keys = pygame.key.get_pressed()
		if keys[pygame.K_f]:
			if fight == 0 and fightf == 0:
				fight = 1
				fightf = 1
				fighta = 1
				b = random.randrange(0,700)
				a = random.randrange(0,700)
				print("BOT enabled")
				time.sleep(0.3)
				
			else:
				print("BOT disabled")
				time.sleep(0.3)
				
		win.fill(blue)
		if keys[pygame.K_TAB] and energy >= 1000:
			if fight == 1 and fightf == 0:
				energy -= 1000
				y = b
				x = a 
				
			if fight == 0 and fightf == 1:
				energy -= 1000
				y = e
				x = k
				
			if fighta == 1 and fight == 0 and fightf == 0:
				energy -= 1000
				y = o
				x = j
				                    
		if keys[pygame.K_UP]:
			y -= velocity
			
		if keys[pygame.K_DOWN]:
			y += velocity
			
		if keys[pygame.K_LEFT]:
			x -= velocity
			
		if keys[pygame.K_RIGHT]:                                                    
			x += velocity
			
				
		if com == 1 and collect == 0:
			win.blit(shield,(l,m))			
				
			
		if fight != 0:
			se=random.randint(1,2)
			win.blit(reds,(a,b))
			
		if fightf != 0:
			win.blit(reds,(e,k))
		
		
		if fighta != 0:
			win.blit(reds,(j,o))
			
		if y == b:
			f = random.randrange(x,x+62)
			s = random.randrange(y,y+69)
			
		else:
			f = -10
			s = -10
			
		if x == a and y == b and fight == 1:
			energy += 50
			score += 1
			fight = 0
			x -= 10
			y -= 10
			fu = 1
			time.sleep(1)
		if x == e and y == k and fightf == 1:
			score += 1
			energy += 50
			fightf = 0
			x -= 10
			y -= 10
			time.sleep(1)
			fu = 1
			
		if o == y and j == x:
			fighta = 0
			score += 1
			fu -= 1
			x -= 10
			y -= 10
			time.sleep(1)
			fu = 1
			energy += 50
		if keys[pygame.K_c] and collect == 0 and com == 1:
			x = l
			y = m
			
			
		if fightf == 0 and fight == 0:
			if fu == 1:
				com=random.randrange(1,3)
				

		 
		if keys[pygame.K_SPACE]:
			if timef != 200:
				energy -= 1
				dash = 1
				timef += 1
				
			if timef == 200:
				dash = 0
				timef = 0
				velocity = 10
				
		if dash == 1:
			velocity = 20	
		
		if times == 100:
			timek += 1
			
		if timek == 1:
			if x > a and fight == 1:
				win.blit(laser2,(a+62,b))
				#pygame.display.update()
				if a  + 138 + 52 == x and b  == y and shielda == 0:
					game = False
					timeb += 1
					lose(score,timeb)
					
					
		if timek == 1:
			if x < e and fightf == 1:
				win.blit(laser2,(e - 138,k))
				if e - (138 + 52) == x and k == y and shielda == 0:
					game = False
					timeb += 1
					lose(score,timeb)
					
					
		if timek == 1:
			if y < o and fighta == 1:
				win.blit(laser,(j,o - 129)) 
				if o - 129 == y and x == j and shielda == 0:
					game = False
					timeb += 1
					lose(score,timeb)
					
		if shielda == 1:
			win.blit(shieldimg,(x - 10,y - 10))
						
		win.blit(text1,(10,10))
		win.blit(text2,(10,50))
		win.blit(text3,(10,100))
		win.blit(text4,(150,50))
		
		if x == l and y == m:
			collect = 1
			shielda = 1
		if times == 100:
			timeb += 1
			times = 0
			
		if energy <= 100:
			velocity = 5
			energy += 5
					
		print("Tries: %s" %(f))
		print("Tried: %s" %(s))
		win.blit(player,(x,y))
		times += 1
		if x - (138 + 52) > a:
			a += 1
		
		
		if y > b:
			b += 1
			
		pygame.display.update()
		
		if y < b:
			b -= 1 
			
		if x - (138 + 52) < a:
			a -= 1 
			
		if x + (138+52) < e:
			e -= 1
			
		if  x > e:
			e += 1
			
		if y > k:
			k += 1
			
		if y < k:
			k -= 1
			
		if o  > y -129:
			o -= 1
			
		if o< y  + 129:
			o += 1
			
		if j < x:
			j += 1
			
		if j > x:
			j -= 1
			
		if y + 129 > o:
			o += 1
		
		if timek == 1:
			timeshield += 1
		
		if timeshield == 500:
			shielda = 0
			com = 0
			fu = 0
			collect = 0
			timeshield = 0
			
		
					
		pygame.display.update()
			
		
def lose(score,timeb):
	lose = True
	text=pygame.font.SysFont("comicsanisms",50)
	text1=text.render("You died!",True,red)
	text2=text.render("You survived %s s, score: %s" %(timeb,score),True,red)
	while lose:
		clock.tick(60)
		win.fill(black)
		win.blit(text1,(250,10))
		win.blit(text2,(10,50))
		keys=pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				lose = False
				pygame.quit()
				
		if keys[pygame.K_SPACE]:
			lose = False
			play()
		pygame.display.update()
		
play()
