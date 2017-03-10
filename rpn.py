#!/usr/bin/env python3

def calculate(arg):
	exIn = arg.split(' ')
	stack = []
	ops = ['+', '-']
	val = 0
	for ex in exIn:
		if (ex.isnumeric()):
			stack.append(int(ex))
		elif (ex in ops):
			if (len(stack) < 2):
				print('Error: Operation defined before valid numbers')
			else:
				if(ex == '+'):
					val = 0
					while (len(stack) > 0):
						val = val + stack.pop()
					stack.append(val)
				elif(ex == '-'):
					stack.reverse()
					val = stack.pop()
					while(len(stack) > 0):
						val = val - stack.pop()
					stack.append(val)
		else:
			print('Error: Invalid character entered')
			break
	return(val)




def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()