import turtle as ttl




leo = ttl.Turtle()

while True:
    pxl = int(input('Cuanto mover: '))
    leo.forward(pxl)
    leo.right(15)
    if pxl == 21:
        break

# ttl.done()
