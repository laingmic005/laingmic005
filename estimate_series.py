def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

def eval_series(begin, degree):
    
    aOfN = []
    sOfN = []
    for i in range(int(begin),int(degree)):
        value = i                #input your equation on this line!!
        aOfN.append(value)
        sOfN.append(sum(aOfN))
    
    print("A-series:")
    for j in range(len(aOfN)):
        print(f"{j+int(begin)}: ",aOfN[j])
    print("\nS-series:")
    for k in range(len(sOfN)):
        print(f"{k+int(begin)}: ",sOfN[k])

eval_series(input("What is the starting value for n?"),input("To what degree do you wish to estimate the sum?: "))
