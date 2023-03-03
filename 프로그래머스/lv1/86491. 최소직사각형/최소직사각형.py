def solution(sizes):

    max_w = 0
    max_h = 0
    
    for i in range(len(sizes)):
        max_w = max(max_w,max(sizes[i]))
        max_h = max(max_h,min(sizes[i]))

    return max_w * max_h