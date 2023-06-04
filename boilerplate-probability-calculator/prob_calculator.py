import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents=[]
        for k,v in kwargs.items():
            for i in range(0,v,1):
                self.contents.append(k)
    def draw(self,ball_count):
        draw_list=[]
        copy_contents=copy.copy(self.contents)
        if ball_count>=len(copy_contents):
            return copy_contents
        for i in range(0,ball_count,1):
            num=random.randint(0,len(copy_contents)-1)
            draw=copy_contents.pop(num)
            draw_list.append(draw)
        self.contents=[]
        for value in copy_contents:
          self.contents.append(value)      
        return draw_list
        


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability=0
    ok_cout=0
    
    for i in range(0,num_experiments,1):
        copy_hat=copy.copy(hat)
       
        check_list=copy_hat.draw(num_balls_drawn)
        add_flag=compare_list_dict(expected_balls,check_list)
        if add_flag:
            ok_cout+=1
        else:
            ok_cout+=0
        
    probability=ok_cout/num_experiments
    return probability

def compare_list_dict(expected_balls,check_list):
    ok_flag=True
    for k,v in expected_balls.items():
        if v>check_list.count(k):
            ok_flag=False
            break
        else:
            ok_flag=True
    return ok_flag
