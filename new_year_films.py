import random
import os
from PIL import Image

def new_year_films(n):
  for i in range(1, n + 1):
    DIR = 'films'
    with Image.open(os.path.join(DIR, random.choice(os.listdir(DIR)))) as img:
     display(img)
