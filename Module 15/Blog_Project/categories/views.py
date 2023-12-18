from django.shortcuts import render,redirect
from . import forms
# Create your views here.
# -------- Category ADD  Work ---------- 
def category(request):
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('category')

    else:
        category_form = forms.CategoryForm()

    return render(request, 'bootstrap5/category.html',{'form': category_form})