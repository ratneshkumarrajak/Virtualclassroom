from django.contrib.auth.models import User
from django.shortcuts import render,redirect, get_object_or_404
from ..forms import NewTopicForm
from ..models import Board, Topic, Post
from django.views.generic import TemplateView

def home(request):
    boards = Board.objects.all()
    if request.user.is_authenticated:
        return render(request, 'classroom/home.html', {'boards': boards})
    return render(request, 'classroom/homediscussion.html')
def board_topics(request):
    board = Board.objects.all()
    #board = get_object_or_404(Board)
    return render(request, 'classroom/topics.html',{'board':board})
def new_topic(request):
    
    #board = get_object_or_404(Board)
    board = Board.objects.all()
    #user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            #topic.board = board
            #topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                #created_by=user
            )
            return redirect('board_topics')  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'classroom/new_topic.html', {'board': board, 'form': form})
