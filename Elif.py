print("Enter your marks")
marks=int(input())
if marks<40:
    print("Sorry you have not passed.")
elif marks>75 and marks<100:
    print("You have passed with distinction!")
elif marks>=100:
    print("You are the top scorer. A perfect score")
else:
    print("You have passed!")