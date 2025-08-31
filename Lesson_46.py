vel_num_1 = float(input())
vel_num_2 = float(input())
c = str(input())
if c == "+":
    print (vel_num_1+vel_num_2)
elif c == "-":
    print (vel_num_1-vel_num_2)
elif c == "*":
    print (vel_num_1*vel_num_2)
elif c == "/":
    print (vel_num_1/vel_num_2)
elif c == "**":
    print (vel_num_1**vel_num_2)
elif c == "//":
    print (vel_num_1//vel_num_2)
elif c == "%":
    print (vel_num_1%vel_num_2)
else:
    print("ERROR")