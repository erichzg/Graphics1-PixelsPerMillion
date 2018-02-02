def pixelRule(x, y):
    r = x + y
    g = 499 + y - x
    b = 499 + x - y
    return str(r) + ' ' + str(g) + ' ' + str(b) + '\n'
        


def produceImage(name):
    imageFile = open(name + '.ppm', 'w')
    imageFile.write('P3\n500 500\n998\n')
    for y in range(0, 500):
        for x in range(0, 500):
            imageFile.write(pixelRule(x, y))
    return

produceImage('image')

