from django.shortcuts import reverse,redirect, get_object_or_404, Http404
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from webapp.models import Userinfo, Post
from webapp.form import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return self.model.objects.order_by('-created_at')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostForm


    def get_object(self, queryset = Post.objects.all()):
        object = super(PostUpdateView, self).get_object()

        if object.author == self.request.user:
            return object

        else:
            raise Http404()


    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author == request.user:
        post.delete()
        return redirect('webapp:post_list')
    else:
        return redirect('webapp:post_detail', post_id)