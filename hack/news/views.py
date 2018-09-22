from django.shortcuts import render
import requests
import json


def fun(request):
	user1=requests.get("https://newsapi.org/v2/top-headlines?sources=the-hindu&apiKey=24ae132cc90546f781d40bfbf1c76420")
	user2=requests.get("https://newsapi.org/v2/everything?q=bitcoin&from=2018-08-21&sortBy=publishedAt&apiKey=24ae132cc90546f781d40bfbf1c76420")
	rep=user2.json()
	reps=user1.json()
	x='flood'
	y='fire'
	z='police'
	a='emergency'
	b='landslide'
	c='rape'
	d='storm'
	e='riots'
	f='raping'
	g='bomb'
	h='killed'
	arts=reps["articles"]
	print(arts)
	articles=[]
	images=[]
	for i in range(10):
		if x in arts[i]["description"] or x in arts[i]["content"]:
			print(arts[i]["description"])
			articles.append(arts[i]["description"])
			images.append(arts[i]["urlToImage"])
		elif y in arts[i]["description"] or y in arts[i]["content"]:
			print(arts[i]["description"])
			articles.append(arts[i]["description"])
			images.append(arts[i]["urlToImage"])
		elif z in arts[i]["description"] or z in arts[i]["content"]:
			print(arts[i]["description"])
			articles.append(arts[i]["description"])	
			images.append(arts[i]["urlToImage"])			
		elif a in arts[i]["description"] or a in arts[i]["content"]:
			print(arts[i]["description"])
			articles.append(arts[i]["description"])
			images.append(arts[i]["urlToImage"])
		elif b in arts[i]["description"] or b in arts[i]["content"]:
			print(arts[i]["description"])
			articles.append(arts[i]["description"])
			images.append(arts[i]["urlToImage"])
		elif c in arts[i]["description"] or c in arts[i]["content"]:
			print(arts[i]["description"])
			articles.append(arts[i]["description"])
			images.append(arts[i]["urlToImage"])
		elif d in arts[i]["description"] or d in arts[i]["content"]:
			print(arts[i]["description"])
			articles.append(arts[i]["description"])
			images.append(arts[i]["urlToImage"])
		elif e in arts[i]["description"] or e in arts[i]["content"]:
			print(arts[i]["description"])
			articles.append(arts[i]["description"])
			images.append(arts[i]["urlToImage"])
		elif f in arts[i]["description"] or f in arts[i]["content"]:
			print(arts[i]["description"])
			articles.append(arts[i]["description"])
			images.append(arts[i]["urlToImage"])
		elif g in arts[i]["description"] or g in arts[i]["content"]:
			print(arts[i]["description"])
			articles.append(arts[i]["description"])
			images.append(arts[i]["urlToImage"])
		elif h in arts[i]["description"] or h in arts[i]["content"]:
			print(arts[i]["description"])
			articles.append(arts[i]["description"])
			images.append(arts[i]["urlToImage"])					
		else:
			print ("not found")
	x='flood'
	y='fire'
	z='disaster'
	a='emergency'
	print (articles)
	print(images)
	leng=len(articles)
	print(leng)
	return render(request,'index.html',{'articles':articles,'images':images,'leng':leng})

'''def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=19d400636e536eec92b857df3a16ee37'
    city='Las Vegas'
    r=requests.get(url.format(city)).json()
    print(r)
    weat=[]
    temps=[]
    for ls in r:
    	if 'weather' in ls:
    		print(r[ls])
    		s=r[ls]
    		for i in r[ls]:
    			print(i["description"])
    			weat.append(i["description"])
    			weat.append(i["main"])

    	if 'main' in ls:
    		print(r[ls])
    		s1=r[ls]
    		for j in r[ls]:
    			if 'temp' in j:
    				print(s1[j])
    				temps.append(s1[j])
    return render(request,'index.html',{'weat':weat,'temps':temps})

def jd(request):

	url = 'http://www.justdial.com/autosuggest.php?'
	param = {
        'cases':'popular',
        'strtlmt':'24',
        'city':'Mumbai',
        'table':'b2c',
        'where':'',
        'scity':'Mumbai',
        'casename':'tmp,tmp1,24-24',
        'id':'2'
	}
	res = requests.get(url,params=param)
	r = res.json()
	print(r)
	return render(request,'index.html')


def gps(request):
	user00=requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670,151.1957&radius=500&types=food&name=cruise&key=AIzaSyBYzXj5wF4L6mChyyc5xwfb2QT1QEZ9VN8")
	r=user00.json()
	print(r)
	return render(request,'index.html')

def home(request):
	return render(request,'index.html')'''