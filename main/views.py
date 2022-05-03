from django.shortcuts import render


def showmain(request) :
    return render(request, 'main/mainpage.html')

def firstpage(request) :
    return render(request, 'main/firstpage.html')