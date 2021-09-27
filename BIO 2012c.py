import statistics
from statistics import mode
## get number
##n = int(input("input number between 1 and 1,000,000"))

## Function to return a distinct prime
def dist_prime(myNum):
    #prime factor list
    prime_fact = []
    p_flag = False
    # start at 2
    i = 2
    while i < myNum:
        p_flag = False
        #while num divides by counter keep dividng
        while myNum % i == 0:
            # reeduce number by factor
            myNum = int(myNum / i)
            # if not lready in list add it
            if p_flag == False:
                prime_fact.append(i)
                p_flag = True
        # end while
        # next number
        i = i + 1
    # Next

    # Add final number if not 1
    if myNum != 1:
        prime_fact.append(myNum)

    tot = 1
    for j in range (0,len(prime_fact)):
        tot = tot * prime_fact[j]
    return (tot)

# end function

counter = 2
dist_prime_list = []

for counter in range (1,1000000):
    if counter % 210 == 0:
        dist_prime_list.append(dist_prime(counter))
# end for

print (mode(dist_prime_list))
