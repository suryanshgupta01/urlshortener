from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import shortURL
from .forms import createnewshorturl
from datetime import datetime
import random, string 


def home(request):
    return render(request, "../templates/base.html")

def create(request):
    # return render(request, "../templates/create.html")
    if(request.method=='POST'):
        form=createnewshorturl(request.POST)
        if form.is_valid():
            og_website=form.cleaned_data['og_url'] 
            random_chars_list=list(string.ascii_letters) # character list of all  a-z and A-Z
            random_chars_list.extend(list(string.digits)) # character list of all  a-z and A-Z and 0-9
            random_string=''
            len=6

            for i in range(len):
                random_string+=random.choice(random_chars_list)

            while(shortURL.objects.filter(short_url=random_string).exists()):
                random_string=''
                for i in range(len):
                    random_string+=random.choice(random_chars_list)

            s=shortURL(short_url=random_string,og_url=og_website,date=datetime.now())           
            s.save()
            return render(request, "../templates/urlcreated.html",{'chars':random_string})
    else:
        form=createnewshorturl()

    return render(request, "../templates/create.html",{'form':form})


def redirect(request,url):
    shortobj=shortURL.objects.get(short_url=url)
    if not shortobj :
        return render(request, "../templates/404page.html")
    # return render(request, "../templates/redirect.html",{'obj':shortobj})
    return HttpResponseRedirect(shortobj.og_url)