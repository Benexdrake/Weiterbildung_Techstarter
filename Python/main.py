def aufgabe1(_first_name:str, _last_name:str, _has_license:bool):
    first_name:str = _first_name
    last_name:str = _last_name
    has_license:bool = _has_license

    result = {"FirstName":first_name,"LastName":last_name,"License":has_license}
    print(f"Aufgabe1: {result}")
    print(f"Vorname: {first_name}\nNachname: {last_name}\nLizenz: {has_license}")


def aufgabe2(a:int, b:int):
    sum:int = a + b
    dif:int = a - b
    produkt = a * b
    quotient = a // b
    rest = a % b
    potenz = a ** b
    result = {"Summe":sum, "Differenz": dif, "Produkt": produkt, "Quotient": quotient, "Rest": rest, "Potenz": potenz}
    print(f"Aufgabe2: {result}")
    

def celsius_to_fahrenheit(c:int|float):
    result = 9/5 * c + 32
    print(f"Fahrenheit: {result}")


def price_to_tax(price:int|float):
    result = price * 1.19
    print(f"Price with Tax: {result}")


aufgabe1("BeneX","Drake",False)
aufgabe2(10,3)
celsius_to_fahrenheit(25)
celsius_to_fahrenheit(10)
price_to_tax(10)