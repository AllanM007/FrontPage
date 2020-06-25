import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

def scrape(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "http://web.mta.info/developers/turnstile.html"
  #content = session.get(url).text
  page = requests.get(url)
  #print(page.text[:500])

  html = page.text
  soup = BSoup(html, "html.parser")
  News = soup.findAll('a')

  for artcile in News:
    main = artcile.findAll('a')[:0]
    link = main['href']
    image_src = str(main.find('img')['srcset']).split(" ")[-4]
    title = main['title']
    new_headline = Headline()
    new_headline.title = title
    new_headline.url = link
    new_headline.image = image_src
    new_headline.save()
  return redirect("/")

def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news/home.html", context)