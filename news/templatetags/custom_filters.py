from django import template

register = template.Library()

@register.filter(name = 'censor')


def censor(value):
    censor_list = ['редиска']
    text = value.split()
    for word in text:
        if word.lower() in censor_list:
            count = len(word) - 1
            value = value.replace(word, word[0] + '*' * count)
    return(value)