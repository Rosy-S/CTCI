#1)Is_unique: 
def is_unique_nsquared(string): 
	for i in range(len(string) - 1): 
		for n in range(i + 1, len(string)): 
			if string[i] == string[n]: 
				return False
	return True

def is_unique_n(string): 
	existing_values = {}
	for letter in string: 
		if letter in existing_values: 
			return False
		else: 
			exsting_values[letter] = 1
	return True
#*************************************************************************************
#2) write a method to see if one string is a permutation of the other: 
def is_permutation_nlogn(string1, string2): 
	string1 = sorted(string1)
	string2 = sorted(string2)

	return string1 == string2
# print is_permutation_nlogn("rosysanchez", "sanchezrosy")
# print is_permutation_nlogn("potatoes", 'potaytos')

def is_permutation_n(string1, string2): 
	hash1 = {}
	hash2 = {}
	def helper(string, dic): 
		for letter in string: 
			if letter in dic: 
				dic[letter] += 1
			else: 
				dic[letter] = 1
	helper(string1, hash1)
	helper(string2,hash2)

	if len(hash2) != len(hash1): 
		return False
	for key, value in hash1.iteritems(): 
		if value != hash2.get(key): 
			return False
	return True

# print is_permutation_n("rosysanchez", "sanchezrosy")
# print is_permutation_n("lemonwater", "wateroflemon")
#**************************************************************************************

#3) Write a method to replace all space in a string with "%20"

def url_ify_nspace(string): 
	url = ""
	back_index = len(string) - 1
	while not (string[back_index]).isalpha():
		back_index -= 1
	index = 0
	while index <= back_index: 
		if string[index] == " ": 
			url+="%20"
		else: 
			url += string[index]
		index += 1
	return url
# print(url_ify("hello this is one long url that is also a sentence       "))
# print(url_ify("hello this is also a url but there is no spaces at the end"))

#****************************************************************************************

#4) Given a string, write a funciton to check if it is a permutation of a palindrome
def is_palindrome_ntime(string): 
	string = string.replace(" ", "").lower()
	duplicate_set = set()
	for char in string:
		if char in duplicate_set: 
			duplicate_set.remove(char)
		else: 
			duplicate_set.add(char)
	return len(duplicate_set) <= 1

# print is_palindrome_ntime('tacocat')
# print is_palindrome_ntime("Rosy Sanchez")
# print is_palindrome_ntime("Taco Cat")
#****************************************************************************************

#5) Given two strings, write a function(one_away) to check if they are one edit or zero edits away
def is_different(string1, string2): 
	differences = 0
	for i in range(len(string1)): 
		if string1[i] != string2[i]: 
			differences += 1
		if differences > 1: 
			return False
	return True

def add_character(string1, string2): 
	index1, index2, shifter = 0, 0, 0
	while index1< len(string1) and index2<len(string2): 
		if string1[index1] != string2[index2]: 
			shifter +=1
			index1 +=1
		else: 
			index1 +=1
			index2 += 1
		if shifter > 1: 
			return False
	return True

def one_away(string1, string2): 
	if len(string1) == len(string2): 
		return is_different(string1, string2)
	elif len(string1) - 1 == len(string2): 
		return add_character(string1, string2)
	elif len(string1) + 1 == len(string2): 
		return add_character(string2, string1)
	else: 
		return False

print one_away('pale', 'ple')
print one_away('pales', 'pale')
print one_away('pale', 'bale')
print one_away('pale', 'bake')

#****************************************************************************************

#6) implement a method to perform basic string compression using the counts of repeated characters.
def compressed_string(string): 
	index = 0
	counter = 1
	results = []
	while index < (len(string) - 1): 
		if string[index] != string[index +1]: 
			results.append(string[index] + str(counter))
			counter = 1
		else: 
			counter += 1
		index += 1
	results.append(string[index] + str(counter))
	results = ''.join(results)
	return results

print compressed_string('abcdefg')
print compressed_string('aabcdefg')
print compressed_string('abfdd')
print compressed_string('aabcccccaa')

#*************************************************************************************
#7) given an image represented by an MxM matirix, write a method to rotate the image 90 degrees
def rotate_CW(matrix): 
	column_list = [[] for i in range(len(matrix))]
	[[column_list[i].append(row[i]) for i in range(len(row))] for row in matrix]
	matrix = [reversed(col) for col in column_list]
	return matrix
print rotate_CW([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
