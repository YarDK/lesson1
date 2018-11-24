#user_info = {"first_name":"Yaroslav", "last_name":"Korotyshov"}
#print(user_info.get("first_name"))
#print(user_info["first_name"])

# Обычная функци
def function1 (a,b):
	result = a + b
	return result
print(function1(3,5))

# Лямда функция
function2 = lambda a, b: a+b
print(function2(5,5))

# Функция с динамичиными аргументами
def function3 (*c):
	result = 0
	for i in c:
		result = result + i
	return result
print(function3(5,5,5,5,5,5,5,5,5,5))

#Задача по курсу, сделать буквы заглавными
def get_summ(one, two, delimiter="&"):
	result = str(one.upper()) + str(delimiter) + str(two.upper()) 
	return result
print(get_summ("Learn","python"))


