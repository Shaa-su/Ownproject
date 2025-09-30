# ======= CODE BLOCK 1: SQUARING NUMBERS =======
nums = [1, 2, 3, 4]                    # Start with a list of numbers

# This loop visits each position in the list
for i in range(len(nums)):             # i will be 0, 1, 2, 3 (positions in list)
    nums[i] = nums[i] ** 2             # Take number at position i, square it (multiply by itself)
    # Step by step:
    # i=0: nums[0] = 1 * 1 = 1
    # i=1: nums[1] = 2 * 2 = 4  
    # i=2: nums[2] = 3 * 3 = 9
    # i=3: nums[3] = 4 * 4 = 16

print(nums)                            # Show final result: [1, 4, 9, 16]


# ======= CODE BLOCK 2: NESTED LOOPS =======
# Think of this like a coordinate system (like battleship game!)

for i in range(3):                     # OUTER loop: i = 0, then 1, then 2 (like rows)
    for j in range(3):                 # INNER loop: j = 0, 1, 2 (like columns)
        print(i, j)                    # Print the coordinates (row, column)
        
# What happens:
# i=0: print (0,0), (0,1), (0,2)  ← Complete row 0
# i=1: print (1,0), (1,1), (1,2)  ← Complete row 1  
# i=2: print (2,0), (2,1), (2,2)  ← Complete row 2

# It's like filling out a grid:
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)  
# (2,0) (2,1) (2,2)