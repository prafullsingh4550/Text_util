from django.http import HttpResponse
from django.shortcuts import render 

def index(request):

    # return HttpResponse("Hello Prafull")
    return render(request, 'index.html')

def analyze(request):
    # get the text 
    djtext= request.POST.get('text','default')
    # checkbox value
    dtext= request.POST.get('removepunc','off')
    capital= request.POST.get('capital','off')
    newline= request.POST.get('newline','off')
    space= request.POST.get('space','off')
    charcount= request.POST.get('charcount','off')
  
    
    analyzed= ""
    if dtext == "on":
        punctuations = '''!()-[]{};:'"\,<>.?/@#$%^&*_~'''
        analyzed= ""
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed+char

        params= {'purpose':'Remove Punctuation' , 'analyzed_text':analyzed}

    # analyze the text 
        djtext= analyzed
    
        # return render(request,'analyze.html', params)

    if (capital=="on"):
        analyzed= ""
        for char in djtext:
            analyzed= analyzed+char.upper()
            params= {'purpose':'Change to Uppercase' , 'analyzed_text':analyzed}

            djtext= analyzed

        # return render(request,'analyze.html', params)
    
    if (newline=="on"):
        analyzed= ""
        for char in djtext:
            if char!="\n" and char!= "\r":
                analyzed= analyzed+char
            params= {'purpose':'Removed new lines' , 'analyzed_text':analyzed}

            djtext= analyzed
        # return render(request,'analyze.html', params)

    if (space=="on"):
        analyzed= ""
        for index, char in enumerate(djtext):
            if not(djtext[index] ==" "and djtext[index+1]==" " ):
                analyzed= analyzed+char
            params= {'purpose':'Removed Extra Spaces' , 'analyzed_text':analyzed}

            

        return render(request,'analyze.html', params)

    # elif (charcount=="on"):
    #     analyzed= ""
    #     i = 0
    #     for char in djtext:
    #         i=i+1
    #         analyzed= "Total number of characters "+str(i)
    #         params= {'purpose':'Count of characters' , 'analyzed_text':analyzed}

    #         return render(request,'analyze.html', params)
    
    

    
    # else:
    #     return HttpResponse("Please select any one of these")
    return render(request,'analyze.html', params)
   
   
   
   
   
   
   
   
   
   
   
   
    # return HttpResponse("Hello Prafull removepunc")
# def capfirst(request):
#     return HttpResponse("Hello Prafull capfirst")

# def newlineremove(request):
#     return HttpResponse("Hello Prafull newlineremove")

# def spaceremove(request):
#     return HttpResponse("Hello Prafull spaceremove")

# def charcounter(request):
#     return HttpResponse("Hello Prafull charcounter")
