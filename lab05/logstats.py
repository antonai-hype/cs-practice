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
    err_counts={}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
    
        if event["level"] == "ERROR":
            ms = event["message"]
            err_counts[ms] = err_counts.get(ms,0)+1

    items = list(err_counts.items())
    items.sort(key=lambda x: x[0])
    items.sort(key=lambda x: x[1], reverse=True)
    result = items[:n]
    return result

def format_report(counts: dict, errors: list[list]) -> str:
    report = "Отчёт по журналу\n\n"
    for level in sorted(counts):
        report += f"{level}: {counts[level]}\n"
    report += "\nЧастые ошибки:\n"
    for msg, count in errors:
        report += f"- {msg} — {count}\n"
    return report
        