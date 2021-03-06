from .models import BlogPost
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.urls import reverse

# Create your views here.
def index(request):
	template_name = 'base.html'
	return render(request, template_name)

def home(request):
    template_name = 'home.html'
    return render(request, template_name)

def posts(request):
    qs = BlogPost.objects.all()
    template_name = 'posts.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

def read_article(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'read_article.html'
    context = {'object': obj}

    # comment section
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            # return HttpResponseRedirect(reverse("read_article:",args=(slug)))
            return render(request, template_name, {'object':context['object'],
                                            'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'object':context['object'],
                                            'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def about_view(request):
    template_name = "about.html"
    return render(request, template_name)

# def search(request):
#     template_name = "posts.html"
#     query_set = BlogPost.objects.filter(title_icontains=query)
#     context = {'object_list': query_set}
#     return render(request, template_name, context)
    