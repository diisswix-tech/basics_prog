while True:
    try:
        hour = int(input("Введи годину від 0 до 23: "))

        if hour < 0 or hour > 23:
            print("Такої години не існує. Спробуй ще раз.")
            continue

        if 0 <= hour <= 5:
            print("Ніч")
        elif 6 <= hour <= 11:
            print("Ранок")
        elif 12 <= hour <= 17:
            print("День")
        else:
            print("Вечір")

        again = input("Хочете перевірити ще одну годину? (так/ні): ")

        if again.lower() != "так":
            print("До зустрічі!")
            break

    except ValueError:
        print("Потрібно ввести число. Спробуйте ще раз.")