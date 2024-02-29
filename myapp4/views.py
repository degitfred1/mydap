from django.shortcuts import render
from .models import song

def kan(request):
    who1=song.objects.filter(title='wish1')
    who2=song.objects.filter(title='wish2')
    return render(request,'index.html',{'who1':who1,'who2':who2})
