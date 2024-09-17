from django.shortcuts import render, redirect
from .models import Member


# Create your views here.
def index(request):
    mem = Member.objects.all()
    return render(request, "index.html", {'mem': mem})

# render view for add member

def add(request):
    return render(request, 'add.html')

#post
def addpost(request):
    first = request.POST['first']
    last = request.POST['last']
    country = request.POST['country']

    newmem=Member(firstName=first, lastName=last, country=country)
    newmem.save()
    return redirect('/')


#delete user
def delete(request, id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect('/')

#update member
def update(request, id):
    updatemem=Member.objects.get(id=id)
    return render(request, 'update.html', {'updatemem': updatemem })

def up(request,id):
    upfirst=request.POST['first']
    uplast=request.POST['last']
    upcountry=request.POST['country']
    updatesave=Member.objects.get(id=id)
    updatesave.firstName=upfirst
    updatesave.lastName=uplast
    updatesave.country=upcountry

    updatesave.save()
    return redirect('/')

