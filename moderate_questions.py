

# 16.6: Given two arrays of integers, compute the pair of values (one value in each array)
# with the smallest non-negative difference. return the difference. 
from sys import maxint
def smallest_difference(array1, array2): 
	array1.sort()
	array2.sort()
	a = 0
	b = 0
	difference = maxint
	while a < len(array1) and b < len(array2): 
		print array1[a], array2[b]
		difference = min(difference, abs(array1[a] - array2[b]))
		if array1[a] < array2[b]: 
			a += 1
		else: 
			b += 1
	return difference
# print smallest_difference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8, 9, 20, 40])

# 16.7: Write a method that finds the maximum of two umbers. You should not use
# if-else or any other comparison opperator. 
def find_max(a, b): 
	total = a + b
	pass

# 16.8 Given any integer, print an English phrase that describes the integer
def translate_num(num): 
	num = str(num)
	results = []
	place_dictionary = {3: 'hundred', 4: 'thousand', 6: 'mil'}
	while len(num) > 3: 
		length = len(num)
		if length > 9: 
			placeholder = length - 9
			billon = num[:placeholder]
			results.append(hundreds_breakdown(billon) + " billon,")
			num = num[placeholder:]
		elif  length > 6: 
			placeholder = length - 6
			millon = num[:placeholder]
			results.append(hundreds_breakdown(millon) + " millon,")
			num = num[placeholder:]
		elif length > 3: 
			placeholder = length - 3
			thousand = num[:placeholder]
			results.append(hundreds_breakdown(thousand) + " thousand,")
			num = num[placeholder:]
	results.append(hundreds_breakdown(num))
	return results

def hundreds_breakdown(num): 
	ones_dictionary = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
	two_dictionary = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
	doubles_dictionary = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
	results = []
	num = str(int(num))
	print "this is the hundreds num: ", num
	if len(num) == 3: 
		results.append(ones_dictionary[int(num[0])] + " hundred ")
		num = num[1:]
	if len(num) == 2: 
		if int(num) in two_dictionary: 
			results.append(two_dictionary[int(num)])
		if int(num) in doubles_dictionary: 
			results.append(doubles_dictionary[int(num)])
		else: 
			results.append(doubles_dictionary[int(num[0])] + "-" + ones_dictionary[int(num[1])])
	if len(num) == 1: 
		if int(num) == 0: 
			pass
		else: 
			results.append(ones_dictionary[int(num)])
	return "".join(results)

print (translate_num(1000))








