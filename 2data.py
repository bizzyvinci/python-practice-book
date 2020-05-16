# https://anandology.com/python-practice-book/working-with-data.html

'''
#Problem 1: [0,1,[3]] \n [0,1,[3,4]] \n [0,1,2]
x=[0,1,[2]]
x[2][0]=3
print(x)
x[2].append(4)
print(x)
x[2]=2
print(x)
'''


'''
#Problem 2: Kinda boring
print(sum([1,2,3,4,5]))
'''


'''
#Problem 3: Wow, I just decided to take it a bit further and experiment with built-in function 
print(sum([1,2,3,4]))
def sum(string_list):
	ans=""
	for x in string_list:
		ans+=x
	return ans*2
print(sum(['hey', ' yo', ' buddy']))
#ERROR for summing unrelated datatype: print(sum([1,2,3,4]))
'''


'''
#Problem 4 and 5:
def product(p):
	ans=1
	for x in p:
		ans*=x
	return ans
def factorial(num):
	ls=[]
	for x in range(1,num):
		ls.append(x)
	return product(ls)*num
print(product([1,2,3,4,10]))
print(factorial(6))
'''


'''
#Problem 6: 
def reverse(p):
	ans=[]
	for x in range(0,len(p)):
		ans.append(p.pop())
	return ans
print(reverse([1,2,3,4]))
'''


'''
#Problem 7: abc to z \n -10 to 22
a=['hey','abc','abcd','adb','z']
x=[1,3,5,22,5,-10]
print('from', min(a), 'to', max(a))
print('from', min(x), 'to', max(x))
'''


'''
#Problem 8 and 9: find cumulative sum and cumulative product respectively
def cumulative_sum(p):
	cs=0
	sum_list=[]
	for x in p:
		cs+=x
		sum_list.append(cs)
	return sum_list
def cumulative_product(p):
	cp=1
	product_list=[]
	for x in p:
		cp*=x
		product_list.append(cp)
	return product_list
print(cumulative_sum([1,2,3,4]))
print(cumulative_sum([4,3,2,1]))
print(cumulative_product([1,2,3,4]))
print(cumulative_product([4,3,2,1]))
'''


'''
#Problem 10: print unique elements of a list
def unique(p):
	p.sort()
	ans=[]
	for x in range(0,len(p)-1):
		if p[0]==p[1]:
			p.pop(0)
		else:
			ans.append(p.pop(0))
		print(x)
	ans.append(p.pop(0))
	return ans
print(unique([1,2,3,1,2,5]))
'''


'''
#Problem 11: Find duplicates
def dups(p):
	p.sort()
	#The initial value is given to prevent error (list out of range) from the if below
	ans=[0]
	for x in range(0,len(p)-1):
		if p[x]==p[x+1]:
			if p[x]!=ans[len(ans)-1]:
				ans.append(p[x])
	#Pop out the 0
	ans.pop(0)
	return ans
print(dups([1,2,1,4,3,4,5]))
'''


'''
#Problem 12: Split ls into smaller lists of length num
def group(ls,num):
	flr=len(ls)//num
	ans=[]
	for x in range(0,flr):
		t=ls[x*num:x*num+num]
		ans.append(t)
	if len(ls)>flr*num:
		t=ls[flr*num:]
		ans.append(t)
	return ans
print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
'''


'''
# Problem 13: sort list based on string length
def lensort(ls):
	ls.sort(key=lambda x: len(x))
	return ls
print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))
'''


'''
# Problem 14: print unique elements of a list based on a key function
# I initially copied from #10 but I had issue, it was very difficult for me so I used the internet
# It's really better so I change the whole method from #10
# I leave #10 for future comparison purpose. Shit, why did I include the pop() before.
# Hmm, wait. Is mine more effective?
def unique(ls, key):
	uniq=[]
	for x in ls:
		if key(x) not in uniq:
			uniq.append(key(x))
	return uniq
print(unique(["python", "java", "Python", "Java"], key=lambda s: s.lower()))
'''


'''
# Problem 15: It's unique again. But this time, using set datatype
def unique(ls):
	return list(set(ls))
print(unique([1,2,3,1,2,5]))
# Eazy Peazy
'''


