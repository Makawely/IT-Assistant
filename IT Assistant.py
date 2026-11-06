import platform
import socket
import subprocess
import sys
import speedtest
import os

sys.stdout.reconfigure(encoding="utf-8")
name_prog = "================== \nIT ASSISTANT v0.6\n=================="

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
pc_management = "4. Управление компьютером"
net_diagnostic = "5. Диагностика сети"
process_management = "6. Управление процессами"
admin_tools = "7. Инструменты администратора"
exit_menu = "8. Выход"
task_manager = "1. Диспетчер задач"
control_panel = "2. Панель управления"
restart_computer = "3. Перезагрузить компьютер"
back_menu = "4. Вернуться в главное меню"



os_name = platform.system()
os_version = platform.release()
architecture = platform.machine()
pc_name = platform.node()
processor_name = platform.processor()


while True:
    print(info_pc)
    print(check_net)
    print(net_set)
    print(pc_management)
    print(net_diagnostic)
    print(process_management)
    print(admin_tools)
    print(exit_menu)

    print()
    try:
        choice = int(input("Выберите действие: "))
    except ValueError:
        print()
        print("Ошибка! Введите число от 1 до 8.")
        print()
        continue

    print()
    if choice == 1:
        print("Получение информации о системе...")
        print()
        print("Операционная система:", os_name)
        print("Версия:", os_version)
        print("Архитектура:", architecture)
        print("Имя компьютера:", pc_name)
        print("Процессор:", processor_name)
        print()
    elif choice == 2:
        print("Проверка интернет-соединения...")
        print()
        try:
            connection = socket.create_connection(("8.8.8.8", 53), timeout=5)
            connection.close()
            print("Интернет подключён!")
            print()

        except OSError:
            print("Интернет не подключён!")
        print()

        result = subprocess.run(
            ["ping", "8.8.8.8"],
            capture_output=True,
            text=True,
            encoding="cp866",
            errors="replace"
        )

        print(result.stdout)

        print()

        st = speedtest.Speedtest()
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        print("Download:", round(download_speed, 2), "Мбит/с")
        print("Upload:", round(upload_speed, 2), "Мбит/с")
        print()
    elif choice == 3:
        print("Получение сетевых настроек компьютера...")
        print()
        subprocess.run(["ipconfig"])
        print()
    elif choice == 4:
        print("Открытие инструментов управления компьютером...")
        print()
        while True:

            print(task_manager)
            print(control_panel)
            print(restart_computer)
            print(back_menu)
            print()

            try:
                sub_choice = int(input("Выберите действие: "))
            except ValueError:
                print()
                print("Ошибка! Введите число от 1 до 4.")
                print()
                continue

            if sub_choice == 1:
                print("Выполняется действие... ")
                os.startfile("taskmgr.exe")
                print()
            elif sub_choice == 2:
                print("Выполняется действие... ")
                os.startfile("control.exe")
                print()
            elif sub_choice == 3:
                print()
                confirm = input("Перезагрузить компьютер? (да/нет): ").lower()
                print()
                if confirm == "да":
                    confirm_again = input("Вы точно хотите перезагрузить компьютер? (да/нет): ").lower()
                    print()
                    if confirm_again == "да":
                        print("Перезагрузка подтверждена!")
                        subprocess.run(["shutdown", "/r", "/t", "10"])
                        print()
                    elif confirm_again == "нет":
                        print("Перезагрузка отменена!")
                        print()
                    else:
                        print("Неверный ответ!")
                        print()

                elif confirm == "нет":
                    print("Отмена перезагрузки... ")
                else:
                    print("Ошибка! Введите да или нет!")
            elif sub_choice == 4:
                print()
                print("Выход в главное меню... ")
                print()
            else:
                print("Неверный выбор! Попробуйте снова.")
                print()

            if sub_choice == 4:
                break

    elif choice == 5:
        print("Запуск диагностики сети...")
        print()
    elif choice == 6:
        print("Открытие диспетчера процессов...")
        print()
    elif choice == 7:
        print("Запуск инструментов администратора...")
        print()
    elif choice == 8:
        print("Выполняется выход...")

    else:
        print("Неверный выбор! Попробуйте снова.")
        print()

    if choice == 8:
        break


