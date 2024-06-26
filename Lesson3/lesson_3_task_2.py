from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79161234567"),
    Smartphone("Samsung", "Galaxy S21", "+79162345678"),
    Smartphone("Google", "Pixel 6", "+79163456789"),
    Smartphone("Xiaomi", "Mi 11", "+79164567890"),
    Smartphone("OnePlus", "9 Pro", "+79165678901")
]

for phone in catalog:
    print(phone)