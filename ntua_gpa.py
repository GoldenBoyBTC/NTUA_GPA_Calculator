# -*- coding: utf-8 -*-
#GPA calculator for the National Technical University of Athens, Greece

print ("\nGPA calculator for the National Technical University of Athens (Greece) | Author: Pavlos Mparitakis.")

while True:
	
	try:

	#GPA of the classes required for the Master of Engineering degree with a rate of 80% (4/5)
		
		Μέσος_Όρος_Μαθημάτων = float(input("\nΠοιος είναι ο μέσος όρος των μαθημάτων σου?: "))

		if 5 <= Μέσος_Όρος_Μαθημάτων <= 10:
			break
		print("\nOops! Για την απόκτηση διπλώματος ο μέσος όρος των μαθημάτων πρέπει να είναι από 5 μέχρι 10. Δοκίμασε ξανά.")

	except ValueError:
		print("\nOops! Γράψε το μέσο όρο των μαθημάτων χρησιμοποιώντας μόνο αριθμούς. Για δεκαδικούς αριθμούς χρησιμοποίησε τελεία (.) αντί για κόμμα (,). \nπχ 8.5 και όχι 8,5")

while True:

	try:

    #GPA of the masters' thesis with a rate of 20% (1/5)

		Βαθμός_Διπλωματικής = float(input("\nΠοιος είναι ο βαθμός της διπλωματικής σου?: ")) 
		
		if 5.5 <= Βαθμός_Διπλωματικής <= 10: 
			break 
		print("\nOops! Για την απόκτηση διπλώματος ο βαθμός της διπλωματικής πρέπει να είναι από 5.5 μέχρι 10. Δοκίμασε ξανά.") 

	except ValueError:
		print("\nOops! Γράψε το βαθμό της διπλωματικής χρησιμοποιώντας μόνο αριθμούς. Για δεκαδικούς αριθμούς χρησιμοποίησε τελεία (.) αντί για κόμμα (,). \nπχ 8.5 και όχι 8,5")


#Total GPA
Βαθμός_Διπλώματος = (0.8*Μέσος_Όρος_Μαθημάτων) + (0.2*Βαθμός_Διπλωματικής)

if 5 <= Βαθμός_Διπλώματος < 7:
	print("\nΕπίδοση = Καλώς!")
		
if 7 <= Βαθμός_Διπλώματος < 9:
	print("\nΕπίδοση = Λίαν Καλώς!!")
		
if 9 <= Βαθμός_Διπλώματος <= 10:
	print("\nΕπίδοση = Άριστα!!!")  

print ("\nΟ βαθμός του διπλώματός σου (GPA) είναι", "%.2f" % Βαθμός_Διπλώματος + ".", "Συγχαρητήρια για την αποφοίτησή σου!!!")

input("\nPress ENTER to exit...")
