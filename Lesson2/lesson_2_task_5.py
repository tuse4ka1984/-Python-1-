def month_to_season (m):
         if m in [1, 2, 12]:
             return ('Зима')
         if m in [3, 4, 5]:
             return ('Весна')
         if m in [6, 7, 8]:
             return ("Лето")
         if m in [9, 10, 11]:
             return ("Осень")
         else:
             return ("Некорректный номер месяца")
         
print (month_to_season (1))
print (month_to_season (3))
print (month_to_season (6))
print (month_to_season (9))
print (month_to_season (18))