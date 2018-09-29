from django.http import HttpResponse
from django.shortcuts import render
import operator

def about(request):
    #return HttpResponse("Hello")
    return render(request,'about.html')

def homepage(request):
    #return HttpResponse("Hello")
    return render(request,'home.html')

def count(request):
    #return HttpResponse("Hello")
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    count = len(wordlist)
    #print(fulltext)

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    #print((sortedwords))
    return render(request,'count.html',{'fulltext':fulltext,"count":count,"worddictionary":sortedwords})

# def eggs(request):
#     return HttpResponse("<h1>EGGS</h1>")