import random as r
import sys, string, re, math
from Tkinter import Tk
from tkFileDialog import askopenfilename

welcome_string = "This is a pin number generator. If you want to truly randomize the pin then enter yes and then select a text file. If not then enter no."
Followers = [[0 for x in range(26)] for x in range(26)] 
Count = [0 for x in range(26)]
Starters = [0 for x in range(26)]
num_starters = 0
total_num_letters = 0

def get_file():
	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
	return filename

def get_number_of_pins():
	x = int(raw_input("How many pin numbers do you want to generate? "))
	print "Your pin options are: "
	return x

def rand_pin_no_file():
	a = r.randint(0, 9)
	b = r.randint(0, 9)
	c = r.randint(0, 9)
	d = r.randint(0, 9)
	return str(a) + str(b) + str(c) + str(d)


def update_table(word, word_index, index):
	global Count; global Followers
	Count[word_index] += 1
	Followers[word_index][int(math.fabs((ord('z') - ord(word[index + 1])) - 25))] += 1

def process_input_file(filename):
	global num_starters; global total_num_letters
	global Starters
	x = string.split(filename,'/')
	extension = string.split(x[len(x) - 1], '.')
	if extension[1] != "txt":
		print "please select a .txt file."
		sys.exit(-1)
	else:
		filename = open(filename, 'r')
		for line in filename:
			line = re.split("[^a-zA-Z]*", line.lower())
			for word in line:
				if len(word) > 0: 
					letters = list(word)
					for i in range(len(letters)):
						x = ord(letters[i])
						index = int(math.fabs((ord('z') - x) - 25))
						if i == 0: Starters[index] += 1; num_starters += 1
						if i != (len(letters)-1): update_table(letters, index, i)
						total_num_letters += 1


def invert_tables():
	global Followers; global Count; global Starters; global num_starters
	for x in range(len(Followers)):
		row = Followers[x]
		Starters[x] = (num_starters - Starters[x])
		for z in range(len(row)):
			Followers[x][z] = (Count[x] - Followers[x][z])



def print_followers():
	global Followers
	for i in range(len(Followers)):
	    for j in range(len(Followers[0])):
	        print '{:7}'.format(Followers[i][j]),
	    print



def rand_pin_file():
	start = r.randint(0, num_starters)
	index = 0
	pin = []
	for x in range(len(Starters)):
		index += Starters[x]
		if index >= start:
			pin.append(x); index = 0; break

	for x in range(3):
		num = r.randint(0, Count[pin[x]])
		for y in range(len(Followers)):
			index += Followers[pin[x]][y]
			if index >= num:
				pin.append(y); index = 0; continue

	return translate_into_pin(pin)


def translate_into_pin(pin):
	result = str()

	for x in range(4):
		if pin[x] == 0 or pin[x] == 1 or pin[x] == 2:
			result += str(1); continue
		elif pin[x] == 3 or pin[x] == 4:
			result += str(2); continue
		elif pin[x] == 5 or pin[x] == 6 or pin[x] == 7:
			result += str(3); continue
		elif pin[x] == 8 or pin[x] == 9:
			result += str(4); continue
		elif pin[x] == 10 or pin[x] == 11 or pin[x] == 12:
			result += str(5); continue
		elif pin[x] == 13 or pin[x] == 14:
			result += str(6); continue
		elif pin[x] == 15 or pin[x] == 16 or pin[x] == 17:
			result += str(7); continue
		elif pin[x] == 18 or pin[x] == 19:
			result += str(8); continue
		elif pin[x] == 20 or pin[x] == 21 or pin[x] == 22:
			result += str(9); continue
		elif pin[x] == 23 or pin[x] == 24 or pin[x] == 25:
			result += str(0); continue
	return result






def main():
	global total_num_letters
	print welcome_string
	response = raw_input("Base file? Yes or no: ")
	if response == "yes":
		f = get_file()
		if f:
			process_input_file(f)
			for x in range(get_number_of_pins()):
				print rand_pin_file()
		else:
			for x in range(get_number_of_pins()):
				print rand_pin_no_file()

	else:
		for x in range(get_number_of_pins()):
				print rand_pin_no_file()
	

if __name__ == '__main__':
	main()