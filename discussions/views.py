from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Discussion, Reply


# Discussions Home
def discussion_home(request):
    discussions = Discussion.objects.all().order_by('-date_posted')
    return render(request, 'discussions/discussions.html', {'discussions': discussions})


# Create New Discussion
def new_discussion(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        topic = request.POST.get('topic')
        content = request.POST.get('content')

        if title and content:
            Discussion.objects.create(
                title=title,
                topic=topic,
                content=content,
                author=request.user if request.user.is_authenticated else "Anonymous"
            )
            return redirect('discussions_home')

    return render(request, 'discussions/create_discussion.html')


# Discussion Detail Page
def discussion_detail(request, pk):
    discussion = get_object_or_404(Discussion, id=pk)

    # Handle reply submissions
    if request.method == 'POST':
        content = request.POST.get('reply_content')
        if content:
            Reply.objects.create(
                discussion=discussion,
                content=content,
                author=request.user if request.user.is_authenticated else "Anonymous"
            )
            return redirect('discussion_detail', pk=pk)

    return render(request, 'discussions/discussion_detail.html', {'discussion': discussion})
