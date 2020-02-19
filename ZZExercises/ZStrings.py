'''
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'
'''
def hello_name(name):
  return "Hello "+name+"!"


'''
Given two strings, a and b, return the result of putting them together in the order abba,
 e.g. "Hi" and "Bye" returns "HiByeByeHi".

make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'
'''
def make_abba(a, b):
  return a + (b * 2 ) + a


'''
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
In this example, the "i" tag makes <i> and </i> which surround the word "Yay". 
Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'
'''
def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"


'''
Given an "out" string length 4, such as "<<>>", and a word, 
return a new string where the word is in the middle of the out string, e.g. "<<word>>".

make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'
'''
'''
def make_out_word(out, word):
  out_f2 = out[0:len(out)/2]
  out_l2 = out[len(out)/2:]
  return out_f2+word+out_l2
'''
'''
string1 = "alpha beta beta gamma gamma gamma delta"
string1 = "my cat is my cat fat"

new_string = list (string1.split(" "))
#print(new_string)

for each in new_string:
  if new_string.count(each)>1:
    print(new_string.index(each))
    
    new_string.pop(new_string.index(each) )

#print(new_string)
out = ""
for each in new_string:
  out = out+" "+each
print(string1)
print(out)

'''
def dupli(word):
  mylist = []
  [mylist.append(x) for x in word if x not in mylist]
  return mylist

string1 = "my cat is my cat fat"
string1 = "alpha beta beta gamma gamma gamma delta"
string1 = ' '.join(dupli(string1.split(' ')))
print(string1)