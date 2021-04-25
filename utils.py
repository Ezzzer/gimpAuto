def scale_crop(image, x, y):
    print image.width
    print image.height
    dx = 1.0
    dy = 1.0
    if image.width < x:
        dx = x / image.width
    if image.height < y:
        dy = y / image.height
    print dx, dy
    if dx > dy:
        image.scale(int(x), int(image.height * dx))
    else:
        image.scale(int(image.width * dy), int(y))
    center_x = image.width / 2
    center_y = image.height / 2
    print image.width
    print image.height
    image.crop(int(x), int(y), int(center_x - x / 2), int(center_y - y / 2))