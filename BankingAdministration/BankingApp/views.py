from django.shortcuts import render
from django.views import View
from forms import LoginForm


class MainPageView(View):
    """Brief explanation on the purpose of the page with option to log in"""

    def get(self, request):
        return render(request, 'main_page.html')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            pass


