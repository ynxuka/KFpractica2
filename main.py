import argparse


def main():
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description="Параметры для работы с пакетами")

    # Добавляем аргументы
    parser.add_argument('-n', '--package_name', required=True, type=str,
                        help='Название пакета')
    parser.add_argument('-u', '--repository_url', required=True, type=str,
                        help='URL репозитория')
    parser.add_argument('-m', '--repository_mode', required=True, type=str,
                        help='Режим репозитория')
    parser.add_argument('-v', '--package_version', required=True, type=str,
                        help='Версия пакета')
    parser.add_argument('-o', '--output_file', required=True, type=str,
                        help='Выходной файл')

    # Получаем аргументы
    params = parser.parse_args()

    # Выводим полученные значения
    print("Полученные аргументы:")
    print(f"  Пакет: {params.package_name}")
    print(f"  Репозиторий: {params.repository_url}")
    print(f"  Режим: {params.repository_mode}")
    print(f"  Версия: {params.package_version}")
    print(f"  Выходной файл: {params.output_file}")
    print()

    # Проверяем корректность значений
    errors = []

    if not params.package_name.strip():
        errors.append("Название пакета не может быть пустым")

    if not params.repository_url.strip():
        errors.append("URL репозитория не может быть пустым")

    if not params.repository_mode.strip():
        errors.append("Режим репозитория не может быть пустым")

    if not params.package_version.strip():
        errors.append("Версия пакета не может быть пустой")

    if not params.output_file.strip():
        errors.append("Выходной файл не может быть пустым")

    # Выводим ошибки или подтверждение
    if errors:
        print("Обнаружены ошибки:")
        for error in errors:
            print(f"  - {error}")
        exit(1)
    else:
        print("Все параметры корректны!")


if __name__ == "__main__":
    main()