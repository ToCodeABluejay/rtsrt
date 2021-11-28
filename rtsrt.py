#!/bin/python
#Released entirely in the Public Domain!! ;)
srt = input("Path to SRT file: ")

with open(srt, "r") as file:
	srtl = file.read().split("\n")
	file.close()

def double_lines(val: int, ll: list) -> bool :
	print("Found two lines of text in a row. The first one says:")
	print(ll[val], end="\n\n")
	print("And the second one says:")
	print(ll[val+1])
	x = input("Would you like to delete one? (y/n) ")
	if x == "y" :
		return True
	elif x != "n" :
		print("Not a listed option.")
		double_lines(val, ll)
	else:
		return False
		

def del_prompt() -> int :
	x = input("Would you like to remove the first or the second? (1/2) ")
	if x == "1" :
		return 0
	elif x == "2" :
		return 1
	else :
		print("Not a valid response")
		del_prompt()

dl = list()
for i in range(len(srtl)) :
	if srtl[i] == "\ufeff1" :
		pass
	elif srtl[i] != "" and not srtl[i][0].strip("\n/, ->").isnumeric() :
		if srtl[i+1] != "":
			k = double_lines(i, srtl)
			if k :
				j = del_prompt()
				dl.append(i+j)
			else:
				pass
for i in dl :
	del srtl[i]

with open(srt, "w") as file:
	file.write(''.join(str(x) for x in srtl))
	file.close()

print("Thank you for using rtsrt! Remember to always double-check your subtitles!! ;)")





