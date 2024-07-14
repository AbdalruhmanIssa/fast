names=input("enter names:").title().split(',')  
ass=input("enter assCount:").split(',')  
grades=input("enter grades:").split(',')  
for name,ac,grade in zip(names,ass,grades):
    print("Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n".format(name,ac,grade,int(grade)+(int(ac)*2)))