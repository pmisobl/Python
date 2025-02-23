from sys import argv

script, filename = argv

text = open (filename) # filename passed as an argument 
print (f"here is your file : {filename}") 
# print (text) 
print (text.read())

print ("Type the filename again : ")
file_again = input("> ")
txt_again = open(file_again)

print (txt_again.read())