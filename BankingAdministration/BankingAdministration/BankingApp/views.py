from django.shortcuts import render
from django.views import View


class MainPageView(View):
    """Brief explanation on the purpose of the page with option to log in"""

    def get(self, request):
        return render(request, 'main_page.html')



