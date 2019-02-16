# # program to check whether given string is palindrome or not

# def check_palindrome(string):

# 	if not string:
# 		return True

# 	else:
# 		front = 0
# 		back  = len(string) - 1
# 		while front <= back:

# 			while string[front : front + 1] == ' ':
# 				front += 1

# 			while string[back : back + 1] == ' ':
# 				back -= 1

# 			if string[front : front + 1] != string[back : back + 1]:
# 				return False

# 			front += 1
# 			back  -= 1

# 		return True

# print(check_palindrome('che tan nateh c'))

