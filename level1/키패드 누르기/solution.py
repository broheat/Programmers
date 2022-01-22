def solution(numbers, hand):
    position = ""
    L = [1,4,7]
    R = [3,6,9]
    L_position = 10
    R_position = 12
    
    for i in numbers:
        if i in L:
            position += "L"
            L_position = i
        elif i in R:
            position += "R"
            R_position = i
        else:
            if i == 0:
                i = 11
            else:
                i
                
            a, b = divmod(abs(i-L_position),3)
            c, d = divmod(abs(i-R_position),3)
          
            if a+b > c+d:
                position +="R"
                R_position = i
            elif a+b < c+d:
                position +="L"
                L_position = i
            else:
                if hand == "left":
                    position += "L"
                    L_position = i
                else:
                    position += "R"
                    R_position = i
                
    answer = position
    return answer