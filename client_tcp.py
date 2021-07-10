import socket

img_data = []


def connection_and_parse(host, port, command, chunk_size):

    #Створення сокета, надсилання запиту на сервер і зчитування всієї необхідної інформації
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    try:
        while True:
            sock.send(command)
            chunk = sock.recv(chunk_size)
            print('Chunk complete!')
            img_data.append(chunk)
    except BrokenPipeError:
        print('Connection closed')
        # обробка закінчення зчитування


def data_processing(data_list):
    saved_list = []
    #створення списку з кортежами з необхідною інформацією для сортування
    for chunk in data_list:
        if len(chunk) > 0:
            info_tuple = (chunk[0], chunk[1:])
            saved_list.append(info_tuple)

    #Сортування списку у правильному порядку
    saved_list.sort(key=lambda x: x[0])

    #зберігання інформації в byte_data
    byte_data = b''
    for ch in saved_list:
        byte_data += ch[1]
    return byte_data


def image_conversion(data, image_name):
    from PIL import Image

    #записую данні у текстовий файл
    with open(f'{image_name}.txt', 'wb') as bt_inf:
        bt_inf.write(data)

    path_to_file = f'{image_name}.txt'
    safe_path = path_to_file.replace('.txt', '.jpg')

    #записую данні з файлу для подальшого перетворення в картинку
    with open(path_to_file, 'rb') as textfile:
        bytestring = textfile.read()

    with open(safe_path, 'wb') as imagefile:
        imagefile.write(bytestring)

    return Image.open(safe_path)


connection_and_parse('localhost', 8888, b'next', 2048)
image_conversion(data_processing(img_data), 'byte_info')

