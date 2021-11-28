#!/bin/python
#Released entirely in the Public Domain!! ;)
from vtt_to_srt.vtt_to_srt import vtt_to_srt

print("Welcome to rtsrt.py!")
srt = input("Path to subtitle file: ")


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

def open_srt(filename: str) -> None:
	with open(filename, "r") as file:
		srtl = file.read().split("\n")
		file.close()

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

	with open(filename, "w") as file:
		file.write(''.join(str(x)+"\n" for x in srtl))
		file.close()
		
def menu() -> int:
	rv = input("Would you like to:\n (1) Convert VTT to SRT, or\n (2) Check SRT file\n (3) Exit Application\n:")
	if rv == "1":
		return 0
	elif rv == "2":
		return 1
	elif rv == "3":
		return 2
	else:
		print("Not a valid option")
		menu()

resp = menu()
if resp == 0:
	vtt_to_srt(srt)
elif resp == 1:
	open_srt(srt)
	

print("Thank you for using rtsrt! Remember to always double-check your subtitles!! ;)")





