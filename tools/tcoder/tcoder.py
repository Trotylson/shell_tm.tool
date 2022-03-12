

CodeDictionary = {'a':'Z=','ą':'!y','b':'X?','c':'w0','ć':'1V','d':'u^','e':'$T','ę':'s0',
                  'f':'@Q','g':'p?','h':'@o','i':'N&','j':'mX','k':'!L','l':'k@','ł':'$J',
                  'm':'9i','n':'5H','ń':'g%','o':'3F','ó':'4f','p':'E$','q':'0c','r':'B>',
                  's':'!a','ś':'5+','t':'82','u':'0F','v':'-x','w':'vV','x':'+!','y':'\!',
                  'z':'B5','ż':'5b','ź':'6b',
                  ' ':'&i','.':'\e',',':'\i',':':'\d'}


def runDecoding(text):

    print('\n\nDecoding:', text,'\n\nDecoded message: ',end='')
    coded = ""
    for x in text:
        coded += x
        if coded in CodeDictionary.values():
            print(list(CodeDictionary.keys())[list(CodeDictionary.values()).index(coded)], end='')
            coded = ""
    print('\n\nDECODED!\n')

def runEncoding(text):

    print('\n\nEncoding:', text, '\n\nCoded message: ',end='')
    for x in text:
        if x in CodeDictionary:
            print(CodeDictionary[x], end='')
    print('\n\nENCODED!\n')

