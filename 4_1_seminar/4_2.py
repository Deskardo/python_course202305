# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.

text = "She sells sea shells on the sea shore The shellsthat she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".split()
text_pl = set()
print(text)

for i in range(len(text)):
    text_pl.add(text[i])
    
print(len(text_pl))