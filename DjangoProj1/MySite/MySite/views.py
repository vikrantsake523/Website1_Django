# this is the file i created - Viky
# 
import datetime
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('''<h2>Helloo</h2>
            <a href = "https://www.javatpoint.com/django-view"> Code In Style </a>''')

# def hello():
#     return "Hello"

def date_now(request):
    print(request.GET.get('text','dfault'))
    now = datetime.datetime.now()
    html_date = "<html><body><h3> Now the time is %s </h3></body></html>" %now
    return HttpResponse(html_date)

def analyzer(request):
    djtext = request.GET.get('text','Default')
    removepunc = request.GET.get('tick','TickOff')
    uppercase = request.GET.get('upper','TickOff')
    removenewlines = request.GET.get('removenew','TickOff')
    print(djtext,removepunc)
    if removepunc == "on":
        AnalayzedText = PunctuationRemover(djtext)
        params = {'purpose':': Removed Punctuations Text here','analyzed_text': AnalayzedText}
        print(AnalayzedText)
        return render(request,'analyze.html',params)
    elif (uppercase == "on"):
        AnalayzedText = Caps(djtext)
        params = {'purpose':': Uppercase Text here','analyzed_text': AnalayzedText}
        print(AnalayzedText)
        return render(request,'analyze.html',params)
    elif (removenewlines == "on"):
        AnalayzedText = removeNewLines(djtext)
        params = {'purpose':': Removed New Lines here','analyzed_text': AnalayzedText}
        print(AnalayzedText)
        return render(request,'analyze.html',params)
    else:
        params = {'purpose':': Not Removed Punctuations Text here','analyzed_text': djtext}
        return render(request,'analyze.html',params)

def removeNewLines(djtext):
    AnalayzedText = ''
    for char in djtext:
        if char != '\n':
            AnalayzedText += char
    return AnalayzedText


def Caps(text):
    return text.upper()

def PunctuationRemover(djtext):
    AnalayzedText = ''
    Punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    for char in djtext:
        if char not in Punctuation:
            AnalayzedText+=char
    return AnalayzedText

def index(request):
    #can also define parameters here and access it in urls. Specify 3rd parameter in return render
    params = {'name':'Larry','place':'USA'}
    return render(request, "index.html",params)
    