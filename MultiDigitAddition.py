# Author: Omoju 
# This is the algorithm kids learn in elementary school to do multi-digit Addition
#!/usr/bin/python

import sys
A = sys.argv[1]
B = sys.argv[2]  

# Determine the number of  digits that make up each number, assuming the numbers are named A and B

length_first = len(str(A))
length_second = len(str(B))
print("You entered", A, " and ", B, "their lengths are", length_first, length_second)

bigger = length_first if length_first > length_second else length_second
bigger_num = max(A,B)
smaller_num = min(A,B)

# Declare a data structure the size of the largest number
first_number = [0] * bigger
second_number = [0] * bigger
answer = [0] * bigger

# Now put the numbers in the conventional format so that we can align correctly
# A = 999998, and B = 9
# [9, 9, 9, 9, 9, 8]
# [0, 0, 0, 0, 0, 9]
# determine by how many digits are the numbers bigger than each other
digit_difference = (bigger - length_first) if (bigger - length_second) < (bigger - length_first) else (bigger - length_second)

for number in range (0,bigger):
    first_number[number] = int (str(bigger_num)[number])

for number in range(0,digit_difference):
	second_number[number] = 0

for number in range(digit_difference, length_second + digit_difference):
	second_number[number] = int (str(smaller_num)[number - digit_difference])

# Now we can start adding digits that are in the same indexes
# However, we need to make sure we handle the carry over case
index = bigger
carry = 0
carry_flag = 0


# After first pass through the loop
# following our example numbers, answer now has [0, 0, 0, 0, 0, 7]
# decrement the index to move on to the next position

while index:
	#determine if the index addition results in two digits
	temp = first_number[index-1] + second_number[index-1] + carry
	carry_flag = 1 if len(str(temp)) > 1 else 0
	# update the answer by inserting the rigthmost digit of temp in the right index and store the carry
	if carry_flag:
		answer[index-1] = int(str(temp)[1])
		carry = int(str(temp)[0])
	else:
		answer[index-1] = temp

	index = index - 1
	print index


# This part handles the reassembling of the number
# We can use our knowledge that the number is in base 10, to reassamble it
# for example 999998 is actually
# (10^5 * 9) + (10^4 * 9) + (10^3 * 9) + (10^2 * 9) + (10^1 * 9) + (10^0 * 8), where ^ stand for raised to the power
# There is an error in this last for loop 
for x in xrange(bigger-1, -1, -1):
	answer[abs(x-bigger-1)] = pow(10,x) * answer[abs(x-bigger-1)]



print "The answer is "
print pow(10,bigger) * carry + sum(answer)

