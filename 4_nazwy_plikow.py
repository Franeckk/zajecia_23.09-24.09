
def mnozenie(a, b, c):
    return round(a * b * c)

print(mnozenie(a= 54, b=3.323, c=4.3))

now = datetime.datetime.now()
moja_nazwa = now.strftime('Plik_%H%M%S.txt')

for i in range(10):
    print('moja nazwa to', moja_nazwa)
    time.sleep(2)