#!/usr/bin/python3

def kalkulator():
    print("Prosty kalkulator w Pythonie")
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    operacja = input("Wybierz operację (+, -, *, /): ")

    if operacja == "+":
        wynik = a + b
    elif operacja == "-":
        wynik = a - b
    elif operacja == "*":
        wynik = a * b
    elif operacja == "/":
        if b != 0:
            wynik = a / b
        else:
            print("Błąd: Dzielenie przez zero!")
            return
    else:
        print("Nieprawidłowa operacja!")
        return

    print(f"Wynik: {wynik}")

kalkulator()
