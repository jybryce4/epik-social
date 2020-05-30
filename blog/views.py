from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.models import User
from .forms import CommentForm
from users.views import profile


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # newest posts first
    paginate_by = 15


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # newest posts first
    paginate_by = 15

    def get_queryset(self):
        # if user exists, this variable holds their name
        # otherwise, return 404 error
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # limit posts to user; order by latest posts
        return Post.objects.filter(author=user).order_by('-date_posted')
    

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # check if user is allowed to update the post (it must be their post)
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


# public user profile
def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'blog/public_profile.html', {'user': user})
