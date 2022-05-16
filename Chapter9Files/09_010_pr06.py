# which line python is present we need to check
content = True
i = 1
with open("log.txt") as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"yes python is present in line number {i}")
            i = i+1
