from django import template
import math
register = template.Library()

@register.simple_tag
def cal_sellprice(price, discount):
    if discount is None or discount is 0:
        return price
    sellprice = price
    sellprice = price - ( price * discount * 0.01 )
    return math.floor(sellprice)

@register.filter
def dollar(price):
    return f"${price}"
