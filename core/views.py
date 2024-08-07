from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from dashboard.models import BlogPost
from .forms import CommentForm

class BlogListView(ListView):
    model = BlogPost
    template_name = 'index.html'
    context_object_name = 'post'

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.title = self.get_object()
            comment.user = self.request.user
            comment.save()

            return redirect('post-detail', pk=self.get_object().pk)
        else:
            # Handle invalid form submission (e.g., display errors)
            return self.render_to_response(self.get_context_data(object=self.object, form=form))