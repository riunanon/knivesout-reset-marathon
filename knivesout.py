#pythonista3専用

import keyboard,random,clipboard,string

def random_digits_name(n): #数字のみのランダム文字列
    randlst = [random.choice(string.digits) for i in range(n)]
    keyboard.insert_text(''.join(randlst))
    keyboard.insert_text('\n')

def random_letters_name(n): #アルファベットのみのランダム文字列
    randlst = [random.choice(string.ascii_letters) for i in range(n)]
    keyboard.insert_text(''.join(randlst))
    keyboard.insert_text('\n')

def random_name(n): #数字とアルファベット混合のランダム文字列
    randlst = [random.choice(string.digits+string.ascii_letters) for i in range(n)]
    keyboard.insert_text(''.join(randlst))
    keyboard.insert_text('\n')

def hai(): #「はい」を入力
    keyboard.insert_text('はい')
    keyboard.insert_text('\n')

def passcode(passcode): #パスコードを入力
    keyboard.insert_text(passcode)
    keyboard.insert_text('\n')
