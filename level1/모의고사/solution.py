def answer_sheets(answers):
    way_to_guess_1 = [1,2,3,4,5]
    way_to_guess_2 = [2,1,2,3,2,4,2,5]
    way_to_guess_3 = [3,3,1,1,2,2,4,4,5,5]
    
    length_answers = len(answers)
    length_guess_1 = len(way_to_guess_1)
    length_guess_2 = len(way_to_guess_2)
    length_guess_3 = len(way_to_guess_3)
    
    divmod_1 = divmod(length_answers, length_guess_1)
    divmod_2 = divmod(length_answers, length_guess_2)
    divmod_3 = divmod(length_answers, length_guess_3)
    
    answer_sheet_1 = way_to_guess_1*(divmod_1[0])+way_to_guess_1[:divmod_1[1]]
    answer_sheet_2 = way_to_guess_2*(divmod_2[0])+way_to_guess_2[:divmod_2[1]]
    answer_sheet_3 = way_to_guess_3*(divmod_3[0])+way_to_guess_3[:divmod_3[1]]
    
    return [answer_sheet_1, answer_sheet_2, answer_sheet_3]

def right_answer_num(answers,answer_sheet):
    right_answer_num = 0
    for i in range(len(answers)):
        if answers[i] == answer_sheet[i]:
            right_answer_num += 1
    return right_answer_num
            

def solution(answers):
    answer_sheet = answer_sheets(answers)
    right_answer_nums = {}
    right_answer_nums[1] = right_answer_num(answers, answer_sheet[0])
    right_answer_nums[2] = right_answer_num(answers, answer_sheet[1])
    right_answer_nums[3] = right_answer_num(answers, answer_sheet[2])
    keys = [key for key, value in right_answer_nums.items() if value == max(right_answer_nums.values())]
    result = keys
        
    return result