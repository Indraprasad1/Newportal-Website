from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import News, Category, Comment
from Blog.models import Blog
from Blog.forms import Registration
from datetime import datetime, timedelta
from django.http import JsonResponse
# Create your views here.

def weekly_top_news(request):
    one_week_ago = datetime.today() - timedelta(days=7)
    weekly_top = News.objects.filter(
        add_time__gte=one_week_ago
    ).order_by('-views')[:5]
    
    print(f"Weekly top news count: {weekly_top.count()}")  # Debug print
    for news in weekly_top:
        print(f"News: {news.title}, Views: {news.views}, Date: {news.add_time}")
        
    return weekly_top

def Homepage(request):
    first_news=News.objects.first()
    three_news=News.objects.all().order_by('-id')[1:4]
    trend = News.objects.all().order_by('?')[:5]
    weekly_top = weekly_top_news(request)  # Get weekly top news
    four_news = News.objects.all().order_by('id')[:4] #Get four news
    data={
        'first_news': first_news,
        'three_news': three_news,
        'trend': trend,
        'weekly_top': weekly_top,  # Add to context
        'four_news': four_news # Add to content
    }
    return render(request,"index.html",data)

def category_page(request):
    news_ct = News.objects.all().order_by('id')[:10]
    data={
        'news_ct': news_ct
    }
    return render(request,"categori.html",data)

def Details(request,id):
    news=News.objects.get(pk=id)
    
    # filter weekly top news
    news.views += 1  # Increment view count
    news.save()      # Save the model
    
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        comments = request.POST['comments']
        Comment.objects.create(
            news=news,
            name=name,
            email=email,
            comments=comments
        )
        messages.success(request,'Comment Submitted but in moderation mode')
    
    category_id = request.GET.get('Category')
    if category_id:
        related_news = News.objects.filter(category__id=category_id).exclude(pk=id)
    else:
        related_news = News.objects.filter(category=news.category).exclude(pk=id)

    # Get approved comments (status=True) ordered by newest first
    al_comments = Comment.objects.filter(news=news, status=True).order_by('-id')
    
    data={
        'news': news,
        'related_news': related_news,
        'al_comments': al_comments
    }
    return render(request, 'details.html', data)

# Sub Category
def Fashion(request):
    # Get the Fashion category
    fashion_category = Category.objects.get(title="Fashion")  # Assuming your Fashion category is titled "Fashion"
    # Get all news items in the Fashion category
    fashion_news = News.objects.filter(category=fashion_category).order_by('-add_time')
    
    data = {
        'news': fashion_news,
        'category': fashion_category
    }
    return render(request, "category/fashion.html", data)


def lifestyle_page(request):
    lifestyle_category = Category.objects.get(title="Lifestyles")
    li_news = News.objects.filter(category=lifestyle_category).order_by('-add_time')
    data = {
        'news': li_news,
        'category': lifestyle_category
    }
    return render(request,"category/lifestyle.html",data)

def Travel(request):
    Travel_category = Category.objects.get(title="Travel")
    Tr_news = News.objects.filter(category=Travel_category).order_by('-add_time')
    data = {
        'news': Tr_news,
        'category': Travel_category
    }
    return render(request,"category/travel.html", data)

def Sports(request):
    sports_category = Category.objects.get(title="Sports")
    sport_news = News.objects.filter(category=sports_category).order_by('-add_time')
    data = {
        'news': sport_news,
        'category': sports_category
    }
    return render(request,"category/sports.html", data)

def Technology(request):
    tech_category = Category.objects.get(title="Technology")
    tech_news = News.objects.filter(category=tech_category).order_by('-add_time')
    data = {
        'news': tech_news,
        'category': tech_category
    }
    return render(request,"category/technology.html",data)



def About(request):
    return render(request,"about.html")

def LatestNews(request):
    return render(request,"latest_news.html")

def Contact(request):
    return render(request,"contact.html")

def Elements(request):
    return render(request,"elements.html")

def Blog_page(request):
    All_blog = Blog.objects.all()
    random = Blog.objects.all().order_by('?')[:10]
    data={
        'All_blog' : All_blog,
        'random' : random
    }
    
    return render(request,"blog.html",data)

def Blog_Details(request, id):
    detail_blog = Blog.objects.get(pk=id)
    recent = Blog.objects.all().order_by('id')[:10]
    data = {
        'detail_blog': detail_blog,
        'recent': recent 
    }
    return render(request,"single-blog.html",data)

def header(request):
    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Handle AJAX search request
        search_term = request.GET.get('alldata')
        if search_term:
            results = News.objects.filter(title__icontains=search_term).values('id', 'title')[:5]  # Adjust field names as needed
            return JsonResponse(list(results), safe=False)
    
    # Regular page load
    alldata = News.objects.all()
    data = {
        'alldata': alldata
    }
    return render(request, "header.html", data)

# User Login
def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    if request.method=="POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_page')
    else:
        form = Registration()
    form = Registration()
    context={
        'form' :form
    }
    return render(request, 'register.html',context)

    
        