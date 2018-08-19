from sys import stdin,stdout
import os


alphabets_lower='abcdefghijklmnopqrstuvwxyz'

alphabets_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def read_input(s,key):
	message=''
	for character in s:
		if character in alphabets_upper:
			position=alphabets_upper.find(character)
			new_position=(position+key)%26
			message+=alphabets_upper[new_position]
		elif character in alphabets_lower:
			position=alphabets_lower.find(character)
			new_position=(position+key)%26
			message+=alphabets_lower[new_position]
		else:
			message+=character
	return message



def read_file():
	message=''
	base_dir=os.getcwd()

	stdout.write("Enter the name of file(if in same directory)\n")
	stdout.write("If file is not in same directory enter the full path:\n")
	filename=stdin.readline().strip('\n')
	stdout.write("\nEnter the Key\n")
	key=int(stdin.readline())
	new_file='encrypted.txt'
	

	with open(filename,'r') as file:
		#Use loop Here
		s=file.read()
		for character in s:
			if character in alphabets_upper:
				position=alphabets_upper.find(character)
				new_position=(position+key)%26
				message+=alphabets_upper[new_position]
			elif character in alphabets_lower:
				position=alphabets_lower.find(character)
				new_position=(position+key)%26
				message+=alphabets_lower[new_position]
			else:
				message+=character

	with open(new_file,'w+') as file:
		file.write(message)
	stdout.write("Encrypted file has been created\n")



try:
	stdout.write("Choose Options:\n")
	stdout.write("1.Encrypt input text\n2.Encrypt text file\n3.Decrypt")

	option=int(stdin.readline())

	if option==1:
		stdout.write("Enter the Character\n")
		s=stdin.readline()
		stdout.write("Enter the key to Encrypt\n")
		key=int(stdin.readline())
		output=read_input(s,key)
		stdout.write(output+'\n')

	elif option==2:
		read_file()

	elif option==3:
		read_file()

	else:
		stdout.write("Sorry wrong option selected\n")

	

except Exception as e:
	stdout.write(str(e)+'\n')






