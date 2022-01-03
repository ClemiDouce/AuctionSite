from django.shortcuts import redirect, render

from comment.models import Comment

from .forms import NewCommentForm

# Create your views here.
def comment_view(request):
    comments = Comment.objects.all()
    return render(request, "comment/comment_details.html", {'comments': comments})


def create_comment(request):
    """ Function to create a comment for an auction"""
    
    if request.method == "POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.save()
            return redirect('comment')
    else:
        form = NewCommentForm()        

    #form = NewCommentForm()
    return render(request, 'comment/create_comment.html', {'form': form})