from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from .models import Post, Tag
from .utils import DetailMixin, CreateMixin, UpdateMixin, DeleteMixin
from .forms import TagForm, PostForm


class PostList(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/posts_list.html', context={'posts': posts})


class PostDetail(DetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
    # def get(self, request, slug):
    #     # post = Post.objects.get(slug__iexact=postname)
    #     post = get_object_or_404(Post, slug__iexact=slug)
    #     return render(request, 'blog/post_detail.html', context={'post': post})


class PostCreate(CreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'

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


class PostUpdate(UpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'


class PostDelete(DeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'post_list_url'


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


class TagCreate(CreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


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


class TagUpdate(UpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'

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


class TagDelete(DeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tag_list_url'

    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     return render(request, 'blog/tag_delete_form.html', context={'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     tag.delete()
    #     return redirect(reverse('tag_list_url'))
