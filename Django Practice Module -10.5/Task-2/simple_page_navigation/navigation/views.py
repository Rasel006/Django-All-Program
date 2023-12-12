from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'About.html')
def contact(request):
    return render(request,'Contact.html')
def extra(request):
    return render(request,'Extra.html')
def services(request):
    return render(request,'Services.html')
def link_page(request):
    return render(request, 'Link_page.html')