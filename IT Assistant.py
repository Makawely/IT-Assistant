#Название программы
name_prog = "================== \nIT ASSISTANT v0.2 \n=================="

print()
print(name_prog)

print()

name = input("Введите ваше имя: ")
print()
print("Здравствуйте", name + "!")

print()

info_pc = "1. Информация о компьютере"
check_net = "2. Проверка интернет-соединения"
net_set = "3. Сетевые настройки"
exit_menu = "4. Выход"



while True:
    print(info_pc)
    print(check_net)
    print(net_set)
    print(exit_menu)

    print()

    choice = int(input("Выберите действие: "))

    print()

    if choice == 1:
        print("Получение информации о системе...")
    elif choice == 2:
        print("Проверка интернет-соединения...")
    elif choice == 3:
        print("Получение сетевых настроек компьютера...")
    elif choice == 4:
        print("Выполняется выход...")
    else:
        print("Неверный выбор! Попробуйте снова.")


    if choice == 4:
        break