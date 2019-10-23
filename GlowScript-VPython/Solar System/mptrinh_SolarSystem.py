from vpython import *
#GlowScript 2.9 VPython
#May Trinh
#Simple Solar System
#Calculate velocity, grativational force, and new position of 3 planets (Earth,
#Mars,Venus) in regard to the Sun based on given formulas.
#(1) p = p + vt + (1/2)a(t**2)
#(2) v = v + at
#(3) F = KM1M2/(r**2)
#(4) a = F/m

scene.lights[0].visible=False
planets = []
#less mass for Sun, less gravitational force
sun = sphere(pos=vec(0,0,0),radius=0.7,mass = 2500,velocity = vec(0,0,0), emissive = True, texture = "http://i.imgur.com/yoEzbtg.jpg")
lamp = local_light(pos=vector(0,0,0), color=color.yellow)
# create the Earth object
earth = sphere (pos=vec(3,0,0), radius = 0.2, mass =1.67, velocity=vec(0,27,0), texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Nasa_land_ocean_ice_8192.jpg/320px-Nasa_land_ocean_ice_8192.jpg", flipx = False)
#create the Mars object
mars = sphere (pos=vec(4,0,0), radius = 0.1, mass = 0.567, velocity = vec(0,25,0), texture ="https://vignette.wikia.nocookie.net/planet-texture-maps/images/1/19/Mars_Map.png/revision/latest/scale-to-width-down/451?cb=20190402042909")
venus = sphere (pos=vec(2.2,0,0), radius = 0.1, mass = 1.5, velocity = vec(0,30,0), texture ="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/90ad8232-4e09-4675-b9e7-bc2898960870/dc0ss1u-9ce1cbd0-6f56-4bb1-ab24-e64089914504.png/v1/fill/w_1024,h_512,q_80,strp/venus_cloud_texture_map_by_jcpag2010_dc0ss1u-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTEyIiwicGF0aCI6IlwvZlwvOTBhZDgyMzItNGUwOS00Njc1LWI5ZTctYmMyODk4OTYwODcwXC9kYzBzczF1LTljZTFjYmQwLTZmNTYtNGJiMS1hYjI0LWU2NDA4OTkxNDUwNC5wbmciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.W_cmzd6frwnuf_p4_K40ME9cIai41bgUtrIImysmwaM")


planets.extend((sun,earth, mars,venus))
print("""May Trinh
Calculate velocity, grativational force, and new position of 3 planets (Earth,Mars,Venus) in regard to the Sun based on given formulas.
(1) p = p + vt + (1/2)a(t**2)
(2) v = v + at
(3) F = KM1M2/(r**2)
(4) a = F/m
""")

# add trails
for planet in planets:
    attach_trail(planet,color = vec(1,random(),random()), type='points',  interval=10, retain=100)

    
#calculate the gravitational force between two objects
def gForce(planets,j):
    G = 1                   #gravitational constant
    force = vec(0.0,0.0,0.0)
    for i in range(len(planets)):
        if(j != i):
            d_vec = planets[i].pos - planets[j].pos #distance between 2 planets
            d_mag = mag(d_vec)      #calculate the magnitude of the distance
            u_vec = d_vec / d_mag   #calculate the unit vector of the distance vector
            force_mag = (G*planets[i].mass*planets[j].mass)/d_mag**2 #calculate the force magnitude
            force_vec = force_mag * u_vec #calculate the force vector
            force += force_vec
    return force; 


dt = 0.0001
t = 0
while (t<3):   # this will make the simulation stop

    rate(1500)   # this limits the animation rate so that it won't depend on computer/browser processor speed
    for j in range(len(planets)):
         force = gForce(planets,j)
         planets[j].force = force
         planets[j].acceleration = planets[j].force/planets[j].mass
         planets[j].velocity = planets[j].velocity + planets[j].acceleration*dt
         planets[j].pos=planets[j].pos+planets[j].velocity*dt+(1/2)*planets[j].acceleration*(dt**2)
 
    t += dt
        


