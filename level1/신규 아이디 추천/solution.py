import string

def solution(new_id):
    lower_id = new_id.lower() #1단계
    #2단계
    word = string.ascii_lowercase+string.digits+"-"+"_"+"."
    remove_id = ""
    for i in lower_id:
        if i in word:
            remove_id += i
    #3단계
    while ".." in remove_id:
        remove_id = remove_id.replace("..",".")
    #4단계
    if remove_id[0] == "." and len(remove_id)>0:
        remove_id = remove_id[1:]
    if len(remove_id)>0 and remove_id[-1] == ".":
        remove_id = remove_id[:-1]
    #5단계
    if remove_id == "":
        remove_id += "a"
    #6단계
    if len(remove_id) >= 16:
        remove_id = remove_id[:15]
        if remove_id[-1] == ".":
            remove_id = remove_id[:-1]
    #7단계
    if len(remove_id)<=2:
        while len(remove_id) <3:
            remove_id += remove_id[-1]
    answer = remove_id
    return answer
