
A=(60*60)
print(A)
3600
seconds_per_hour= A
print(seconds_per_hour)
3600
B=(seconds_per_hour*24)
print(B)
86400
seconds_per_day= B
print(seconds_per_day)
86400
C=(seconds_per_day/seconds_per_hour)
print(C)
24.0
D=(seconds_per_day//seconds_per_hour) 
print(D)
    #Both C and D are equal despite the removal of the decimal thanks to the use of
    # interger divison.