
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None#虛無
	allenword = 0
	allenstiker = 0
	allenimage = 0
	vikiword = 0
	vikistiker = 0
	vikiimage = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allenstiker = allenstiker + 1
			elif s[2] == '圖片':
				allenimage = allenimage + 1
			else:
				for m in s[2:]:
					allenword = allenword + len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				vikistiker = vikistiker + 1
			elif s[2] == '圖片':
				vikiimage = vikiimage + 1
			else:
				for m in s[2:]:
					vikiword = vikiword + len(m)
	print('allen說了', allenword, '個字；傳了', allenstiker, '個貼圖；傳了', allenimage, '張圖片')
	print('viki說了', vikiword, '個字；傳了', vikistiker, '個貼圖；傳了', vikiimage, '張圖片')


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('-LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)


main()#程式進入點