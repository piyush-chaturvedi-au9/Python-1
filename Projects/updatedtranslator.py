from googletrans import Translator
translator = Translator()
def GoogleTranslator():
    text = input("Enter the text in your language : ")
    dest = input("Enter the destination language with ISO-639s : ")
    translated = translator.translate(text,dest=dest)
    with open('E:\Python\File I_O\Test.txt',mode='w',encoding="utf8") as write:
        write.write(f"Original text :{translated.origin}\nTranslated to : {translated.dest}\n\n{translated.text}")
    
    with open('E:\Python\File I_O\Test.txt',mode='r',encoding="utf8") as text:
        print(text.read())

GoogleTranslator()