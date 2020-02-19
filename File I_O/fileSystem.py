'''
r - read
w - write
'''
'''
#Open
sample_file = open('sample.txt')  #opening file and assign to variable
print(sample_file.read()) 
'''
'''
#Seek
sample_file = open('sample.txt')  #opening file and assign to variable
print(sample_file.read())
sample_file.seek(0)
print(sample_file.read())
print(sample_file.read()) # doen not read because cursor is at end
'''
'''
#close

sample = open('Sample.txt')
print(sample.read())
sample.close()
print(sample.read()) # error
'''
'''
#With open read
with open('Sample.txt') as sample: # it will auto close the file once it's task is finished
    print(sample.read())
'''
# with open mode ,default is r

with open('Sample.txt',mode='w') as test:
    test.write("""Hello My name is Praveen
""")



 
