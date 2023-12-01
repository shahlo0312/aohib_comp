from django.shortcuts import render
from .forms import RegistrationForm
from django.views.generic import CreateView, ListView, UpdateView, View
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserUpdateForm
from django.contrib.auth.models import User



class RegistrationView(CreateView):
    template_name = 'registration/registr.html'
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('home')


class MyProfileView(LoginRequiredMixin,View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        context = {
            'user': user
        }
        return render(request, "user/my_profile.html", context)
    

class MyProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "user/user_update.html"
    success_url = reverse_lazy("home")
    
    def test_func(self):
        new = self.get_object()
        if self.request.user == new.user or self.request.user.is_superuser:
            return True
        return False
    
		