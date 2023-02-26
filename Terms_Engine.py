from ursina import *
# from constants import *
# from subprocess import call
import tkinter as tk
from tkinter import ttk
from tkinter import font
# from tkcode import CodeEditor
from tkinter import Tk
from tkinter import filedialog
import tkinter as tk
import sys
import os
import json
from PyQt5.QtWidgets import QWidget,QMainWindow,QTextEdit,QVBoxLayout,QApplication,QAction,QFileDialog,QInputDialog
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import pygame
from pygame.locals import *
#from constants import *
#from subprocess import call
#from subprocess import Popen
from ursina.prefabs.grid_editor import PixelEditor
from PIL import Image
from ursina import *
from ursina.shaders import basic_lighting_shader
from ursina.prefabs.memory_counter import *
from ursina.shaders import lit_with_shadows_shader
# from UrsinaLighting import LitObject,LitDirectionalLight
from ShaderLoader import load_shader

# call(["python", "code_editor.py"])

app = Ursina(vsync=False)
window.borderless = True
window.exit_button.enabled = True
input_handler.gamepad = True

# tse = input("Shader gir: ")
# 
# ts = load_shader(tse)
# 
# Entity.default_shader = ts # lit_with_shadows_shader 

print('Yüklemek İstediğiniz Model ve Material(Texture) Dosyasının içinde bulunduğu dosya yolunu yaz.')

model_isim1 = input("Objenin İsmi: ")
print(model_isim1 + "  M O D E L")
model = input(model_isim1 + "  Adlı Objenin Modelini Yükle: ")
texturepath = input(model_isim1 +  "  Adlı Objenin Dokusunu Yükle: ")
texture = load_texture(texturepath)
EditorCamera()
Entity(model=model, position=(0, 0, 0), rotation=(0, 120, 0), texture=texture, collider='mesh')


model_isim2 = input("Objenin İsmi: ")
print(model_isim2 + "  M O D E L")
model2 = input(model_isim2 + "  Adlı Objenin Modelini Yükle: ")
texturepath2 = input(model_isim2 + "  Adlı Objenin Dokusunu Yükle: ")
texture2 = load_texture(texturepath2)
EditorCamera()
Entity(model=model2, position=(5, 0, 0), texture=texture2, collider='mesh', scale=(0.1))  # collider='mesh'

model_isim3 = input("Objenin İsmi: ")
print(model_isim3 + "  M O D E L")
model3 = input(model_isim3 + "  Adlı Objenin Modelini Yükle: ")
texturepath3 = input(model_isim3 + "  Adlı Objenin Dokusunu Yükle: ")
texture3 = load_texture(texturepath3)
EditorCamera()
Entity(model=model3, position=(20, 0, 10), rotation=(0, 0, 0), texture=texture3, collider='mesh', scale=(0.1))

model_isim4 = input("Objenin İsmi: ")
print(model_isim4 + "  M O D E L")
model4 = input(model_isim4 + "  Adlı Objenin Modelini Yükle: ")
texturepath4 = input(model_isim4 + "  Adlı Objenin Dokusunu Yükle: ")
texture4 = load_texture(texturepath4)
EditorCamera()
Entity(model=model4, position=(10, 0, 10), rotation=(0, 180, 0), texture=texture4, collider='mesh', scale=(0.2))

# sun = LitDirectionalLight(direction = Vec3(0.5, -0.6, 1))

# model_isim5 = input("Objenin İsmi: ")
# print(model_isim5 + "  M O D E L")
# model5 = input(model_isim5 + "  Adlı Objenin Modelini Yükle: ")
# texturepath5 = input(model_isim5 + "  Adlı Objenin Material'ni Yükle: ")
# texture5 = load_texture(texturepath5)
# EditorCamera()
# Entity(model=model5, position=(10, 0, 0), texture=texture5, collider='mesh', shader=basic_lighting_shader)
# 
# model_isim6 = input("Objenin İsmi: ")
# print(model_isim6 + "  M O D E L")
# model6 = input(model_isim6 + "  Adlı Objenin Modelini Yükle: ")
# texturepath6 = input(model_isim6 + "  Adlı Objenin Material'ni Yükle: ")
# texture6 = load_texture(texturepath6)
# EditorCamera()
# Entity(model=model6, position=(28, 0, 0), rotation=(0, 0, 14), texture=texture6, collider='mesh', shader=basic_lighting_shader)
# 
# model_isim7 = input("Objenin İsmi: ")
# print(model_isim7 + "  M O D E L")
# model7 = input(model_isim7 + "  Adlı Objenin Modelini Yükle: ")
# texturepath7 = input(model_isim7 + "  Adlı Objenin Material'ni Yükle: ")
# texture7 = load_texture(texturepath7)
# EditorCamera()
# Entity(model=model7, position=(-5, 0, 4), rotation=(0, 90, 10), texture=texture7, collider='mesh', shader=basic_lighting_shader)
# 
# model_isim8 = input("Objenin İsmi: ")
# print(model_isim8 + "  M O D E L")
# model8 = input(model_isim8 + "  Adlı Objenin Modelini Yükle: ")
# texturepath8 = input(model_isim8 + "  Adlı Objenin Material'ni Yükle: ")
# texture8 = load_texture(texturepath8)
# EditorCamera()
# Entity(model=model8, position=(-5, 4, 2), texture=texture8, collider='mesh', shader=basic_lighting_shader)
# 
pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True)

