def parse_event(line: str) ->dict:
    line = line.split(' ')
    if len(line) >= 3:
        time, level, *message = line
        message = ' '.join(message).strip()
        return{
            "time":time,
            "level":level,
            "message":message
        }
    else:
        return{}
def count_levels(lines: list[str]) -> dict:
    pass
def top_errors(lines: list[str], n: int) -> list[list]:
    pass
def format_report(counts: dict, errors: list[list]) -> str:
    pass