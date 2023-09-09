from django.contrib import admin
from .models import Test, Question, Answer

# Register your models here.
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['title', 'questions_count']

    def questions_count(self, test):
        return test.questions.count()

    class Meta:
        model = Test


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'test', 'answers', 'correct_answers']

    def answers(self, question):
        return question.answers.count()
    
    def correct_answers(self, question):
        return question.correct_answers.count()
    

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'question', 'test']

    def test(self, answer):
        return answer.question.test
