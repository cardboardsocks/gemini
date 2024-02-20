from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import Image

def image_upload(request):
   if request.method == 'POST':
       form = ImageUploadForm(request.POST, request.FILES)
       if form.is_valid():
           new_image = form.save(commit=False)
           new_image.uploader = request.user 
           new_image.save()
           return redirect('image_list')  # Redirect to the image list view
   else:
       form = ImageUploadForm()
   return render(request, 'upload.html', {'form': form})

   def image_list(request):
    images = Image.objects.all()
    return render(request, 'list.html', {'images': images})

