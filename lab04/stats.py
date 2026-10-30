def pars_record(line: str)->dict:
    parts=split.line(";")
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
    pass
def average_by_city(records: list[dict])-> dict:
    pass
def warmest_city(records: list[dict])->str:
    pass