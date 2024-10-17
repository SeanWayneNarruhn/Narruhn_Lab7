""

name= input("What is yur name? ")
section= input("What is your section? ")
Prelim= float(input("What is your Grade on Prelim? "))
if Prelim <40 or Prelim > 100:
    print("\nError, please enter a Grade between  40 and 100")

    exit()

Midterm= float(input("What is your Grade on Midterm? "))
if Midterm <40 or Midterm > 100:
    print("\nError, please enter a Grade between  40 and 100")
    exit()

Finals= float(input("What is your Grade on Finals? "))
if Finals <40 or Finals > 100:
    print("\nError, please enter a Grade between  40 and 100")
    exit()

FinalGrade= float(Prelim + Midterm + Finals) /3
FinalGrade= round(FinalGrade)
if FinalGrade <=100 and FinalGrade >=99:
    print("\nYou have a 1.00 Grade Points, Excellent!")
elif FinalGrade >=96 and FinalGrade <=98:
    print("\nYou have a 1.25 Grade Points, Outstanind!")
elif FinalGrade >=93 and FinalGrade <=95:
    print("\nYou have a 1.50 Grade Points, Superior!")
elif FinalGrade >=90 and FinalGrade <=92:
    print("\nYou have a 1.75 Grade Points, Very Good!")
elif FinalGrade >=87 and FinalGrade <=89:
    print("\nYou have a 2.00 Grade Points, Good!")
elif FinalGrade >=84 and FinalGrade <=86:
    print("\nYou have a 2.25 Grade Points, Satisfactory!")
elif FinalGrade >=81 and FinalGrade <=83:
    print("\nYou have a 2.50 Grade Points, Fairly Satisfactory!")
elif FinalGrade >=78 and FinalGrade <=80:
    print("\nYou have a 2.75 Grade Points, Fair!")
elif FinalGrade >=75 and FinalGrade <=77:
    print("\nYou have a 3.00 Grade Points, Passed!")
elif FinalGrade <75 and FinalGrade >=40:
    print("\nYou have a 5.00 Grade Points, Failed")
else: print("\nError")