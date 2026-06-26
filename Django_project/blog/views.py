from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts=[
   { "author":"Dishu pagli",
    "date_posted":"30 of apr,2007",
    "content":"Mein bhot gussa hu or meine line change krli h",
    "title":"1st blog"},

    { "author":"Yash",
    "date_posted":"2 of may,2007",
    "content":"second post made",
    "title":"2nd blog"}

]

def home(request):
    context={
        "posts":posts
    }
    return render(request,'blog/blog.html',context)
def about(request):
    return render(request,'blog/about.html')