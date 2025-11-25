'''
def main():
    try:
        x, y, z = map(int, input().strip().split())
    except Exception:
        x = y = z = 0

    coord = (x, y, z)
    print(f"X: {coord[0]}")
    print(f"Y: {coord[1]}")
    print(f"Z: {coord[2]}")

if __name__ == "__main__":
    main()
'''

x,y,z = map(int,input().strip().split())
coord = (x,y,z)

print(f"X: {coord[0]}")
print(f"Y: {coord[1]}")
print(f"Z: {coord[2]}")