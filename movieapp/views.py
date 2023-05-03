from django.shortcuts import render,redirect
from . models import Movielist
from . forms import Updatemovielist

# Create your views here.
def home(request):
    movie=Movielist.objects.all()
    return render(request,"index.html",{'movie':movie})
def detail(request,movieid):
    movie=Movielist.objects.get(id=movieid)
    return render(request,"detail.html",{'movie':movie})
def add(request):
    if request.method== 'POST':
        name=request.POST.get('moviename')
        desc = request.POST.get('moviedesc')
        genre = request.POST.get('moviegenre')
        year = request.POST.get('movieyear')
        img = request.FILES['movieimg']
        movie=Movielist(name=name,desc=desc,genre=genre,year=year,img=img)
        movie.save()
        return redirect('/')

    return render(request,"add.html")

def update(request,id):
    movie=Movielist.objects.get(id=id)
    form=Updatemovielist(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form, 'movie':movie})

def genre(request,moviegenre):
    movie = Movielist.objects.filter(genre=moviegenre)
    return render(request, "genre.html", {'movie': movie})
