from django import template

register = template.Library()

@register.filter
def persian_digits(text):
    persian_digit = "۰۱۲۳۴۵۶۷۸۹"

    for i_en in range(10):
        i_fa = persian_digit[i_en]
        text = text.replace(str(i_en), i_fa)

    return text
