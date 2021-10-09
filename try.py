a=int(input("Введите целое число:"))
b=int(input("Введите целое число:"))
c=int(input("Введите целое число:"))
d=int(input("Введите целое число:"))
if a>0 and b>0 and c>0 and d>0:
    def lokki(a, b, c, d):
     if c<d and a<b and a<c and b<d:
      return 'Да!'
     return 'Нет!' 
    print(lokki(a, b, c, d))
else: 
    print("Ошибка!")