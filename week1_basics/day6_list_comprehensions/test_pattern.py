# Print Right-angled triangle using pattern loops
#
# Right-angled triangle using pattern loops
#
def print_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

print("Right-angled triangle using pattern loops")
print_triangle(5)

# Pyramid pattern using pattern loops
def print_pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end=" ")
        for k in range(2 * i + 1):
            print("*", end=" ")
        print()
print("Pyramid pattern using pattern loops")
print_pyramid(5)