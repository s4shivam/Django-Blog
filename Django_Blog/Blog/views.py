from django.shortcuts import render,get_object_or_404
#from django.http import HttpResponse
from Blog.models import BlogPost
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.


# def home(requests):
#     context = {
#         'posts' : BlogPost.objects.all()
#     }
#     return render(requests, 'Blog/home.html' ,context);

class PostListView(ListView):
    model = BlogPost
    template_name = 'Blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted_on']
    paginate_by = 6


class PostDetailView(DetailView):
    model = BlogPost


class UserPostListView(ListView):
    model = BlogPost
    template_name = 'Blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return BlogPost.objects.filter(author=user).order_by('-date_posted_on')





class PostCreateView(LoginRequiredMixin,CreateView):
    model = BlogPost
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = BlogPost
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = BlogPost
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(requests):
    return render(requests, 'Blog/about.html',{'title':'About'})
