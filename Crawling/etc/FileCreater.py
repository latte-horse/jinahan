f =open('test.txt',mode='wt', encoding='utf-8')

f.write('파이썬으로 파일을 작성하고 있습니다.')
f.write('newline 문자로 개행해 봅니다. \n')
f.write('개행이 잘 되었나요?')

f.close()
f.read('test.txt',mode='rt',encoding='utf-8')
f.read(10)