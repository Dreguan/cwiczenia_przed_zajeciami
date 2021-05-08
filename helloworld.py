message = "Hello"
message = message + " World "
print(message * 3)

a = 1.5
b = 0.5
print(a+b)
print(a*b)
print(a/b)
a = 2
b = 3
print(a ** b)
print(b % a)

print(1 == 2)
a = 1
b = 2
print(a == 1)
print(a != b)

print("1"+"2")
print(int("1")+int("2"))
print(bool(1))
print(str(12))

print("Jest to {} linia programu".format(26))
print("Jest to {} linia programu, w której występuje słowo '{}'".format(27, "słowo"))
print("Jest to {line} linia programu, w której drukujemy słowo '{word}'. Koniec linii {line}".format(line=28, word="Hello"))

print("Jak masz na imię?")
user_name = input()
print("Twoje imię to {}".format(user_name))
print("Ile masz lat?")
age = int(input())
print("Twój wiek to {}".format(age))
