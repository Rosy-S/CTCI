##17.2: Write a method to shuffle a deck of cards. It must be a perfect shuffle with each shuffle having equal chance of happening
import random
def shuffle_deck(deck): 
	c = 0
	while c < len(deck): 
		random_card = random.randrange(0, len(deck))
		temp = deck[c]
		deck[c] = deck[random_card]
		deck[random_card] = temp
		c += 1
	return deck
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
# print shuffle_deck(deck)

##17.3 write a mthod to random generate a set of m integers from an array of size n w/ each element having equal prob of being chosen.
def generate_set(m, array): 
	if m > len(array): 
		return "not enough numbers to generate a set with."
	ceiling = len(array)
	results = []
	result_set = set()
	while len(result_set) < m: 
		result_set.add(random.randrange(0, ceiling))
	for num in result_set: 
		results.append(array[num])
	return results

#print generate_set(4, deck)

##17.4: an array A contains all the integers from 0 to n, except for one number which is missing. 
def find_number(num_array): 
	pass

## 17.5: given an array filled with letters and numbers, find the longest subarray with an equal number of letters and numbers