# model2 = input("Model path: ")
# texturepath2 = input("Material path: ")
# texture2 = load_texture(texturepath2)
# EditorCamera()
# Entity(model=model2, texture=texture2)

# def buton():
#     model = input("Model path: ")
#     texturepath = input("Material path: ")
#     texture = load_texture(texturepath)
#     EditorCamera()
#     Entity(model=model, texture=texture)
#     
# b1 = Button(text='Load Mesh')
# 
# b1.on_click = buton

# b = Button(text='hello world!', color=color.azure, icon='sword', scale=.25, text_origin=(-.5,0))
# b.on_click = mesh_importer.resume    # assign a function to the button.
# b.tooltip = Tooltip('exit')


# code=input("New File Name : ")
# 
# root = tk.Tk()
# root.title("Terms Game Engine Code Editor")
# root.option_add("*tearOff", 0)
# 
# 
# notebook = ttk.Notebook(root)
# tab_1 = ttk.Frame(notebook)
# notebook.add(tab_1, text=code+'.py')
# notebook.pack(fill="both", expand=True)
# 
# code_editor = CodeEditor(
#     tab_1,
#     width=99,
#     height=30,
#     language="python",
#     background="black",
#     highlighter="dracula",
#     font="Consolas",
#     autofocus=True,
#     blockcursor=True,
#     insertofftime=0,
#     padx=10,
#     pady=10,
#     
# )
# code_editor.pack(fill="both", expand=True)
# code_editor.content = """print("Hello World")"""
# root.update()
# root.minsize(root.winfo_width(), root.winfo_height())
# root.mainloop()




#player = Entity(model='cube', color=color.orange, scale_y=2)

txt007 = Text(text="Oyuncu/Editor Moduna Geçmek İçin TAB Tuşuna Basınız.",
              color = color.black,
              scale = 1.60,
              rotation = (45, 30),
              position = (-0.6, 0.5)
              )

# col033 = Entity(model=model4,
#                 texture=texture3,
#                 collider='box',
#                 scale=100,
#                 alpha=.2,
#                 visible=False)

hit_plane = Entity(model='plane', collider='box', scale=100, alpha=.2, visible=False)

#terrain = Entity(model=Terrain('desert_terrain_heightmap'), scale=128)

cursor = Entity(model='box', color=color.azure, scale=1)

#terrain = Mesh()

vertices, triangles = list(), list()
uvs = list()
# self.normals = list()
w, h = 50,50
# self.height_values = [[j/255 for j in i] for i in self.height_values]


centering_offset = Vec2(-.5, -.5)
# centering_offset = Vec2(0, 0)
# if self.aspect_ratio > 1: # offset should be different if the terrain is not 1:1
#     centering_offset.x *= self.aspect_ratio
# else:
#     centering_offset.y /= self.aspect_ratio

min_dim = min(w, h)

from ursina.shaders import lit_with_shadows_shader
terrain = Entity(model=Mesh(vertices=[], triangles=[], uvs=[], colors=[]), scale=(w,1,h), y=-.01, texture='grass', collider='sphere')
terrain.scale *= 2




# create the plane
i = 0
for z in range(h):
    for x in range(w):
        terrain.model.vertices.append(Vec3((x/min_dim)+(centering_offset.x), 0, (z/min_dim)+centering_offset.y))
        terrain.model.uvs.append((x/w, z/h))

        if x > 0 and z > 0:
            terrain.model.triangles.append((i, i-1, i-w-1, i-w-0))

        i += 1

#terrain.model.colors = [color.green for v in terrain.model.vertices]
terrain.model.generate()

terrain.model.height_values =[[0 for x in range(w)] for y in range(h)]
from ursina.prefabs.first_person_controller import FirstPersonController #PLAYER İÇİN

ec = EditorCamera(rotation_smoothing=2, enabled=1, rotation=(30,30,0))
player = FirstPersonController() #BU SADECE KARAKTER GİBİ İLERLEMEK İÇİN VAR   #model='assets/charachter', texture='assets/cha.png', collider='mesh'

# def generate_normals_for_heightmap

