from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Complain
from django.db import connection
from psycopg2 import sql
from .models import Mins
from .models import Add

from django.utils import timezone

@login_required()
def getmins(request):
    results= Mins.objects
    return render(request, 'complain/create.html', {'results': results})

def getmins2(request):
    results= Mins.objects
    return render(request, 'complain/ministrypage.html', {'results': results})

def home(request):
    return render(request,'complain/home.html')

@login_required()
def mhome(request):
    current_user = request.user
    user_idd = current_user.first_name
    print(user_idd)
    cursor = connection.cursor()
    cursor.execute("call getaddressbyidministries('"+user_idd+"')")
    results = cursor.fetchall()
    print(results)
    complains = Complain.objects
    return render(request, 'complain/mhome.html', {'results': results, 'complains': complains})

def ministrypage(request):
    return render(request,'complain/ministrypage.html')
def aboutus(request):
    return render(request,'complain/aboutus.html')

@login_required()
def create(request):
    if request.method == 'POST':
        if request.POST['address'] and  request.POST['description'] and request.POST['ministry']  and request.FILES['image']:
            complain= Complain()
            complain.address= request.POST['address']
            complain.description = request.POST['description']
            complain.ministry = request.POST['ministry']
            add= Add.objects.create(address=request.POST['address'])
            complain.image = request.FILES['image']
            complain.pub_date = timezone.datetime.now()
            complain.user = request.user

            complain.save()
            return redirect('home')

        else:
            return render(request, 'complain/create.html', {'error': 'All fields are required'})

    else:
        results = Mins.objects
        return render(request, 'complain/create.html', {'results': results})


@login_required()
def detail(request,complain_id):
    complain=get_object_or_404(Complain,pk=complain_id)
    return render(request,'complain/detail.html',{'complain':complain})


@login_required()
def mdetail(request,complain_id):
    complain=get_object_or_404(Complain,pk=complain_id)
    return render(request,'complain/mdetail.html',{'complain':complain})

@login_required()
#def clist(reques0t, user_id):
def clist(request):
    current_user = request.user
    user_idd = current_user.username
    #print(user_id)
    cursor = connection.cursor()
    #cursor.callproc('lastweekcomplains')
    cursor.execute("call lastweekcomplains()")
    complain = cursor.fetchall()
    cursor.execute("call getaddressbyid('"+user_idd+"')")
    #cursor.execute("call getaddressSP()")
    results = cursor.fetchall()
    print(complain)
    print(results)
    return render(request, 'complain/clist.html', {'results': results, 'complains': complain})

@login_required()
def lastweek(request):
    current_user = request.user
    user_idd = current_user.username
    cursor = connection.cursor()
    cursor.execute("call last7days()")
    complain = cursor.fetchall()
    cursor.execute("call getaddressbyidlast7days('"+user_idd+"')")
    results = cursor.fetchall()
    print(complain)
    return render(request, 'complain/clist.html', {'results': results, 'complains': complain})

@login_required()
def last15days(request):
    current_user = request.user
    user_idd = current_user.username
    cursor = connection.cursor()
    cursor.execute("call last15days()")
    complain = cursor.fetchall()
    cursor.execute("call getaddressbyidlast15days('"+user_idd+"')")
    results = cursor.fetchall()
    print(complain)
    return render(request, 'complain/clist.html', {'results': results, 'complains': complain})

@login_required()
def lastmonth(request):
    current_user = request.user
    user_idd = current_user.username
    cursor = connection.cursor()
    cursor.execute("call lastmonth()")
    complain = cursor.fetchall()
    cursor.execute("call getaddressbyidlastmonth('"+user_idd+"')")
    results = cursor.fetchall()
    print(complain)
    return render(request, 'complain/clist.html', {'results': results, 'complains': complain})



@login_required()
def deletecomplain(request,complain_id):
    complain= get_object_or_404(Complain, pk=complain_id)
    if request.method=='POST':
        complain.delete()
        return redirect('clist')


#TAsfiar last addition

@login_required()
def approvecomplain(request,complain_id):
    complain = get_object_or_404(Complain, pk=complain_id)
    if request.method == 'POST':
        complain.dateApprove=timezone.now()
        complain.approve=True
        complain.save()
        return redirect('mhome')


def approvedlist(request):      #for ministry
    complains = Complain.objects.filter(approve__isnull=False).order_by('-dateApprove')
    return render(request, 'complain/approved.html', {'complains': complains})