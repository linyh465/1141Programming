def parse_product_line(line: str):
    # line: "001 Apple 50" 或 "001 Fancy Apple 50"
    left, qty_str = line.rsplit(maxsplit=1)
    qty = int(qty_str)
    if " " in left:
        pid, name = left.split(maxsplit=1)
    else:
        pid, name = left, ""
    return pid, name, qty

def find_index_by_id(inventory, pid):
    for i, (p, _, _) in enumerate(inventory):
        if p == pid:
            return i
    return -1

def update_stock(inventory, pid, delta):
    idx = find_index_by_id(inventory, pid)
    p, name, qty = inventory[idx]
    inventory[idx] = (p, name, qty + delta)

def format_query(inventory, pid):
    idx = find_index_by_id(inventory, pid)
    p, name, qty = inventory[idx]
    return f"ID: {p}, Name: {name}, Stock: {qty}"

def main():
    n = int(input().strip())
    inventory = []
    for _ in range(n):
        line = input().rstrip()
        pid, name, qty = parse_product_line(line)
        inventory.append((pid, name, qty))

    m = int(input().strip())
    for _ in range(m):
        parts = input().split()
        cmd = parts[0]
        if cmd == "UPDATE":
            pid = parts[1]
            delta = int(parts[2])
            update_stock(inventory, pid, delta)
        elif cmd == "QUERY":
            pid = parts[1]
            print(format_query(inventory, pid))

if __name__ == "__main__":
    main()