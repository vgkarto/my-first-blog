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