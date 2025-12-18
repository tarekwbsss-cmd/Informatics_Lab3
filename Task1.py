import re

pattern = r'([А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)?)\s[А-ЯЁ]\.(?:[А-ЯЁ]\.)?'


print("Test 1: Lab Example : ")
text1 = "помогали: Анищенко А.А., Машина Е.А. и Голованова-Иванова Д.В., а также Балакшин П.В."
surnames1 = re.findall(pattern, text1)
surnames1.sort()
print("Original text:", text1)
print("Found and sorted surnames:", surnames1)
print("\n" + "="*30 + "\n")


print("Test 2: Text with no matches : ")
text2 = "Просто текст без фамилий в нужном формате. Иван Иванов не подходит."
surnames2 = re.findall(pattern, text2)
surnames2.sort()
print("Original text:", text2)
print("Found and sorted surnames:", surnames2)
print("\n" + "="*30 + "\n")


print("Test 3: Surnames with single initial : ")
text3 = "В совещании участвовали: Петров П., Сидоров С. и Кузнецов-Задунайский К."
surnames3 = re.findall(pattern, text3)
surnames3.sort()
print("Original text:", text3)
print("Found and sorted surnames:", surnames3)
print("\n" + "="*30 + "\n")


print("Test 4: Surnames at start and end : ")
text4 = "Смирнов В.В. открыл заседание, а закрыл его Попов Д."
surnames4 = re.findall(pattern, text4)
surnames4.sort()
print("Original text:", text4)
print("Found and sorted surnames:", surnames4)
print("\n" + "="*30 + "\n")


print("Test 5: Mixed text : ")
text5 = "Это точно был он, Зайцев А.Б., но не его друг (Волков И.А.)."
surnames5 = re.findall(pattern, text5)
surnames5.sort()
print("Original text:", text5)
print("Found and sorted surnames:", surnames5)
print("\n" + "="*30 + "\n")
