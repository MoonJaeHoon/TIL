data1 = [7,4,2,0,0,6,0,7,0]

def gravity(data1):
    max_diff = 0
    for left_ind in range(len(data1)):
        diff=0
        for right_ind in range(left_ind+1,len(data1)):
            if data1[left_ind]>data1[right_ind]:
                diff += 1
        max_diff = diff if diff>max_diff else max_diff
    return max_diff

print(gravity(data1))