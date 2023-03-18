import os
import random


# def get_random_image_path():
#     path = os.path.join('static', 'images')
#     images = os.listdir(path)
#     image_path = os.path.join(path, random.choice(images))
#     return image_path

cwd = os.getcwd()
print(cwd)

# folder_path = "/images"
# files = os.listdir(folder_path)

# for file in files:
#     print(file)

# Get the directory where the current script is located
dir_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(dir_path, 'static', 'images')
files = os.listdir(path)
# Print the directory path
print(files)

