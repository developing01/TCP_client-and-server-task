import socket
from PIL import Image

#Створюю сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# #Задаю параметри для підключення сокета
host, port = 'localhost', 8888

#Підключаю сокет
sock.connect((host, port))
img_data = []
sorted_data = []

#надсилаю запит на сервер і зчитую всі необхідні данні
try:
    while True:
        sock.send(b'next')
        chunk = sock.recv(2048)
        print('Chunk complete!')
        img_data.append(chunk)
except BrokenPipeError:
    print('Connection closed')
    # обробляю закінчення зчитування

#створюю список з кортежами з необхідною інформацією для сортування
for chunk in img_data:
    if len(chunk) > 0:
        info_tuple = (chunk[0], chunk[1:])
        sorted_data.append(info_tuple)

#Сортую список у правильному порядку
sorted_data.sort(key=lambda x: x[0])

#зберігаю всю інформацію в змінну
byte_data = b''
for ch in sorted_data:
    byte_data += ch[1]

#записую данні у текстовий файл
with open('byte_info.txt', 'wb') as bt_inf:
    bt_inf.write(byte_data)

path_to_file = 'byte_info.txt'
safe_path = path_to_file.replace('.txt', '.jpg')

#записую данні з файлу для подальшого перетворення в картинку
with open(path_to_file, 'rb') as textfile:
    bytestring = textfile.read()

with open(safe_path, 'wb') as imagefile:
    imagefile.write(bytestring)

image = Image.open(safe_path)
