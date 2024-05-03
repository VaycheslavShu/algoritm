def decode_command(compressed_command: str):
    decoded_commands = []
    
    # Разбиваем входную строку на подстроки по закрывающимся квадратным скобкам
    for part in compressed_command.split(']'):
        # Убираем пробелы и делим на части по открывающимся квадратным скобкам
        subparts = part.strip().split('[')
        
        # Если первая часть - это число, то это количество повторений
        if subparts[0].isdigit():
            count = int(subparts[0])
            command = subparts[1]
        else:
            count = 1  # Если нет числа, значит команда повторяется один раз
            command = subparts[0]
        
        # Добавляем команду count раз в список
        for _ in range(count):
            decoded_commands.append(command)
    
    # Возвращаем расшифрованную команду в виде строки
    return ''.join(decoded_commands)


if __name__ in '__main__':
    str_array: str = input()
    print(str(decode_command(str_array))) 