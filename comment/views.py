from django.shortcuts import render

# Create your views here.
def comment_view(request):
    return render(request, "comment/comment_details.html")