from django.shortcuts import render
from django.shortcuts import redirect, render  
from .forms import ImagefieldForm
from .models import ImagefieldModel 

import cv2
import json
import base64
from PIL import Image
import numpy as np
# Create your views here.

def home(request):
    context = {}
    if request.method == 'POST' and request.FILES['image-input']:
        image = request.FILES['image-input']
        name = request.POST['name']
        print(f"uploaded data is : {image, name}")
        image = Image.open(image)
        image.save('upload.png')
        img = Image.open('upload.png')
        image = img.convert('L')
        image.save('upload.png')
        print(image.format)
        print(image.size)
        print(image.mode)
        # ------------------ convert image to array ------------------
        # PIL images into NumPy arrays
        numpydata = np.asarray(image)
        # <class 'numpy.ndarray'>
        print(type(numpydata))
        #  shape
        print(numpydata.shape)
        np_array = np.asarray(image)
        print(np_array)
        #****************************We finished taking input from user from web now we will pass the image to neural network to predict the digit**************************
        return redirect('home')
    else: 
        form = ImagefieldForm()
        context['form'] = form
        return render( request, "my_app/home.html", context)  
    

def canvas(request):
    if request.method == 'POST' :
        image = request.POST['image-input']
        # convert string to byte 
        image = bytes(image, 'utf-8')
        img_file = open('bash64.txt', 'wb')
        img_file.write(image)
        img_file.close()

        file = open('bash64.txt', 'rb')
        encoded_data = file.read()
        file.close()
        #decode base64 string data

        decoded_data = base64.b64decode((encoded_data))
        # write the decoded data back to original format in  file
        img_file = open('canvas.png', 'wb')
        img_file.write(decoded_data)
        img_file.close()
        # load image and g1et dimensions
        from PIL import Image
        im = Image.open("canvas.png")

        fill_color = (255,255,255)  # your new background color

        im = im.convert("RGBA")   # it had mode P after DL it from OP
        if im.mode in ('RGBA', 'LA'):
            background = Image.new(im.mode[:-1], im.size, fill_color)
            background.paste(im, im.split()[-1]) # omit transparency
            im = background

        im.convert("RGB").save("canvas.png")

        img = Image.open('canvas.png')
        image = img.convert('L')
        image.save('canvas.png')
        print(image.size)
        y_pred = 8
        context = {'y_pred': y_pred}
        print(f"predicted digit is : {y_pred}")

        numpydata = np.asarray(image)
        # <class 'numpy.ndarray'>
        print(type(numpydata))
        #  shape
        print(numpydata.shape)
        np_array = np.asarray(image)
        print(np_array)

        #****************************We finished taking input from user from web now we will pass the image to neural network to predict the digit**************************
        
        return render(request, 'my_app/canvas.html', context)

    return render(request, 'my_app/canvas.html')