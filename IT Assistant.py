import platform
import socket
import subprocess
import sys
import speedtest

sys.stdout.reconfigure(encoding="utf-8")
name_prog = "================== \nIT ASSISTANT v0.4 \n=================="

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

os_name = platform.system()
os_version = platform.release()
architecture = platform.machine()
pc_name = platform.node()
processor_name = platform.processor()

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

        except OSError:
            print("Инетрнет не подключён!")
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
    elif choice == 4:
        print("Выполняется выход...")
    else:
        print("Неверный выбор! Попробуйте снова.")


    if choice == 4:
        break


