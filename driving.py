country = input('请问你是哪国人？')
if country == '中国':
	print('你可以考试')
else:
	print('回自己国家去吧')

age = input('你的年龄是多少？')
age = int(age)

if age >= 18:
	print('你可以考驾照')
else:
	print('成年了再来吧臭小子！')

#================================================
country = input('你是哪国人')
age = input('你的年龄')
age = int(age)
if country == '中国':
	if age >= 18:
		print('你可以考驾照')
	else:
		print('你还不能考驾照')
elif country == '美国':
	if age >= 16:
		print('take you driving test')
	else:
		print('you can not take test')
else:
	print('only US and China are available')
	print('你只能输入中国或美国')