strength = 5
# def update():
#     if mouse.world_point:
#         cursor.position = mouse.world_point
# 
#         if mouse.left:
#             x = int(cursor.x/(terrain.scale_x/w) + w/2)
#             z = int(cursor.z/(terrain.scale_z/h) + h/2)
#             # print(cursor.position / 128)
#             i = (z*(w)) + x
#             # print(x, z, i)
#             if x >= 0 and x+1 < w and z >= 0 and z+1 < h:
#                 # terrain.model.vertices[i] += Vec3(0, strength*time.dt, 0)
#                 # terrain.model.vertices[i+1] += Vec3(0, strength*time.dt, 0)
#                 # terrain.model.vertices[i+h+1] += Vec3(0, strength*time.dt, 0)
#                 # terrain.model.vertices[i+h+1+1] += Vec3(0, strength*time.dt, 0)
# 
#                 terrain.model.height_values[x][z] += strength*time.dt
#                 terrain.model.height_values[x+1][z] += strength*time.dt
#                 terrain.model.height_values[x][z+1] += strength*time.dt
#                 terrain.model.height_values[x+1][z+1] += strength*time.dt
# 
#                 # terrain.model.colors[i] = terrain.model.colors[i].tint(-.05)
#                 # terrain.model.vertices
# 
#                 terrain.model.vertices = []
#                 for z, column in enumerate(terrain.model.height_values):
#                     for x, row in enumerate(column):
#                         terrain.model.vertices.append(Vec3(x/w, terrain.model.height_values[x][z], z/h) + Vec3(centering_offset.x, 0, centering_offset.y))
# 
# 
# 
#                 terrain.model.generate()
# 
# 
#     pos = cursor.get_position(relative_to=terrain) + Vec3(.5,0,.5)
#     if pos.x >= 0 and pos.x < 1 and pos.z >= 0 and pos.z < 1:
#         pos *= Vec3(w,0,h)
#         # print(int(pos.x), int(pos.z))
#         cursor.y = terrain.model.height_values[int(pos.x)][int(pos.z)]
#         x, _, z = pos
#         # print(floor(x), floor(z))
# 
#         height_values = terrain.model.height_values
#         point =     height_values[int(floor(x))][int(floor(z))]
#         point_e =   height_values[int(min(w-1, ceil(x)))][int(floor(z))]
#         point_n =   height_values[int(floor(x))][int(min(h-1, ceil(z)))]
#         point_ne =  height_values[int(min(w-1, ceil(x)))][int(min(h-1, ceil(z)))]
# 
#         u0v0 = point * (ceil(x) - x) * (ceil(z) - z) # interpolated (x0, z0)
#         u1v0 = point_e * (x - floor(x)) * (ceil(z) - z) # interpolated (x1, z0)
#         u0v1 = point_n * (ceil(x) - x) * (z - floor(z)) # interpolated (x0, z1)
#         u1v1 = point_ne * (x - floor(x)) * (z - floor(z)) # interpolated (x1, z1)
# 
#         _h = u0v0 + u1v0 + u0v1 + u1v1  #estimate
#         cursor.y = _h * terrain.scale_y

def input(key):
    if key == 'tab':    # Editor/Player Mod için tab tuşunu atadık
        ec.enabled = not ec.enabled
        player.enabled = not player.enabled

Sky()
MemoryCounter() #GPU VE RAM'İN HAFIZASINI ÖLÇER VE EKRANA YANSITIR.

AmbientLight().look_at(Vec3(-.5,-1,-1))

from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

DropdownMenu('Dosya', buttons=(
        DropdownMenuButton('Yeni'),
        DropdownMenuButton('Aç'),
        DropdownMenu('Proje Aç', buttons=(
            DropdownMenuButton('Proje 1'),
            DropdownMenuButton('Proje 2'),
            )),
        DropdownMenuButton('Kaydet'),
        DropdownMenu('Ayarlar', buttons=(
            DropdownMenuButton('a Ayarları'),
            DropdownMenuButton('b Ayarları'),
            )),
        DropdownMenuButton('Çıkış'),
        ))

# import imgui
# 
# imgui.begin("Scrollale regions with flags")
# 
# imgui.begin_child(
#     "Child 1", height=70, border=True,
#     flags=imgui.WINDOW_ALWAYS_HORIZONTAL_SCROLLBAR
# )
# imgui.text("inside region 1")
# imgui.end_child()
# 
# imgui.begin_child(
#     "Child 2", height=70, border=True,
#     flags=imgui.WINDOW_ALWAYS_VERTICAL_SCROLLBAR
# )
# imgui.text("inside region 2")
# imgui.end_child()
# 
# imgui.end()

# exec(open('game_engine_tool1.py').read())
#  
# sys.exit(app.exec_())

app.run()
