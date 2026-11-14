seconds= int(input())
hours = seconds // 3600
minutes = (seconds % 3600) // 60
sec = seconds % 60
print(hours)
print(minutes)
print(sec)