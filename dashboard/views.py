from django.db.models.query import QuerySet
from .forms import BlogPostForm, BlogGenerateForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import BlogPost
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .utils import generate_blog_content

class BlogListView(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'index.html'
    context_object_name = 'post'

    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_post'] = True
        context['dashboard'] = True
        return context


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog_update.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogGenerate(FormView):
    form_class = BlogGenerateForm
    success_url = reverse_lazy('mypost')
    template_name = 'autogen.html'

    def form_valid(self, form):
        title = form.cleaned_data["title"]
        tone = form.cleaned_data["tone"]
        style = form.cleaned_data["style"]

        content = generate_blog_content(title, tone, style)

        post = BlogPost(title=title, author=self.request.user, content=content)
        post.save()
        return redirect(reverse_lazy("mypost"))
    
class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('mypost')