from io import StringIO
from typing import no_type_check_decorator
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index2.html')
#   var="this is a string"
#   return HttpResponse(f"this is about ` <a href='/'> back </a> {var} ")


def analyze(request):
    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    charcount=request.POST.get('charcount', 'off')
    uppercase_text=request.POST.get('uppercase_text', 'off')
    remove_spaces=request.POST.get('remspaces', 'off')
    capitilzed=request.POST.get('capitlized', 'off')
    remove_new_line=request.POST.get('new_line_remove', 'off')
    
    analyzed=""  # variable to store text value 
    
    # remove punctuations 
    punctuations='[]{}.:;'
    if removepunc=='on':
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
    else:
        analyzed=djtext   

    # count characters in a string 
    if charcount=='on':
        characters=''
        string=''
        for i in analyzed:
            if i not in characters:
                characters+=i
        for char in characters:
            string+=f"\'{char}\'={str(analyzed.count(char))}, "
    else:
        string=''

    # remove extra spaces 
    if remove_spaces=='on':
        rm_space=''
        for i,char in enumerate(analyzed):
            if not(char==' ' and analyzed[i+1]==' '):
                rm_space+=char
        analyzed=rm_space
        
    # capitilzed the text 
    if capitilzed == 'on':
        analyzed = analyzed.title()
   
    # uppercase the text 
    if uppercase_text=="on":
        analyzed=analyzed.upper()

    # remove new lines 
    if remove_new_line =="on":
        rm_new_line=''
        for char in analyzed:
            if char != "\n" and char !='\r':
                rm_new_line+=char
        analyzed=rm_new_line
   
    params={'purpose':['remove punctuations','count characters'],'analyzed_text':analyzed,'char_count':string}
    return render(request,'analyze.html',params)

def about(request):
    return render(request ,'about.html')
def contact(request):
  
    return render(request ,'contact.html')