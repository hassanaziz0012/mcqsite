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

        duration = request.GET.get('duration')
        if duration == "30":
            questions = test.questions.all().order_by('?')[0:15]
        elif duration == "60":
            questions = test.questions.all().order_by('?')[0:30]
        else:
            questions = test.questions.all().order_by('?')

        print(len(questions))

        return render(request, 'take_test.html', context={'test': test, 'questions': questions})
    