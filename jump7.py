for i in range(100):
	flag = 0
	num = i
	while num > 0:
		tmp = num % 10
		num = num / 10
		if tmp == 7:
			flag = 1
			break
	if flag == 1 or i % 7 == 0:
		continue
	print(i)
