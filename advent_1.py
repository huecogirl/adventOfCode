'''
For example, if the device displays frequency changes of +1, -2, +3, +1, then starting from a frequency of zero, the following changes would occur:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
In this example, the resulting frequency is 3.

Here are other example situations:

+1, +1, +1 results in  3
+1, +1, -2 results in  0
-1, -2, -3 results in -6
Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?
'''

temp = [
	3, 
	9, 
	-5,
	2,
]

freq_list = []
def add_freq(data):
	
	total_frequency = sum(data)
	
	return total_frequency


txt = open("data/data1.txt", "r")
for number in txt:
	#print(number)
	number = int(number)
	freq_list.append(number)
print(freq_list)

print(add_freq(freq_list))
