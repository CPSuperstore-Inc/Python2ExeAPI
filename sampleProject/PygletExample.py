import pyglet

window = pyglet.window.Window()
window.set_caption('Pyglet Hello World')

label = pyglet.text.Label(
    'Hello World',
    font_name='Arial',
    font_size=70,
    x=window.width//2,
    y=window.height//2,
    anchor_x='center',
    anchor_y='center'
)


@window.event
def on_draw():
    window.clear()
    label.draw()


pyglet.app.run()
