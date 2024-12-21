from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout


from apps.users.forms import LoginForm

# def login(request):
#     return render(request, 'sign-in.html')

class LoginView(FormView):
    template_name = 'sign-in.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(
            request=self.request,
            username=data['username'],
            password=data['password']
        )
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('get_posts')
            return HttpResponse("<h1> User is not active </h1>")
        return HttpResponse("<h1> Invalid user data </h1>")


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("login")