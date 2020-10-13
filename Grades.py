def grade_obtained(percentage):
	if (percentage >= 60) :
		print("1st Division")
	elif (percentage >= 50 and percentage <= 59) :
		print("2nd Division")
	elif (percentage >= 40 and percentage <= 49) :
		print("3rd Division")
	else:
		print("Fail")

total = 0 #Initializing variable
print("Please enter your marks out of 100")
for i in range(1, 6):
    subject = float(input("Please enter your marks of subject " + str(i) + ": "))
    if 0 >= subject or subject >= 100: #Eliminating invalid inputs
        print("Invalid input")
        exit()
    total += subject


percentage = (total) / 500 * 100
print("Percentage optained : " + str(percentage))
print("Grade obtained : ")
grade_obtained(percentage)
