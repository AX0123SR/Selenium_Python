from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d")
print("d1 =", int(d1))
print(type(d1))

for i in d1:
    if i.text == d1-1:
        i.click()
    break
print(type(i))