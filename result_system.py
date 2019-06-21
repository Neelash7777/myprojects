more=True #Here 'more' is 'True' to run the while loop for once atleast.
while more==True:
    '''Taking marks from user'''
    name=input("Enter your name>>>")
    science_marks=int(input("Science marks>>>"))
    maths_marks=int(input("Maths marks>>>"))
    english_marks=int(input("English marks>>>"))
    hindi_marks=int(input("Hindi marks>>>"))
    total_marks=science_marks+maths_marks+english_marks+hindi_marks
    percentage=float((total_marks/400)*100)
    print(name,",your total marks are",total_marks,"and your percentage is",percentage)
    Run_=input("want to enter more y/n>>>") #user has to enter y to run it again.
    if Run_!="y":
        more=False # IF user enters anything other than 'y', then making 'more' to 'False' to stop the loop.