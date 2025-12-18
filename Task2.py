import re

print("Test 1: Lab Example : ")
text1 = "Классное слово – обороноспособность, которое должно идти после слов: трава и молоко."
vowels = "аеёиоуыэюя"
all_words1 = re.findall(r'\b[а-яА-ЯёЁ]+\b', text1)
valid_words1 = []
for word in all_words1:
    found_vowels = set(char for char in word.lower() if char in vowels)
    if len(found_vowels) == 1:
        valid_words1.append(word)
sorted_words1 = sorted(valid_words1, key=lambda w: (len(w), w.lower()))
print("Original text:", text1)
print("Found and sorted words:", sorted_words1)
print("\n" + "="*30 + "\n")


print("Test 2: Simple text with matches : ")
text2 = "Анна шла в шалаш. Там спал кот."
all_words2 = re.findall(r'\b[а-яА-ЯёЁ]+\b', text2)
valid_words2 = []
for word in all_words2:
    found_vowels = set(char for char in word.lower() if char in vowels)
    if len(found_vowels) == 1:
        valid_words2.append(word)
sorted_words2 = sorted(valid_words2, key=lambda w: (len(w), w.lower()))
print("Original text:", text2)
print("Found and sorted words:", sorted_words2)
print("\n" + "="*30 + "\n")


print("Test 3: Text with words to exclude : ")
text3 = "Условие простое: найти слова, а не предложения."
all_words3 = re.findall(r'\b[а-яА-ЯёЁ]+\b', text3)
valid_words3 = []
for word in all_words3:
    found_vowels = set(char for char in word.lower() if char in vowels)
    if len(found_vowels) == 1:
        valid_words3.append(word)
sorted_words3 = sorted(valid_words3, key=lambda w: (len(w), w.lower()))
print("Original text:", text3)
print("Found and sorted words:", sorted_words3)
print("\n" + "="*30 + "\n")


print("Test 4: Text for testing sorting : ")
text4 = "Он, как и я, ел хлеб."
all_words4 = re.findall(r'\b[а-яА-ЯёЁ]+\b', text4)
valid_words4 = []
for word in all_words4:
    found_vowels = set(char for char in word.lower() if char in vowels)
    if len(found_vowels) == 1:
        valid_words4.append(word)
sorted_words4 = sorted(valid_words4, key=lambda w: (len(w), w.lower()))
print("Original text:", text4)
print("Found and sorted words:", sorted_words4)
print("\n" + "="*30 + "\n")


print("Test 5: Mixed case text : ")
text5 = "ПАПА всегда прав. А МАМА?"
all_words5 = re.findall(r'\b[а-яА-ЯёЁ]+\b', text5)
valid_words5 = []
for word in all_words5:
    found_vowels = set(char for char in word.lower() if char in vowels)
    if len(found_vowels) == 1:
        valid_words5.append(word)
sorted_words5 = sorted(valid_words5, key=lambda w: (len(w), w.lower()))
print("Original text:", text5)
print("Found and sorted words:", sorted_words5)
print("\n" + "="*30 + "\n")
