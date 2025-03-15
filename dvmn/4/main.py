from PIL import Image

image = Image.open('4/monro.jpg')

red, green, blue = image.split()

crop1 = 100
crop2 = 50

first_red = red.crop((crop1, 0, red.width, red.height))
second_red = red.crop((crop2, 0, red.width - crop2, red.height))

first_blue= blue.crop((0, 0, blue.width - crop1, blue.height))
second_blue = blue.crop((crop2, 0, blue.width - crop2, blue.height))

green = green.crop((crop2, 0, green.width - crop2, red.height))

red = Image.blend(first_red, second_red, 0.5)
blue = Image.blend(first_blue, second_blue, 0.5)
green = Image.blend(green, green, 0.5)

image = Image.merge('RGB', (red, green, blue))
image.thumbnail((80, 80))
image.save('4/small.jpg')