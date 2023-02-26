# Imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from UrsinaLighting import LitObject,LitDirectionalLight
from ursina.prefabs.memory_counter import *

# Create app
app = Ursina()

# Terrain
t = Entity(
    model = Terrain("heightmap_ada", skip=10),
    scale = (1024, 75, 1024),
    texture = "colormap_ada"
)

t.collider = t.model

water = Entity(model=Plane(subdivisions=(6, 6)), color=rgb(184, 221, 247), scale=(1024, 1, 1024)) #collider="plane"
water.position = (0, 35, 0)

# LitObject(model='assets2/palm.obj', texture='assets2/palm.png', collider='mesh', position=(60, 15, 50), rotation=(0, 0, -25), scale=(2, 2, 2))

# sun = LitDirectionalLight(direction = Vec3(0.5, -0.6, 1))

# Misc
player = FirstPersonController()
player.position = (30, 105, 10)

scene.fog_color = color.gray
scene.fog_density = .005
Sky()
EditorCamera()
MemoryCounter()

# Run app
app.run()

# https://stackoverflow.com/questions/59867493/how-to-make-perlin-noise-color-gradient-generation-in-python-similar-to-the-nois
