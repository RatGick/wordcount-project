from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def dinosaur(request):
    return HttpResponse('Yey, you have found a Dinosaur page!')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    dictionary = {}
    for word in wordlist:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    sortedlist = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    # In order to see the data format. Printing in terminal
    print(dictionary.items())
    print(sortedlist)
    return render(request, 'count.html', {'fulltext':fulltext, 'number':len(wordlist), 'worddictionary': sortedlist})


def about(request):
    return render(request, 'about.html')