import pygame as pg

# Inicio de la Biblioteca
pg.init()

# Seteo de la ventana
window = pg.display.set_mode((800,600))
pg.display.set_caption("Conceptos Basicos")

# Color de fondo (variable)
background = (0,0,0) # Negro
yellow = (255,255,0) # Amarillo
light_blue = (0, 179, 255)
light_green = (14, 255, 0)
fuchsia = (255, 0, 242)


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    window.fill(background)

    # Dibujando Figuras (Circulo)
    pg.draw.circle(window, yellow, (400,300), 50)
    pg.draw.rect(window, light_blue, (150, 400, 100,50))
    pg.draw.line(window, light_green, (100,100), (700,100), 3)

    # Vertices
    vertices = [(400,110),(350,200),(450,200)]

    pg.draw.polygon(window, fuchsia, vertices)

    pg.display.update()



pg.quit()
    