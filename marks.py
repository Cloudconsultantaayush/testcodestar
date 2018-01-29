marks = int(input("Please write the percentage of candidate"))
if(marks>80):
    print('Grade A')
elif (marks>60) and (marks<=80):
        print('Grade B')
elif (marks>40) and (marks<=60):
        print('Grade C')
else:
    print('Grade D')