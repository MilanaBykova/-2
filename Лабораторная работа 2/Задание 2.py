salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital=0
a=0
b=0
for x in range(1,11):
    if x==1:
        money_capital=spend-salary
        a +=money_capital
    else:
        spend=spend+spend*increase
        money_capital=spend-salary
        b+=money_capital
capital=a+b
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:",round(capital,2))
