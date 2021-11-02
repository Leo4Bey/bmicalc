kilo = float(input("Kilonuzu giriniz kg cinsinden: "))
boy = float(input("Boyunuzu giriniz cm cinsinden: "))

bmi = kilo / (boy / 100) ** 2 

if bmi >= 10 and bmi < 18.5:
    print(bmi)
    print("Zayıf")
elif bmi >= 18.5 and bmi < 25:
    print(bmi)
    print("Sağlıklı")
elif bmi >= 25 and bmi < 30:
    print(bmi)
    print("Kilolu")
elif bmi >= 30 and bmi < 40:
    print(bmi)
    print("Şişman")
elif bmi >=40 and bmi < 60:
    print(bmi)
    print("Obezite")
else:
    print("Lütfen geçerli değerler giriniz.")