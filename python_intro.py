print ('Hello, Django Girls')
name = "paula"
print(name)
lijst = [2, 5, 7, 11]
print(lijst)
deelnemer = {'name': 'paula', 'land': 'nederland', 'plaats': 'gemert'}
print(deelnemer)
print(True and True)

if 3>2:
	print('it works!')

print("Ik heet Paula en ik leer Python!")

if 5>2:
	print('5 is inderdaad groter dan 2')
else:
	print('5 is helemaal niet groter dan 2')

name = 'Sonja'
if name == 'Ola':
	print('Hey Ola!')
elif name == 'Sonja':
	print('Hey Sonja')
else:
	print('Hey anonymous')

volume = int(input("Hoe hoog is het volume? "))
# Vraag hoe hoog het volume staat om te kijken of het te hoog is.
if volume < 20:
	print("It's kinda quiet.")
elif 20 <= volume < 60:
	print("Perfect, I can hear the details.")
elif 60 <= volume < 80:
	print("Nice for parties.")
elif 80<= volume < 100:
	print("a bit loud!")
else:
	print("My ears are hurting! :(")
	#pas volume aan
	volume = int(input("pas het volume aan naar tussen de 20 en 60 "))
	if 20 <= volume < 80:
		print("Dat is beter")
	else:
		print("probeer het nog eens")


