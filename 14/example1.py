for x in range(5769, 0, -1):
	e = 9**2025 + 9**1000 - x
	x9 = ''
	while e > 0:
		x9 += str(e % 9)
		e //= 9
	x9 = x9[::-1]
	if x9.count('0') == 1026:
		print(x)
		break
