 
#  1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
#  В тексте используется разделитель пробел.
# in
# Number of words: 10
# 
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
 
 from random import choices, sample


def list_rand_words(count: int, alp: str = 'абв'):
    words_list = []
    for i in range(count):
        letters = sample(alp, k=3)
        words_list.append("".join(letters))
    return " ".join(words_list)

def simple_sentence(words: str) -> str:
    return " ".join(i for i in words.split() if i != "абв")

num = int(input("Number of words: "))
if num <= 0:
    print("The data is incorrect")
else:
    all_list = list_rand_words(num)
    print(all_list)
    print(simple_sentence(all_list))