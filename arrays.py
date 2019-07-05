# students = ('gideon', 'samuel','ayo','tomisin')
# # students[1] ='olamide'
# print(students[1])
# # students {'kslg','hslgls','jhfhwsoh'}
# gideon = {'eyes':2, 'Name':'gideon','legs':2}
# print('gideon',eyes)

"""
block = eval(input('no of block: '))
lines = eval(input('no of lines: '))
start = eval(input('enter starting num: '))
noOfLines = lines + start
for i in range(1,block+1):
	for j in range(start,noOfLines):
		print(i,'*', j, '=', i*j,)
		if(j == noOfLines-1):
			print('-------------')
"""
# for i in range(1,13):
# 	print('1','*',i, '=',1*i)

# for i in range(1,13):
# 	print('2','*',i, '=',2*i)

# for x in 'Gideon':
# 	if x != 'd':
# 		print(x)
# 	else:
# 		break
# 	print(x)

"""
s = len('string')
print(s)
"""

s = ''
for i in range(10):
	t = input('enter a lettter: ')
	if t == 'a' or t == 'e' or t == 'i' or t == 'o' or t == 'u':
		s = s + t
print(s)
