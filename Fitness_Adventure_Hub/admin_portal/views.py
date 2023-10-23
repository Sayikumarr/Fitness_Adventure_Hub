from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Configuration,Activity,BlogPost

# Create your views here.

def index(request):
    try:
        # Retrieve the explore_more_url
        explore_more_url = Configuration.objects.get(key='explore_more_url').value
        # Retrieve the latest video URL and title
        latest_video_url = Configuration.objects.get(key='latest_video_url').value
        latest_video_title = Configuration.objects.get(key='latest_video_title').value
    except Configuration.DoesNotExist:
        # Handle the case where Configuration objects are not found
        explore_more_url = "default_explore_more_url"
        latest_video_url = "default_latest_video_url"
        latest_video_title = "default_latest_video_title"
    # Get the latest activities, sorted by modified_date in descending order
    latest_activities = Activity.objects.all().order_by('-id')
    # Get the latest blog posts, sorted by modified_date in descending order
    latest_blog_posts = BlogPost.objects.all().order_by('-id')
    context = {
        'explore_more_url': explore_more_url,
        'latest_video_url': latest_video_url,
        'latest_video_title': latest_video_title,
        'latest_activities': latest_activities,
        'latest_blog_posts': latest_blog_posts,
    }
    return render(request,'mainIndex.html',context)


def contactForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'contactSuccess.html')
    else:
        form = ContactForm()
    return render(request,'contactForm.html',{'form': form})


from django.shortcuts import render, get_object_or_404

def blogpost(request,pk):
    blog = get_object_or_404(BlogPost, id=pk)
    return render(request,'blogpost.html',{'blog': blog})