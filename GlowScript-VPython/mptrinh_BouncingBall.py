from vpython import *
#GlowScript 2.9 VPython
# May Trinh
# This project will create a simple ball in 3D and drop it from a specific 
# height above a floor. It will update the position and velocity everytime
# the ball hit the floor. The animation will stop after a certain time.

#change background's color
scene.background = vec(0.22,0.22,0.22)
floor = box(pos=vec(0,-4,0),size=vec(12.5,0.5,12.5),color=color.green)
ball = sphere(pos=vec(0,6,0),radius=1,color=vec(random(),random(),random()))

ball.velocity = vec(0.0,0.0,0.0)

dt = 0.05 #delta t
g = -9.81 #gravity force
t = 0.1
while t < 20:
    rate (50)
    ball.velocity.y = ball.velocity.y + g * dt  
    ball.pos = ball.pos + ball.velocity*dt
    
    if ball.pos.y < floor.pos.y + ball.radius:
        #change ball's velocity 
        ball.velocity.y =- ball.velocity.y * 0.9
        #change ball's height
        ball.pos.y = floor.pos.y + ball.radius + 0.1
        
        #change floor's color to the ball's color everytime the ball hit it
        floor.color = ball.color
        #change the ball's color randomly
        ball.color = vec(random(),random(),random())  
    t = t+dt
