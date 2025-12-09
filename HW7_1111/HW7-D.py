'''
def handle_wait(queue, name):
    queue.append(name)

def handle_call(queue):
    if queue:
        name = queue.pop(0)
        return f"Call: {name}"
    return "No one in line"

def process_line(line, queue):
    if not line:
        return None
    parts = line.split(maxsplit=1)
    cmd = parts[0]
    if cmd == "WAIT":
        name = parts[1].strip() if len(parts) > 1 else ""
        handle_wait(queue, name)
        return None
    if cmd == "CALL":
        return handle_call(queue)
    return None

def main():
    queue = []
    try:
        while True:
            try:
                line = input().strip()
            except EOFError:
                break
            if line == "EXIT":
                break
            out = process_line(line, queue)
            if out is not None:
                print(out)
    except Exception:
        pass

if __name__ == "__main__":
    main()
'''

queue = []
outputs = []

while True:
    line = input().strip()

    if line == "EXIT":
        break

    if line.startswith("WAIT "):
        # 提取 'WAIT ' 之後的名字
        name = line[5:].strip()
        if name:
            queue.append(name)

    elif line == "CALL":
        if queue:
            # 取出並移除第一個名字
            called_name = queue.pop(0)
            outputs.append(f"Call: {called_name}")
        else:
            outputs.append("No one in line")

# 統一輸出所有 CALL 的結果
for out in outputs:
    print(out)