from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,  redirect, reverse
from django.views.generic import ListView, CreateView, DetailView, View
from django.views.generic.edit import DeleteView, UpdateView
from .models import News, Category, Tags
from django.urls import reverse_lazy
from .forms import AddNewsForms
from django.contrib.auth.decorators import login_required
from hitcount.views import HitCountDetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.contrib.auth.models import User




class HomePage(ListView):
    template_name = 'index.html'
    model = News

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        sport = News.objects.filter(category__name='Sports').order_by('-create_at')[:4]
        technology = News.objects.filter(category__name='Technology').order_by('-create_at')[:4]
        business = News.objects.filter(category__name='Business').order_by('-create_at')[:4]
        entertainment = News.objects.filter(category__name='Entertainment').order_by('-create_at')[:4]
        latest_news = News.objects.all().order_by('-create_at')[1:6]
        latest_new = News.objects.all().order_by('-create_at').first()
        # most_viewed_categorys = Category.objects.all().order_by('-get_hit_count')[4]
        # most_viewed_category = Category.objects.all().order_by('-get_hit_count').first()
        most_news = News.objects.all().order_by('-view_count')[:4]


        


        # all = News.objects.all()
        
        context = {
            'news_sport': sport,
            'news_technology': technology,
            'news_business': business,
            'news_entertainment': entertainment,
            'categorys': Category.objects.all(),
            'tags': Tags.objects.all(),
            'users': User.objects.all(),
            'latest_news': latest_news,
            'latest_new': latest_new,
            # 'most_viewed_categorys': most_viewed_categorys,
            # 'most_viewed_category': most_viewed_category,
            "most_news": most_news,


        }
        return context


@login_required
def addnewsview(request):
    if request.POST:
        form = AddNewsForms(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            # form.instance.slug = request.slug
            form.save()
            return redirect('add_new')

    context = {}
    context['form'] = AddNewsForms()
    return render(request, 'add_new.html', context)





class NewsDetailView(HitCountDetailView):
    model = News
    template_name = 'single_page.html'
    context_object_name = 'new_detail'
    count_hit = True

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        print("salom")
        return super().get(request, *args, **kwargs)

class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView ):
    model = News
    success_url = reverse_lazy('home')
    template_name = 'news_delete.html'

    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.user == self.request.user or self.request.user.is_superuser

class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = News
    form_class = AddNewsForms
    success_url = reverse_lazy('home')
    template_name = 'news_update.html' 

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        print(21)
        print(123)
        print(super().get_context_data(**kwargs))
        return super().get_context_data(**kwargs)
    

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("new_update", kwargs={"pk":pk})  
    
    

    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.user == self.request.user or self.request.user.is_superuser
    




class SearchView(ListView):
    template_name = "search.html"
    model = News
    
    def get_queryset(self):
        query = self.request.GET.get("search")
        object_list = News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        print(object_list)
        return object_list
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("search")
        return context
    

class CategoryView(View):
    
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        context = {
            "object_list": category.news_category.all(),
            "ctg_name": category.name,
            'categorys': Category.objects.all(),
            'users': User.objects.all(),
            'tags': Tags.objects.all(),

            # "news": News.objects.filter(category=category)

        }
        return render(request, "category.html", context)
    
class TagsView(View):

    def get(self, request, pk):
        tags = Tags.objects.get(id=pk)
        context = {
            "object_list": News.objects.filter(tags=tags).prefetch_related('tags'),
            "tag_name": tags.name,
            'tags': Tags.objects.all(),
            'categorys': Category.objects.all(),
            'users': User.objects.all(),



            # "news": News.objects.filter(category=category)

        }
        return render(request, "tags.html", context)
    
class UserView(View):
    
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        context = {
            "object_list": user.news_user.all(),
            "user_name": user.username,
            'users': User.objects.all(),
            'tags': Tags.objects.all(),
            'categorys': Category.objects.all(),



            # "news": News.objects.filter(category=category)

        }
        return render(request, "user.html", context)