# I have created this file - Rakesh
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>Hello girls</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7&ab_channel=CodeWithHarry"> code with harry <a/>''')
#
# def about(request):
#     return HttpResponse('''<h1>This is our first link below in django</h1> <a href="https://www.google.com"> google link click here </a>''')

def index(request):
    return render(request,'index.html')
def analyze(request):
    # Get the text
    djtext=request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charactercounter=request.GET.get('charactercounter','off')
    print(djtext)
    # print(removepunc)
    if (removepunc=="on"):
        # print(removepunc)
        # print(djtext)
        # analyzed=djtext
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = " "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text':
            analyzed}
        djtext=analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)
    if (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Upper Case', 'analyzed_text':
            analyzed}
        djtext=analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char!="\n":
                analyzed=analyzed+char

        params = {'purpose': 'Removed NewLines', 'analyzed_text':
            analyzed}
        djtext=analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char

        params = {'purpose': 'Space Remover', 'analyzed_text':
            analyzed}
        djtext=analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (charactercounter=="on"):
        var=""
        analyzed=0
        for char in djtext:
            if char!=" ":
                var=var+char
                for i in range(len(var)):
                    analyzed=i+1
        params = {'purpose': 'Character Counter', 'analyzed_text':
            analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)
    if (removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charactercounter!="on"):
        return HttpResponse("Please select any operation try again")

    return render(request,'analyze.html',params)

def Home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')


# def capfirst(request):
#     return HttpResponse("capitalize first <a href='/'>back</a>")
#
# def newlineremove(request):
#     return HttpResponse("newline remove")
#
# def spaceremove(request):
#     return HttpResponse("space remove")
#
# def charcount(request):
#     return HttpResponse("char count")
#
