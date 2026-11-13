from logstats import count_levels, top_errors, format_report

with open('events.log', 'r', encoding='utf-8') as file:
    counts = count_levels(file)

with open('events.log', 'r', encoding='utf-8') as file:
    errors = top_errors(file, 3)
report = format_report(counts, errors)
print(report)

