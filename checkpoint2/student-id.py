def main():
	print('')
	print('Please enter the following information to create your ID Card.')
	input('Press enter to continue.')
	
	FN = input("Please enter your First Name: ").title()
	LN = input("Please enter your Last Name: ").capitalize()
	EA = input("Please enter your Email Address: ")
	PN = input("Please enter your Phone Number: ").replace("0" "1" "2" "3" "4", "*")
	FPT = input("Please enter your FPT class: ")
	YR = input("What year are you entering in? ")
	FS = input("What is your favorite subject? ").title()
	EX = input("Are you participating in any extracurricular activity? ").title()	

	print("Your ID Card is:")
	line = "-" *45
	print(line)
	print(f"{LN}, {FN}")
	print("Student")
	print("ID: 345236453")
	print("\n")
	print(EA)
	print(PN)

main()