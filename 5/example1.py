for N in range(1000):
	b = bin(N)[2:]
	if N % 2 == 0:
		b = b.replace('1', '11')
	else:
		b = b.replace('0', '00')
	R = int(b, 2)
	if R > 70:
		print(N)
		break
