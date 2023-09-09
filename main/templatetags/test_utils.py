from django import template

register = template.Library()

@register.filter(name="get_answers")
def get_answers(question):
    return list(question.answers.all().values_list('pk', flat=True))

@register.filter(name="get_correct_answers")
def get_correct_answers(question):
    return list(question.correct_answers.all().values_list('pk', flat=True))