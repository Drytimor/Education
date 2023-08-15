# выражения генераторы
# проходят один раз, не использую память
"""
num = (i for i in range(10, 21))
print(next(num)) 10
print(next(num)) 11
"""
"""
days = ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday']
gen = ((i, days[i%7])for i in range(1, 78))
for i in range(77):
    print(next(gen))
(1, 'Saturday')
(2, 'Sunday')
(3, 'Monday')
(4, 'Tuesday')
(5, 'Wednesday')
(6, 'Thursday')
(7, 'Friday')
"""

