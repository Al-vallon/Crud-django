from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm

# Create your views here.
def index(request):
    mem = Member.objects.all()
    return render(request, "index.html", {'mem': mem})

# Render view for add member
def add(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MemberForm()
    return render(request, 'add.html', {'form': form})

# Delete user
def delete(request, id):
    mem = get_object_or_404(Member, id=id)
    mem.delete()
    return redirect('/')

# Update member
def update_member(request, id):
    mem = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=mem)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MemberForm(instance=mem)
    return render(request, 'update.html', {'form': form,'updatemem': mem})
