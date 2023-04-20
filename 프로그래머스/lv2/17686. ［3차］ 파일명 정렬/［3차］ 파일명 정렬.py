import re
def solution(files):
    
    tmp = [re.split('(\d+)', file) for file in files]
    print(tmp)
    
    sort = sorted(tmp, key = lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(s) for s in sort]