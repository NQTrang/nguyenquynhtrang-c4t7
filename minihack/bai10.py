n = int(input("enter month"))
if n == 1 or n ==3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
    print("thang nay co 31 ngay")
elif n == 4 or n == 6 or n ==9 or n == 11:
    print("thang nay co 30 ngay")
elif n == 2:
    print("thang nay co 28 hoac 29 ngay")
else :
    print("ban tu hanh tinh nao den vay")
