# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('File.txt', 'r', encoding='utf-8') as file:
     text = file.read()
#
def com(text): # Зашифровали
    str_list = []
    count = 1
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            str_list.append(str(count) + text[i])
            count = 1
    if count > 1 or (text[len(text) - 2] != text[-1]):
        str_list.append(str(count) + text[i])
    return str_list
print(text)
print(com(text))
#
new_text = ''.join(com(text))
# Записали
with open('File1.txt', 'w', encoding='utf-8') as file:
    file.write(new_text)
#
#
with open('File1.txt', 'r', encoding='utf-8') as file:
          text2 = file.read()
#
print(text2)
def decom(text):
    new_txt = ''
    num = 0
    for i in range(len(text)):
        if text[i].isnumeric():
            num = text[i]
        else:
            new_txt =new_txt + text[i] * int(num)
    return new_txt
# a = [0 for i in range(5)]
print(decom(text2))
decod = decom(text2)
with open('File2.txt', 'w', encoding='utf-8') as file:
     file.write(decod)