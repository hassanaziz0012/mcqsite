from django.shortcuts import render, get_object_or_404
from django.views import View
from main.models import Question, Answer, Test

# Create your views here.
class HomeView(View):
    def get(self, request):
        tests = Test.objects.all()
        return render(request, 'home.html', context={'tests': tests})


class TakeTestView(View):
    def get(self, request, test_id: int):
        test = get_object_or_404(Test, pk=test_id)
        return render(request, 'take_test.html', context={'test': test})
    
