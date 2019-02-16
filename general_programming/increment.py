# This is program to increment a number in any number system

number_system = ['A', 'B', 'C', 'D']
	
def get_next(character):
	return number_system[(number_system.index(character) + 1) % 4]

def increment_number(num):
	result = list(num)
	for character in num[ : : -1]:
		flag = False 
		char = get_next(character)
		if char != number_system[0]:
			result.remove(character)
			result.insert(result.index(character), char)
			return result
		else:
			result.remove(character)
			result.insert(result.index(character), char)
			flag = True 
	if flag:
		result.insert(0, number_system[0])
	return result 

print(increment_number('AB'))
# 'BA'
# AD
# BA
# ['BD']