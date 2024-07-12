def find_pattern(word, pattern):
    match = []
    for i in range(len(word)):
        if word[i:i+len(pattern)] == pattern:       # Check if the current substring is the pattern.
            match.append((i, i+len(pattern)-1))     # exclusive end index
    return match

word = input("Enter a word: ")
pattern = input("Enter word to identify: ")
match = find_pattern(word, pattern)

if match:
    print(f"Pattern '{pattern}' found at index:")
    for start, end in match:
        print(f"  {start} and {end}")
else:
    print(f"Pattern '{pattern}' not found")