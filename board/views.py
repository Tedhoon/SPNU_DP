from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# pagination
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView , DeleteView
# from django.views.generic import DetailView
from hitcount.views import HitCountDetailView

from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse_lazy

# from django.contrib import messages
from django.contrib.auth.models import User



def notice(request):
    notice = NoticeBoard.objects.all().order_by('-id')

    paginator = Paginator(notice , 10) #10페이지씩 자르기
    page = request.GET.get('page')
    posts = paginator.get_page(page) #request된 페이지를 담는다

    return render(request, 'notice.html' , {'notices' : notice , 'notice_posts' : posts})



class NoticeDetail(HitCountDetailView):
    model = NoticeBoard
    template_name = 'notice_detail.html'
    context_object_name = 'notice_detail'
    count_hit = True



class NoticePost(CreateView):
     
    def get(self, request, *args, **kwargs):
        context = {'notice_form': NoticeForm()}
        return render(request, 'notice_post.html', context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff: # staff 아닌 user는 글 못씀
            raise Http404
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.instance.author = self.request.user
            form.instance.save()
            form.save()
            # messages.info(request, '글이 등록 되었습니다!')
            return HttpResponseRedirect(reverse_lazy('notice'))
        return render(request, 'notice_post.html', {'notice_form': form})


NoitcePost = NoticePost.as_view()
NoticePost_permission = login_required(NoticePost)
#근데 어차피 로그인 안하면 anonymous user여서 글 등록 자체가 안된다...!



def notice_edit(request, notice_detail_id):
    notice_detail = get_object_or_404(NoticeBoard , pk = notice_detail_id)

    edit_notice_form = NoticeForm(instance = notice_detail)

    if request.method == 'POST':
        edit_notice_form = NoticeForm(request.POST , instance = notice_detail)
        
        if request.user != notice_detail.author:
            raise Http404

        if edit_notice_form.is_valid():
            edit_notice_form.save()
            return redirect('notice')


    return render(request, 'notice_edit.html', {'edit_notice_form' : edit_notice_form ,'notice_detail' : notice_detail} )



# def notice_delete(request , notice_detail_id):
#     notice_detail = get_object_or_404(NoticeBoard, pk = notice_detail_id)
    
#     notice_detail.delete()
#     return redirect('notice')
        
    # if self.request.user != notice_detail.author.username:
    #     msg = "권한이 없습니다"
    #     return HttpResponse(msg, status=404)

class NoticeDelete(DeleteView):

    model = NoticeBoard
    success_url = reverse_lazy('notice')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object() #이게 타이틀임
        self.author = self.get_object().author # 작성자 name

        if self.request.user == self.author:
            
            success_url = self.get_success_url()

            self.object.delete()
            return HttpResponseRedirect(success_url)

        else:
            raise Http404



# =========================================FreeBoard====================================================


def free(request):
    free = FreeBoard.objects.all().order_by('-id')

    paginator = Paginator(free , 10) #10페이지씩 자르기
    page = request.GET.get('page')
    posts = paginator.get_page(page) #request된 페이지를 담는다

    return render(request, 'free.html' , {'frees' : free , 'free_posts' : posts})



class FreeDetail(HitCountDetailView):
    model = FreeBoard
    template_name = 'free_detail.html'
    context_object_name = 'free_detail'
    count_hit = True



class FreePost(CreateView):
     
    def get(self, request, *args, **kwargs):
        context = {'free_form': FreeForm()}
        return render(request, 'free_post.html', context)

    def post(self, request, *args, **kwargs):
        form = FreeForm(request.POST)
        if form.is_valid():
            form.instance.author = self.request.user
            form.instance.save()
            form.save()
            return HttpResponseRedirect(reverse_lazy('free'))
        return render(request, 'free_post.html', {'free_form': form})


# FreePost = FreePost.as_view()
# FreePost_permission = login_required(FreePost)



def free_edit(request, free_detail_id):
    free_detail = get_object_or_404(FreeBoard , pk = free_detail_id)

    edit_free_form = FreeForm(instance = free_detail)

    if request.method == 'POST':
        edit_free_form = FreeForm(request.POST , instance = free_detail)
        
        if request.user != free_detail.author:
            raise Http404

        if edit_free_form.is_valid():
            edit_free_form.save()
            return redirect('free')


    return render(request, 'free_edit.html', {'edit_free_form' : edit_free_form ,'free_detail' : free_detail} )



class FreeDelete(DeleteView):

    model = FreeBoard
    success_url = reverse_lazy('free')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object() #이게 타이틀임
        self.author = self.get_object().author # 작성자 name

        if self.request.user == self.author:
            
            success_url = self.get_success_url()

            self.object.delete()
            return HttpResponseRedirect(success_url)

        else:
            raise Http404
    

    
