def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        s = ""
        for a in tree:
            if a in skill:
                s += a
        
        if s == skill[:len(s)]:
            answer += 1

    return answer