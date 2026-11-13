def parse_event(line: str) ->dict:
    line = line.split(' ')
    if len(line) < 3:
        raise ValueError("части")
    
    time, level, *message = line
    message = ' '.join(message).strip()

    if level not in {"DEBUG", "INFO", "WARNING", "ERROR"}:
        raise ValueError("уровень")
    
    return{
        "time":time,
        "level":level,
        "message":message
        }

def count_levels(lines: list[str]) -> dict:
    counts = {}
    for line in lines:
        if not line.split():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            continue
        level = event["level"]
        counts[level] = counts.get(level, 0)+1
    return counts

def top_errors(lines: list[str], n: int) -> list[list]:
    pass
def format_report(counts: dict, errors: list[list]) -> str:
    pass