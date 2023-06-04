def add_time(start, duration,day_of_week=None):
    start_time=parse_time(start)
    duration_time=parse_time(duration)
    
    time=""
    day_week=""
    days=""
    
    time=format_time(start_time,duration_time)
    if day_of_week is not None:
        day_week=format_day(start_time,duration_time,day_of_week)
    days=format_days(start_time,duration_time)
    
    new_time=time+day_week+days
    return new_time

def parse_time(time):
    now_time=None
    list_time=time.split()
    
    time=list_time[0].split(':')
    min_time=int(time[0])
    second_time=int(time[1])
    
    now_time=min_time*60+second_time
    if len(list_time)>=2:
        if list_time[1]=='PM':
            now_time+=12*60
    return now_time


def format_time(start_time,duration_time):
    time=None
    result_time=start_time+duration_time
    hour=(result_time%(24*60))//60
    minute=(result_time%(24*60))%60
    if hour>=12:
        if hour-12==0:
            hour+=12
        time=str(hour-12)+":"+"{:0>2}".format(minute)+" PM"
    else:
        if hour==0:
            hour+=12
        time=str(hour)+":"+"{:0>2}".format(minute)+" AM"
    return time

       
def format_day(start_time,duration_time,day_of_week):
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    now_count=days.index(day_of_week.capitalize())
    result_time=start_time+duration_time
    add_day=result_time//(24*60)
    result_count=now_count+add_day
    if result_count>=6:
        result_count=result_count%7
        
    return ", "+days[result_count]


def format_days(start_time,duration_time):
    result_time=start_time+duration_time
    add_day=result_time//(24*60)
    
    if add_day==0:
        return ""
    elif add_day==1:
        return " (next day)"
    else:
        return " ("+str(add_day)+" days later)"