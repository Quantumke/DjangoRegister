from django.shortcuts import render
import datetime
from django.shortcuts import redirect
from django.utils import timezone

from .forms import PostForm
# Create your views here.

def Post_new(request):
	if request.method=="POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post= form.save(commit=True)
			post.user = request.user
			post.published_date = timezone.now()
			post.save()
			
	else:
		form=PostForm()


	return render(request , 'index.html', {'form': form})
