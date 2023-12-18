# from ursina import *
# a=Ursina(icon='textures/ursina.ico')
# Sky()
# b=Animation('assets\img',
#             collider='box',
#             scale=(2,2,2),
#             y=5)
# camera.orthographic=True
# camera.fov=20
# # def Update():
# #     b.y =b.y -4*time.dt
# # def keys(key):
# #     if key == 'space':
# #         b.y = b.y +3
# a.run()


import  random
a="b"
while a == "b":
    n=random.randint(1,6)
    if n == 1:
        print("[--------]")
        print("[        ]")
        print("[    0   ]")
        print("[        ]")
        print("[--------]")

    if n == 2:
        print("[--------]")
        print("[0       ]")
        print("[        ]")
        print("[       0]")
        print("[--------]")
    if n == 3:
        print("[--------]")
        print("[        ]")
        print("[0  0  0 ]")
        print("[        ]")
        print("[--------]")
    if n == 4:
        print("[--------]")
        print("[0     0 ]")
        print("[        ]")
        print("[0     0 ]")
        print("[--------]")
    if n == 5:
        print("[--------]")
        print("[0     0 ]")
        print("[   0    ]")
        print("[0     0 ]")
        print("[--------]")
    if n == 6:
        print("[--------]")
        print("[0  0  0 ]")
        print("[        ]")
        print("[0  0  0 ]")
        print("[--------]")
    a=input("press the key:")
    print("\n")