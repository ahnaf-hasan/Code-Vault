def print_star_grid(rows, cols):
    for row in range(rows):
        for col in range(cols):
            print('#', end=' ')
        print()


rows = 9
cols = 13


print_star_grid(rows, cols)