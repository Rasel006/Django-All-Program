from django.shortcuts import render,redirect
from .import forms
# Create your views here.

# -------- Author ADD  Work ---------- 
def author(request):
    if request.method == 'POST':
        author_form = forms.AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('author')

    else:
        author_form = forms.AuthorForm()

    return render(request, 'bootstrap5/author.html',{'form': author_form})