def count_by_extension(paths):
    extensions = {}

    for path in paths:

        if '.' in path:
            extention = path.split('.')[-1].lower()

        else:
            extention = ""
        extensions[extention] = extensions.get(extention, 0) + 1
    return extensions

def deepest_path(paths):
    pass


def human_size(n_bytes):
    pass
paths = ["docs/report.PDF",
            "notes.txt",
            "docs/img/logo.png", 
            "Makefile"
        ]
print(count_by_extension(paths))

# count_by_extension(paths)   # {"pdf": 1, "txt": 1, "png": 1, "": 1}
# deepest_path(paths)         # "docs/img/logo.png"

# human_size(900)             # "900 Б"
# human_size(1536)            # "1.5 КБ"
# human_size(5 * 1024 * 1024) # "5.0 МБ"