def arithmetic_arranger(problems,flag=False):
    arranged_problems=None
    scores=list()
    if len(problems)>5:
        arranged_problems="Error: Too many problems."
    else:
        for problem in problems:
            score=create_score(problem)
            scores.append(score)
    if arranged_problems is None:
        arranged_problems=display_fromat(scores,flag)
    return arranged_problems

class Score:
    number1=None
    operator=None
    number2=None
    error_message=None
    answer=None
    number_digit=None

def create_score(problem):
    score=Score()
    list_problem=problem.split()
    try:
        score.number1=int(list_problem[0])
        score.operator=str(list_problem[1])
        score.number2=int(list_problem[2])
        if list_problem[1]=='+':
            score.answer=score.number1+score.number2
        elif list_problem[1]=='-':
            score.answer=score.number1-score.number2
        else:
            score.error_message="Error: Operator must be '+' or '-'."
            
        if score.number1>=score.number2:
            score.number_digit=len(str(score.number1))
        else:
            score.number_digit=len(str(score.number2))
        if score.number1 >=10000 or score.number2 >=10000:
            score.error_message="Error: Numbers cannot be more than four digits."
    except:
        score.error_message="Error: Numbers must only contain digits."
    
    return score

            
def display_fromat(list_score,flag):
    display=None
    line1=""
    line2=""
    line3=""
    line4=""
    
    for i,score in enumerate(list_score):
        if score.error_message is not None:
            display=score.error_message
            break
        if i<len(list_score)-1:
            line1+="  "+"{val:>{keta}}".format(val=score.number1, keta=score.number_digit)+"    "
            line2+=score.operator+" "+"{val:>{keta}}".format(val=score.number2, keta=score.number_digit)+"    "
            line3+="-"*(score.number_digit+2)+"    "
            line4+="{val:>{keta}}".format(val=score.answer, keta=score.number_digit+2)+"    "
            
        
        else:
            line1+="  "+"{val:>{keta}}".format(val=score.number1, keta=score.number_digit)+"\n"
            line2+=score.operator+" "+"{val:>{keta}}".format(val=score.number2, keta=score.number_digit)+"\n"
            if flag:
                line3+="-"*(score.number_digit+2)+"\n"
                line4+="{val:>{keta}}".format(val=score.answer, keta=score.number_digit+2)
            else:
                line3+="-"*(score.number_digit+2)
            
    if display is None:
        if flag:
            display=line1+line2+line3+line4
        else:
            display=line1+line2+line3
    
    return display