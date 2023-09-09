from django.db import models
from django.utils import timezone

# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    questions = models.ManyToManyField('Question', blank=True)

    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return f'<Test: {self.title}>'


class Question(models.Model):
    question = models.CharField(max_length=250)
    extra_information = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='question-images', null=True, blank=True)
    answers = models.ManyToManyField('Answer', blank=True, related_name='question_answers')
    correct_answers = models.ManyToManyField('Answer', blank=True, related_name='question_correct_answers')
    explanation = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.question
    
    def __repr__(self) -> str:
        return f'<Question: {self.question}>'


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answer_question')
    answer = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.answer
    
    def __repr__(self) -> str:
        return f'<Answer: {self.answer}>'
    