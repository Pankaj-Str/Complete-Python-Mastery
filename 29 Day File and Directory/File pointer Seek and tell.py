# File Pointer Tutorial: Understanding seek() and tell()
# =================================================

# Let's create a sample file to work with
with open('sample.txt', 'w') as file:
    file.write("Hello World!\nThis is line 2\nThis is line 3")

# Part 1: Basic File Reading
# -------------------------
print("Part 1: Basic File Reading")

with open('sample.txt', 'r') as file:
    # Read the first line
    first_line = file.readline()
    print(f"First line: {first_line}")
    
    # Get current position
    position = file.tell()
    print(f"Current position after reading first line: {position}")
    
    # Read the next line
    second_line = file.readline()
    print(f"Second line: {second_line}")

# Part 2: Using seek() to Navigate
# ------------------------------
print("\nPart 2: Using seek()")

with open('sample.txt', 'r') as file:
    # Move to specific position from start (offset = 6)
    file.seek(6)
    print(f"Reading from position 6: {file.read(5)}")  # Should read "World"
    
    # Move to beginning of file
    file.seek(0)
    print(f"Back to start: {file.read(5)}")  # Should read "Hello"
    
    # Get file size
    file.seek(0, 2)  # Seek to end
    file_size = file.tell()
    print(f"File size: {file_size} bytes")

# Part 3: Different seek() Modes
# ----------------------------
print("\nPart 3: seek() Modes")

with open('sample.txt', 'r') as file:
    # seek(offset, whence)
    # whence = 0 (start), 1 (current), 2 (end)
    
    # Read from start (whence = 0)
    file.seek(6, 0)
    print(f"6 chars from start: {file.read(5)}")
    
    # Move relative to current position (whence = 1)
    file.seek(0)  # First go back to start
    file.read(6)  # Read "Hello "
    file.seek(6, 1)  # Move 6 more chars from current position
    print(f"After relative seek: {file.read(5)}")
    
    # Move relative to end (whence = 2)
    file.seek(-10, 2)  # 10 chars before end
    print(f"Last 10 chars: {file.read()}")

# Part 4: Practical Example - Simple Text Parser
# -------------------------------------------
print("\nPart 4: Practical Example")

def find_line_position(file_path, line_number):
    positions = []
    with open(file_path, 'r') as file:
        pos = 0
        positions.append(pos)
        
        for line in file:
            pos += len(line)
            positions.append(pos)
            
    if 0 <= line_number < len(positions):
        return positions[line_number]
    return -1

# Use the parser
line_pos = find_line_position('sample.txt', 1)
with open('sample.txt', 'r') as file:
    file.seek(line_pos)
    print(f"Directly reading line 2: {file.readline()}")

# Clean up
import os
os.remove('sample.txt')
