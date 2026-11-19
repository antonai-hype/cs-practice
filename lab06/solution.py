def count_by_extension(paths: list[str]) -> dict[str, int]:
    extensions = {}

    for path in paths:

        if '.' in path:
            extention = path.split('.')[-1].lower()

        else:
            extention = ""
        extensions[extention] = extensions.get(extention, 0) + 1
    return extensions

def deepest_path(paths: list[str]) -> str:
    deepest = ""

    for path in paths:
        if path.count('/') > deepest.count("/") or (path.count("/") == deepest.count("/") and path < deepest):
            deepest = path

    return deepest


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    i = 0

    while n_bytes >= 1024 and i < 4:
        n_bytes = n_bytes / 1024
        i += 1

    if i == 0:
        return f"{n_bytes} {units[i]}"
    
    return f"{n_bytes:.1f} {units[i]}"
    

paths = ["docs/report.PDF",
            "notes.txt",
            "docs/img/logo.png", 
            "Makefile"
        ]
print(count_by_extension(paths))
print(deepest_path(paths))
print(human_size(900))           # "900 Б"
print(human_size(1536))            # "1.5 КБ"
print(human_size(5 * 1024 * 1024)) # "5.0 МБ"

# count_by_extension(paths)   # {"pdf": 1, "txt": 1, "png": 1, "": 1}
# deepest_path(paths)         # "docs/img/logo.png"