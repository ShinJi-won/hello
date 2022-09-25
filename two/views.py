from django.db.models import Count,Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from two.forms import FoodForm, ReviewForm, UpdateFoodForm
from two.models import Food, Review
from django.core.paginator import Paginator

def list(request):
    a=Food.objects.all().annotate(re_cnt=Count('review')).annotate(avg_score=Avg('review__score'))
    pa=Paginator(a,5) #한 페이지당 5개씩 출력
    p=request.GET.get('page') #page데이터 가져옴
    fo=pa.get_page(p) #

    con={'food':fo}
    return render(request,'two/list.html',con)

def make(request):
    if request.method=='POST':
        form=FoodForm(request.POST) #POST데이터들을 FoodForm에 담는다
        if form.is_valid():
            a=form.save()  #원래는 shell
        return HttpResponseRedirect('/two/list/')
    form=FoodForm()
    return render(request,'two/make.html',{'form':form})

def update(request):
    if request.method=='POST' and 'id' in request.POST:
        a=get_object_or_404(Food,pk=request.POST.get('id'))
        pw=request.POST.get("pw","")
        form=UpdateFoodForm(request.POST, instance=a) #수정대상 지정
        if form.is_valid() and pw==a.pw:
            a=form.save()

    elif 'id' in request.GET:
        a=get_object_or_404(Food,pk=request.GET.get('id'))
        form=FoodForm(instance=a)
        form.pw=''
        return render(request,'two/update.html',{'form':form})
    return HttpResponseRedirect('/two/list/')

def detail(request,id):
    if id is not None:
        a=get_object_or_404(Food,pk=id)
        re=Review.objects.filter(food=a).all()
        return render(request,'two/detail.html',{'a':a, 're':re})
    return HttpResponseRedirect('/two/list/')


def delete(request,id):
    a=get_object_or_404(Food,pk=id)
    if request.method=='POST' and 'pw' in request.POST:
        if a.pw==request.POST.get('pw'):
            a.delete()
            return redirect('list')
        return redirect('food-detail',id=id)
    return render(request,'two/delete.html',{'a':a})

def review_make(request,food_id):
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            n=form.save()
        return redirect('food-detail',id=food_id)

    a=get_object_or_404(Food,pk=food_id)
    form=ReviewForm(initial={'food':a})
    return render(request,'two/review_make.html',{'form':form, 'a':a})


def review_delete(request,food_id,review_id):
    a = get_object_or_404(Review,pk=review_id)
    a.delete()
    return redirect('food-detail',id=food_id)

def review_list(request):
    re=Review.objects.all().select_related()
    pa = Paginator(re,5)  # 한 페이지당 10개씩 출력
    p = request.GET.get('page')  # page데이터 가져옴
    fo = pa.get_page(p)

    con = {'re': fo}
    return render(request, 'two/review_list.html', con)
