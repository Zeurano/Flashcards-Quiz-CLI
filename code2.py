
import random
import time

prepasscode = [
    ['kobyakov', 'ko'],
    ['isagi', 'egoist'],
    ['bachira', 'flyday'],
]  #[cite: 5]
passcode = dict(prepasscode)  #[cite: 5]

log = input('Enter username: ')  #[cite: 5]
password = input('Enter password: ')  #[cite: 5]

if log in passcode and password == passcode[log]:  #[cite: 5]
  print('Welcome!')  #[cite: 5]
  liste = [
      ['what is the capital of USA?', 'Washington'],
      ['what is the capital of Russian Federation?', 'Moscow'],
  ]  #[cite: 5]
  go = input("Wanna 'start' or 'add' cards?")  #[cite: 5]
  liste2 = liste.copy()  #[cite: 5]

  while go == 'add':  #[cite: 5]
    adde = input('please name the card: ')  #[cite: 5]
    adde2 = input('please answer: ')  #[cite: 5]
    liste2.append([adde, adde2])  #[cite: 5]
    go2 = input('OK')  #[cite: 5]
  else:  #[cite: 5]
    random.shuffle(liste2)  #[cite: 5]
    score = 0  #[cite: 5]
    for card in liste2:  #[cite: 5]
      print(card[0])  #[cite: 5]
      ans = input('ответ: ')  #[cite: 5]
      if ans == card[1]:  #[cite: 5]
        print('Правильно!')  #[cite: 5]
        score += 1  #[cite: 5]
      else:  #[cite: 5]
        print(f'Неверно! Правильный ответ: {card[1]}')  #[cite: 5]
    print(f'Результат: {score}/{len(liste2)}')  #[cite: 5]
