from django.shortcuts import render, get_object_or_404
from django.views import View
from main.models import Question, Answer, Test
from collections import Counter

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

        return render(request, 'take_test.html', context={'test': test, 'questions': questions})
    

class TestStatsView(View):
    def get(self, request, test_id: int):
        test = get_object_or_404(Test, pk=test_id)
        test_questions = test.questions.all().values_list('pk', flat=True)
        correct_answer_pks_unformatted = [list(question.correct_answers.all().values_list('pk', flat=True)) for question in test.questions.all()]
        correct_answer_pks = []
        for pk_list in correct_answer_pks_unformatted:
            for pk in pk_list:
                correct_answer_pks.append(pk)

        test_answers = Answer.objects.filter(pk__in=correct_answer_pks).values_list('answer', flat=True)
        counts = dict(Counter(test_answers))
        result = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
        return render(request, 'stats_table.html', context={'test_title': test.title, 'counts': result})