'''
# Problem 16:
def extsort(ls):
	ls.sort(key=lambda x: x.split('.')[1])
	return ls
print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))
# hahaha, that was so easy too
'''


'''
# Problem 17: print lines of a file in reverse order
def reverse(file):
	in_file=open(file, 'r')
	in_lines=in_file.readlines()

	# I just felt like outputing in a different file
	x=file.split('.')
	x[0]+='_out'
	new_file='.'.join(x)

	out_file=open(new_file, 'w')
	out_lines=out_file.writelines(in_lines[::-1])

	# Close files because it's good practise
	in_file.close()
	out_file.close()
reverse('she.txt')
# Success. Did I made it more complicated?
'''


# Problem 18: Doesn't look any different from 17

# Problem 19: Waoh. The unix 'head' and 'tail' commands take a file as argument and print its first and last 10 lines respectively
# e.g head she.txt

# Problem 20: The unix 'grep' command takes a string and a file as arguments and prints all lines in the file which contain the specified string
# e.g grep sure she.txt


'''
# Problem 21: wrap lines with char length greater than width
def wrap(file, width):
	in_file=open(file, 'r')
	in_lines=in_file.readlines()			
			
	# I just felt like outputing in a different file
	x=file.split('.')
	x[0]+='_out'
	new_file='.'.join(x)
	out_file=open(new_file, 'w')

	for line in in_lines:
		if len(line)>width:
			line=line[:30]+'\n'+line[30:]
		out_file.write(line)

	out_file.close()
	in_file.close()

wrap('she.txt', 30)
'''


'''
# Problem 22: wrap words with char length greater than width
def word_wrap(file, width):
	in_file=open(file, 'r')
	in_lines=in_file.readlines()			
			
	# I just felt like outputing in a different file
	x=file.split('.')
	x[0]+='_out'
	new_file='.'.join(x)
	out_file=open(new_file, 'w')

	for line in in_lines:
		if len(line)>width:
			i=29
			while i>0:
				if line[i]==' ':
					break
				i-=1
					
			line=line[:i+1]+'\n'+line[i+1:]		# +1 is to avoid including the space in the next line
		out_file.write(line)
		#print(line)

	out_file.close()
	in_file.close()

word_wrap('she.txt', 30)
'''


'''
# Problem 23: Center align texts
def center_align(file):
	in_file=open(file, 'r')
	in_lines=in_file.readlines()
	max_len=len(max(in_lines, key=lambda x:len(x)))


	
	# Haha, another method to name the out_file the same way
	x=file.split('.')
	x[0]+='_out'
	out_file=open(x[0]+'.'+x[1], 'w')
	
	for line in in_lines:
		n=len(line)
		if n<max_len:
			space=(max_len-n)//2
			line=' '*space+line
		out_file.write(line)

	out_file.close()
	in_file.close()
	return True
center_align('she.txt')
'''


'''
#Problem 24: Implement zip
print(zip([1,2,3], ["a", "b", "c"]))
'''


'''
# Problem 25 & 26: Implement map and filter
square=lambda x: x*x
even= lambda x: x%2==0

print(map(square, range(10)))
print(filter(even, range(10)))
'''


'''
# Problem 27: return (x,y,x+y) for range(0,n). NOTE: x,y == y,x
def triplets(n):
	ls=[]
	for x in range(1,n):
		for y in range(1,x//2+1):
			ls.append((y,x-y,x))
	return ls
print(triplets(5))
# Kinda weird how I did this almost unconsciously and easily
'''


'''
# Problem 28: return (index, item)
def enumerate(ls):
	out=[]
	for x in range(0, len(ls)):
		out.append((x,ls[x]))
	return out

a=["a", "b", "c", "d"]
print(enumerate(a))
for index,value in enumerate(a):
	print(index, value)
'''


'''
# Problem 29: Create 2-dimensional array with initial values of None
def array(i,j):
	return [[None]*j]*i
print(array(2,3))
'''


