money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
svob=money_capital+salary-spend
month=0
while svob>0:
    spend=spend+spend*increase
    svob=svob+salary-spend
    month +=1
print("Количество месяцев, которое можно протянуть без долгов:", month)
