from django.urls import path, register_converter
from . import views as horoscope
from . import converters

# register_converter(converters.MyFloatConverter, 'my_float')
# register_converter(converters.SplitConvertor, 'my_split')
# register_converter(converters.UpperConvertor, 'my_upper')

urlpatterns = [
    path('<int:month>/<int:day>', horoscope.your_zodiac),
    path('type/<str:element>/', horoscope.type_elements, name='type-elements'),
    path('type/', horoscope.type_),
    path('', horoscope.index, name='horoscope-index'),
    path('<int:sing_zodiac>/', horoscope.info_num_horoscope),
    # path('<my_upper:sing_zodiac>/', horoscope.my_upper_converters),
    # path('<my_split:sing_zodiac>', horoscope.my_split_converter),
    # path('<my_float:sing_zodiac>/', horoscope.my_float_converters),
    path('<str:sing_zodiac>/', horoscope.info_sing_horoscope, name='horoscope-name'),
]
