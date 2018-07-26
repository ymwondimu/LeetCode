import math
from statistics import mean

def median_two_sorted(arr1, arr2):
    i = 0
    j = 0

    n1 = len(arr1)
    n2 = len(arr2)

    sorted_arr = []

    while (i < n1 or j < n2):
        if i == n1:
            sorted_arr.append(arr2[j])
            j+=1

        elif j == n2:
            sorted_arr.append(arr1[i])
            i+=1
        else:
            if arr1[i] < arr2[j]:
                sorted_arr.append(arr1[i])
                i += 1
            else:
                sorted_arr.append(arr2[j])
                j += 1

    return sorted_arr


def main():
    arr1 = [1,2, 60, 84, 90]
    arr2 = [2,9, 12, 13]

    final = median_two_sorted(arr1,arr2)
    print (final)

    if len(final) % 2 == 1:
        median_index = math.floor(len(final)/2)
        median = final[median_index]
        print (median)
    else:
        ind1 = int(len(final)/2)-1
        ind2 = int(len(final)/2)
        val1 = final[ind1]
        val2 = final[ind2]
        median = mean([val1,val2])
        print (median)

if __name__ == "__main__":
    main()
