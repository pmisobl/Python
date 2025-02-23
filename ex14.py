from sys import argv

script, username, surname = argv
prompt = '>'

print (f"Hi {username} {surname}. I'm the {script} script ")
print ("I would like to ask you a few questions ")
print (f"Do you like me {username}")
likes = input(prompt)

print (f"Where do you live {username} ? ")
lives = input(prompt)

print ("What kind of computer do you have ? ")
computer = input(prompt)

print (f""" Alright, so you sad {likes} about liking me
    You live in {lives}. Not sure where that is. 
    And you have {computer} computer. Nice
             """)