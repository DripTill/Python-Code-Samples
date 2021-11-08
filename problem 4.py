# Miguel Jusino
# running a rang of numbers to 50 and showing what the number is divisiable by
for i in range(0, 51):
    if i % 3 == 0:
        print(i,"- divisble by 3")
    elif i % 5 ==0:
        print(i, "- divisble by 5")
    else:
        print(i, "- divisble by both")
