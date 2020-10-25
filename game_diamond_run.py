#create a simple game where your player should collect coins and when a coins is touched then u should update the score and draw the coin to 
#another location
#There should be also an item, which the player should not collide with and the item sould always move on diagonal x and y axis. 
# screen size should be w = 1080, h = 800 player should be keyboard control. u can use any images add a background too.


import random
HEIGHT=700
WIDTH=1024
gb = Actor('boy_run')
cb=Actor("crocodile")
db=Actor("diamond")
gb.pos = (550,50)
cb.pos=(50,500)
db.pos=(50,50)
score=0

bg= Actor("background")

def draw():
    screen.clear()
    bg.draw()
    gb.draw()
    cb.draw()
    db.draw()
    
    screen.draw.text(f"SCORE : {score}",(10,10))
    

def update():
    cb.x+=2
    cb.y+=2
    if cb.x>960:
        cb.x=random.randint(0,1024)
    if cb.y>640:
        cb.y=random.randint(0,700)
    if keyboard.right :
        gb.x += 3
        if gb.x>980:
            gb.x=980
    elif keyboard.left:
        gb.x -= 3
        if gb.x<50:
            gb.x=50
    elif keyboard.up:
        gb.y -= 3
        if gb.y<34:
            gb.y=34
    elif keyboard.down:
        gb.y += 3
        if gb.y>640:
            gb.y=640

    

    global score
    if gb.colliderect(db):
        gb.image="boy_cheer"
        score+=1
        db.pos=random.randint(0,1024),random.randint(0,700)
        clock.schedule_unique(fall_boy,0.5)
        

    if gb.colliderect(cb):
        gb.image = "boy_fall"
        score-=1
        cb.pos=random.randint(0,1024),random.randint(0,700)
        clock.schedule_unique(fall_boy,0.75)


def fall_boy():
    gb.image = "boy_run"
