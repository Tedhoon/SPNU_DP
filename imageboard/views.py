from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView , DeleteView 
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse_lazy



def image(request):
    image = ImageBoard.objects.all().order_by('-id')

    return render(request, 'image.html' , {'images' : image })



def image_detail(request, image_id):
    image_detail = get_object_or_404(ImageBoard , pk = image_id)
    return render(request, 'image_detail.html' ,{'image_detail' : image_detail})





class ImagePost(CreateView):
     
    def get(self, request, *args, **kwargs):
        context = {'image_form': ImageForm()}
        return render(request, 'image_post.html', context)

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.instance.author = self.request.user
            form.instance.save()
            form.save()
            return HttpResponseRedirect(reverse_lazy('image'))
        return render(request, 'image_post.html', {'image_form': form})

# class PostLikeRedirect(RedirectView):
#     def get_redirect_url(self, *args , **kwargs):
#         slug = self.kwargs.get("slug") #이 안에 "pk값.. 8: 42"
        
#         obj = get_object_or_404(ImageBoard , slug=slug)
#         return obj.get_absolute_url()



def image_edit(request, image_detail_id):
    image_detail = get_object_or_404(ImageBoard , pk = image_detail_id)

    edit_image_form = ImageForm(instance = image_detail)

    if request.method == 'POST':
        edit_image_form = ImageForm(request.POST, request.FILES , instance = image_detail)
        
        if request.user != image_detail.author:
            raise Http404

        if edit_image_form.is_valid():
            edit_image_form.save()
            return redirect('image')


    return render(request, 'image_edit.html', {'edit_image_form' : edit_image_form ,'image_detail' : image_detail} )



class ImageDelete(DeleteView):

    model = ImageBoard
    success_url = reverse_lazy('image')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object() #이게 타이틀임
        self.author = self.get_object().author # 작성자 name

        if self.request.user == self.author:
            
            success_url = self.get_success_url()

            self.object.delete()
            return HttpResponseRedirect(success_url)

        else:
            raise Http404
    

