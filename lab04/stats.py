def parse_record(line: str)->dict:
    parts=line.split(";")
    if len(parts) !=3:
        raise ValueError("менее трех полей")

    city = parts[0].strip()
    temp_raw = parts[1].strip().replace(",", ".")
    date = parts[2].strip()

    if city == "" or date == "":
        raise ValueError("пустая дата или город")

    try:
        temperature = float(temp_raw)
    except ValueError:
        raise ValueError("температура не число")

    return {"city": city, "temperature": temperature, "date": date}

    
def read_valid(lines: list[str])->list[dict]:
    records = []

    for line in lines:

       if not line.strip():
             continue

       try:
           record = parse_record(line)
       except ValueError:
            continue 
       records.append(record)
    return records

def average_by_city(records: list[dict])-> dict:
    sums = {} 
    counts = {}
    for record in records:            
        city = record["city"]         
        temperature = record["temperature"]
        sums[city] = sums.get(city, 0) + temperature
        counts[city] = counts.get(city, 0) + 1

    result = {}

    for city in sums:
        avg = sums[city] / counts[city]
        result[city] = round(avg, 1)

    return result  

def warmest_city(records: list[dict])->str:
    averages = average_by_city(records)

    if not averages:                      
        return ""                         

    best = ""                            
    best_avg = -1000                      
    for city in averages:                 
        avg = averages[city]
        if avg > best_avg:                
            best = city
            best_avg = avg
        elif avg == best_avg and city < best:   
            best = city
    return best
