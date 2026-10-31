def parse_event(line):
    line=line.split(' ')
    if len(line) >= 3:
        time, level, *message = line
        message = ' '.join(message).strip() 
        return {
            'time':time,
             'level':level,
             'message':message
             }
    else:
        return{}


    