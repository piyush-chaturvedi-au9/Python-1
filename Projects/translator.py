from googletrans import Translator
translator = Translator()
def GoogleTranslator():
    
    with open('E:\Python\File I_O\Test.txt',mode='r',encoding="utf8") as text:
        file_text = text.read()
    
    translated = translator.translate(file_text)
    with open('E:\Python\File I_O\Test1.txt',mode='w',encoding="utf8") as write:
        write.write(f"\nTranslated to : {translated.dest}\n\n{translated.text}")
    
    with open('E:\Python\File I_O\Test1.txt',mode='r',encoding="utf8") as text:
        print(text.read())

GoogleTranslator()