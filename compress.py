from PIL import Image

# img = Image.open('images/photo1.jpg').convert('L')
# img = img.resize((300, 500))
# img.thumbnail((300, 500))
# img = img.crop( (50,50, 150, 150) )
# img.save('images/new_photo1.jpg', quality=95) #0-95
#png file => quantize

# img = Image.open('images/photo1.png') #open as png, save as jpg.
# img.save('new_photo1.jpg', progressive=True) #progressive=True faster loading


import os
route = os.getcwd()
file_names = os.listdir(route + '/images')
print(file_names)

for i in file_names:
    img = Image.open(f'images/{i}')
    img.thumbnail((500, 2500))
    img.save(f'images/new_{i}')