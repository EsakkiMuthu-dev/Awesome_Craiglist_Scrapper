from django.db.models.fields import DateTimeField
from django.http import response
from django.shortcuts import render
import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup
from . import models
 
BASE_URL = 'https://chennai.craigslist.org/d/services/search/?query={}'
# Create your views here.
def index(request):
    return render(request,'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_URL.format(quote_plus(search))
    page  = requests.get(final_url)
    soup = BeautifulSoup(page.text,'html.parser')
    final_postings=[]

    post_listings =soup.find_all('li',class_='result-row')
    for post in post_listings:
        post_title  = post.find('a',class_='result-title hdrlnk').text
        post_url =post.find('a')['href']
        image_url = requests.get(post_url)
    
        soup = BeautifulSoup(image_url.text,'html.parser')
        if soup.find('div',class_='slide first visible'):
            soup1 = soup.find('div',class_='slide first visible')
   
        
            image_url = soup1.find('img')['src']
            post_image = image_url
        else:
            post_image='https://images.unsplash.com/photo-1514081618247-f6fdfa22ed86?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=500&q=80'

        if post.find(class_='result-price'):
            post_price =post.find(class_='result-price').text
        else:
            post_price='N/A'
        final_postings.append((post_title,post_url,post_price,post_image))
  
    

    context = {
        'search':search,
        'final_postings': final_postings,
        
        
    }
    return render(request,'my_app/new_search.html',context)