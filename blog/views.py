from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from .models import Post, Tag
from .utils import DetailMixin, CreateMixin, UpdateMixin, DeleteMixin
from .forms import TagForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.db.models import  Q

class PostList(View):
    def get(self, request):
        search_query = request.GET.get('search', '')

        if search_query:
            posts = Post.objects.filter(Q(title__contains=search_query) | Q(text__contains=search_query))
        else:
            posts = Post.objects.all()

        paginator = Paginator(posts, 1)

        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        # есть ли другие страницы
        is_paginated = page.has_other_pages()
        # есть ли пред. стр
        if page.has_previous():
            prev_url = f'?page={page.previous_page_number()}'
        else:
            prev_url = ''
        # есть ли след. стр
        if page.has_next():
            next_url = f'?page={page.next_page_number()}'
        else:
            next_url = ''

        context = {
            'posts': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url,
        }

        return render(request, 'blog/posts_list.html', context=context)


class PostDetail(DetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
    # def get(self, request, slug):
    #     # post = Post.objects.get(slug__iexact=postname)
    #     post = get_object_or_404(Post, slug__iexact=slug)
    #     return render(request, 'blog/post_detail.html', context={'post': post})


class PostCreate(LoginRequiredMixin, CreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = True

    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'blog/post_create_form.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = PostForm(request.POST)
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'blog/post_create_form.html', context={'form': bound_form})


class PostUpdate(LoginRequiredMixin, UpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, DeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'post_list_url'
    raise_exception = True


class TagList(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'blog/tag_list.html', context={'tags': tags})


class TagDetail(DetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

    # def get(self, request, slug):
    #     # tag = Tag.objects.get(slug__iexact=tagname)
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     return render(request, 'blog/tag_detail.html', context={'tag': tag})


class TagCreate(LoginRequiredMixin, CreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True

    # def get(self, request):
    #     form = TagForm
    #     return render(request, 'blog/tag_create.html', context={'form': form})
    #
    #
    # def post(self, request):
    #     bound_form = TagForm(request.POST)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_create.html', context={'form': bound_form})


class TagUpdate(LoginRequiredMixin, UpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
    raise_exception = True

    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(instance=tag)
    #     return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(request.POST, instance=tag)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})


class TagDelete(LoginRequiredMixin, DeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tag_list_url'
    raise_exception = True

    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     return render(request, 'blog/tag_delete_form.html', context={'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     tag.delete()
    #     return redirect(reverse('tag_list_url'))
