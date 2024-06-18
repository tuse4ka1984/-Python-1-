год = 2024
def is_year_leap (год):
    if год % 4 == 0:
        return True
    else: 
        return False
результат = is_year_leap (год)
print (f'год {год}: {результат}')
    