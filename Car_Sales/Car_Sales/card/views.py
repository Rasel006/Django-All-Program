from typing import Any
from . import forms
from django.shortcuts import redirect
from .import models
from django.views.generic import DetailView
from .models import Card
from django.contrib import messages
from author.models import Purchase
from django.contrib.auth.decorators import login_required


# Create your views here.

class DetailsPostView(DetailView):
    model = models.Card
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form= forms.CommentForm()
            
        context['comments']= comments
        context['comment_form']= comment_form
        return context

@login_required
def purchase(request,id):
    card = Card.objects.get(id=id)
    if card.quantity > 0:
            card.quantity -= 1
            card.save()
            purchase = Purchase.objects.create(user=request.user, car=card)
            
            messages.success(request, "Buy successfully")
            return redirect('profile')
    else:
            messages.error(request, "Car out of stock!")
            return redirect('profile')
        


           