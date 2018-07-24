import numpy as np
#Definition of the function to find the moving average taking the input array and window size

def mov_avg(input, N):
    ln = len(input)
    output = []
    #using a for loop to find the moving average over the array

    for i in range(ln-N+1):
        i = (np.sum(input[i:(i+N)]))/N
        j = round(i,3) #rounding off upto 3 decimal places
        output.append(j)    #populating the output array with mean values
    return output


l = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
window = 3
print(mov_avg(l,window))
