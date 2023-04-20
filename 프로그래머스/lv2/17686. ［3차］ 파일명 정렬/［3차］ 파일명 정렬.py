import re
def solution(files):
    
    arr = []
    for file in files:
        head,number,tail = re.match(r'([\D]+)(\d{1,5})([\S ]*)',file).groups()
        arr.append([head,number,tail])
    
    arr.sort(key=lambda x:(x[0].lower(),int(x[1])))    
    return [''.join(data) for data in arr]