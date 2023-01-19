#pythonista3専用

import keyboard,random,clipboard,string

def random_digits_name(n,enter=True): #数字のみのランダム文字列
    randlst = [random.choice(string.digits) for i in range(n)]
    keyboard.insert_text(''.join(randlst))
    if enter:
      keyboard.insert_text('\n')

def random_letters_name(n,enter=True): #アルファベットのみのランダム文字列
    randlst = [random.choice(string.ascii_letters) for i in range(n)]
    keyboard.insert_text(''.join(randlst))
    if enter:
      keyboard.insert_text('\n')

def random_name(n,enter=True): #数字とアルファベット混合のランダム文字列
    randlst = [random.choice(string.digits+string.ascii_letters) for i in range(n)]
    keyboard.insert_text(''.join(randlst))
    if enter:
      keyboard.insert_text('\n')

def hai(enter=True): #「はい」を入力
    keyboard.insert_text('はい')
    if enter:
      keyboard.insert_text('\n')

def passcode(passcode,enter=True): #パスコードを入力
    keyboard.insert_text(passcode)
    if enter:
      keyboard.insert_text('\n')
