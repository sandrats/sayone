from django.shortcuts import render
import datetime
from .models import Event,Category
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
def index (request):
    events = Event.objects.all().order_by('startDate')
    categories = Category.objects.all()

    p = Paginator(events, 10)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)


    username=None
    if request.session.has_key('logged_in'):
           logged_in = request.session.get('logged_in')
           if logged_in:
             username=request.session.get('username')
           
    else:
      request.session['logged_in'] = False
    return render(request,"event/index.html",{
        "events":page_obj,
        "categories":categories,
        "logged_in":logged_in,
        "username":username
    })
def filter (request):
  if request.method == "POST":
    startDate = request.POST["startDate"]
    endDate = request.POST["endDate"]
    categories = request.POST["categories"]
