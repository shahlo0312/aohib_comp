from django.urls import path
from .views import HomePage, addnewsview, SearchView, NewsDetailView, NewsDeleteView, NewsUpdateView, CategoryView, TagsView, UserView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('add-new/', addnewsview, name='add_new'),
    path('new/<int:pk>/', NewsDetailView.as_view(), name='new_detail'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='new_delete'),
    path('<int:pk>/update/', NewsUpdateView.as_view(), name='new_update'),
    path('search/', SearchView.as_view(), name='search'  ),
    path('category/<int:pk>/', CategoryView.as_view(), name='category'  ),
    path('tags/<int:pk>/', TagsView.as_view(), name='tags'  ),
    path('user/<int:pk>/', UserView.as_view(), name='user'  ),


    

    # path('search/', SearchView.as_view(), name='search'  ),

    
]