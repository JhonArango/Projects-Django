from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
from comments.forms import CommentForm

# Create your views here.
def create_comment(request):
    form=CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.save()
        return redirect(comment.product.get_absolute_url())
    return HttResponseBadRequest()