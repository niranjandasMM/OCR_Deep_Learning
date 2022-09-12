from django.shortcuts import render
from django.shortcuts import redirect, render  
from .forms import ImagefieldForm
from .models import ImagefieldModel 

from PIL import Image
import numpy as np
# Create your views here.

def home(request):
    context = {}
    if request.method == "POST": 
        form = ImagefieldForm(request.POST, request.FILES) 
        if form.is_valid(): 
            name = form.cleaned_data.get("name") 
            img = form.cleaned_data.get("image_field") 
            obj = ImagefieldModel.objects.create( 
                                 title = name,  
                                 img = img 
                                 ) 
            obj.save() 
            img_obj = obj.img.instance
            print(f"uploaded data is : {obj, name}")
            image = Image.open(img)
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
            print(np.asarray(image))
            return render(request, "my_app/home.html", {"img_obj":img_obj,"name":name} )
    else: 
        form = ImagefieldForm()
        context['form'] = form
        return render( request, "my_app/home.html", context)  
    # return render(request, 'my_app/home.html')