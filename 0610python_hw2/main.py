while True:
    number = int(input("Введи ціле число: "))

    original_number = number

    if number < 0:
        number = -number
        print("-", end="")

    if number == 0:
        print(0)
    else:
        while number > 0:
            digit = number % 10
            print(digit, end="")
            number //= 10

    print()
    print(f"Товє число: {original_number}")

    again = input("Хочещ спробувати ще раз? (так/ні): ")

    if again.lower() != "так":
        print("До зустрічі")
        break