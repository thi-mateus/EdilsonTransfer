# shared/templatetags/custom_filters.py
from django.template import Library
from utils import datetime_utils

register = Library()


@register.filter
def format_date(date):
    return datetime_utils.format_date(date)


@register.filter
def format_time(time):
    return datetime_utils.format_time(time)


@register.filter
def format_datetime(datetime):
    return datetime_utils.format_datetime(datetime)


@register.filter
def weekday_name(date):
    return datetime_utils.weekday_name(date)


@register.filter
def cart_total_qtd(cart):
    return datetime_utils.cart_total_qtd(cart)


@register.filter
def toggle_direction(direction, column):
    return datetime_utils.toggle_direction(direction, column)


@register.filter
def get_attribute(obj, attr_name):
    return datetime_utils.get_attribute(obj, attr_name)


# Uso nos Templates:
# {% load custom_filters %}

# <p>Data de Embarque: {{ form.data_embarque|formatar_data }}</p>
# <p>Hora de Embarque: {{ form.hora_embarque|formatar_hora }}</p>