'''
Problem 30 and 31 works on csv. It's easy just readlines and split()
Ignore #... (I think split(#) should come first then split(',') for x[0])
Easier said than done though
'''


'''
# Problem 32 & 33: Word Mutation
# Note: String is non-iterable. That's why I'm working with list

# Problem 32
def mutate(s):
	a_z=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
	store=tuple(s)
	ls=list(store)
	mut=[s]

	# Swap [i] and [i+1]
	for i in range(0, len(store)-1):
		ls[i], ls[i+1] = ls[i+1], ls[i]

		# str(ls) didn't work as I expected so I went for join(ls)
		mut.append("".join(ls))

		# Necessary to always reset the ls to its initial value
		ls=list(store)

	for i in range(0, len(store)):
		# Remove [i]
		ls.pop(i)
		mut.append("".join(ls))
		ls=list(store)

		
		for alphabet in a_z:
			# Insert a-z at [i]
			ls.insert(i,alphabet)
			mut.append("".join(ls))

			# Replace [i] with a-z
			ls.pop(i+1)
			mut.append("".join(ls))
			ls=list(store)

	# Insert a-z at the end
	for alphabet in a_z:
			ls.append(alphabet)
			mut.append("".join(ls))
			ls=list(store)
	

	return mut

# Problem 33:
def nearly_equal(x,y):
	return x in mutate(y)

print(nearly_equal('man', 'woman'))
'''


'''
# Problem 34: word count from file
def word_frequency(words):
	frequency={}
	for w in words:
		frequency[w]=frequency.get(w,0)+1
	return frequency

def read_words(filename):
	return open(filename).read().split()

def main(filename):
	frequency=word_frequency(read_words(filename))

	# The main problem: Sort frequency is descending order
	# sorted returns a list. and frequency.items is also a list of key,value(word, count) pairs
	fr={word:count for word, count in sorted(frequency.items(), key=lambda item: item[1], reverse=True)}
	for word, count in fr.items():
		print(word, count)

if __name__=="__main__":
	import sys
	main(sys.argv[1])
'''


'''
# Problem 35: Character count from file. Then probably predict if it is txt or C program file
# I don't really know how C file look like. I guess it contains '(', ')', '{', '}' and most importantly ';'
# Anyway, I don't think that's enough to predict and I'll need a lot of C files to test. So, I'll just skip that.
def character_frequency(words):
	fr={}
	for w in words:
		for c in w:
			fr[c]=fr.get(c,0)+1
	return fr

def read_characters(filename):
	# Returns a list of words, where each word is a list of character
	return [list(word) for word in open(filename).read().split()]

def main(filename):
	fr=character_frequency(read_characters(filename))

	# Similar to problem 34 above
	sorted_fr={char:count for char, count in sorted(fr.items(), key=lambda item: item[1], reverse=True)}
	for character, count in sorted_fr.items():
		print(character, count)

if __name__=="__main__":
	import sys
	main(sys.argv[1])
'''


'''
# Problem 36: Find anagrams in a given list of words
def anagrams(words):
	dic={}
	for w in words:
		dic[w]=str(sorted(w))	# Converted to string because list in unhashable and therefore cannot be used as key in a dictionary
	result={}

	for word,pattern in dic.items():
		if pattern in result:
			result[pattern].append(word)
		else:
			result[pattern]=[word]

	return list(result.values())	
	# Python3+ return views instead of lists for keys, items and values methods. Therefore cannot be accessed by indexing
	# More at https://portingguide.readthedocs.io/en/latest/dicts.html

words=['eat', 'ate', 'done', 'tea', 'soup', 'node']
print(anagrams(words))
'''


'''
# Problem 37: Sort values of a dictionary based on the key
def valuesort(dic):
	return [dic[key] for key in sorted(dic.keys())]
dic={'x':1, 'y':2, 'a':3, 'D':-2, 'd': 10}
print(valuesort(dic))
'''


'''
# Problem 38: Interchange keys and values in a dictionary
def invertdict(dic):
	x=[]
	return {value:key for key,value in dic.items()}
dic={'x':1, 'y':2, 'a':3, 'D':-2, 'd': 10}
print(invertdict(dic))
'''

