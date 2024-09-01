from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def viewfirst(request):
    return HttpResponse ('<h1>Welcome to Django<h1>')

def viewsecond(request):
    card_title="Students"
    card_body="Alhera kids Haven, House building, Dattapara, Tongi, Gazipur."
    card_footer="Fine 123456"
    name = {'title': card_title,'body': card_body,'footer': card_footer}
    return render (request,'Customize_Setting/organization.html',name)