import knivesout

knivesout.random_digits_name(8) #数字のみのランダム文字列　括弧内に文字数を入力(int)
knivesout.random_letters_name(8) #アルファベットのみのランダム文字列　括弧内に文字数を入力(int)
knivesout.random_name(8) #数字とアルファベット混合のランダム文字列　括弧内に文字数を入力(int)
knivesout.hai() #「はい」を入力
knivesout.passcode('passcode') #パスコードを入力　括弧内にパスコードを入力(str)

#全てデフォルトでは入力後enterキーを押して動作をショートカットできるようにしています。
#もしそれを無効にしたい場合は(enter=False)となるように括弧内にenter=Falseを入力してください。
#文字数やパスコードなど引数を括弧内に入力してしまっている場合は(8,enter=False)('passcode',enter=False)のようにカンマ(,)で区切って入力してください。
