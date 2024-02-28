from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import Image
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def like_image(request, image_id):
    if request.method == 'POST':
        image = get_object_or_404(Image, pk=image_id)
        image.num_up_vote += 1
        image.save()
        return JsonResponse({'updated_like_count': image.num_up_vote}) 
    else:
        # Handle non-AJAX requests if needed
        pass 

def dislike_image(request, image_id):
    if request.method == 'POST':
        image = get_object_or_404(Image, pk=image_id)
        image.num_down_vote += 1
        image.save()
        return JsonResponse({'updated_dislike_count': image.num_down_vote}) 
    else:
        # Handle non-AJAX requests if needed
        pass

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


