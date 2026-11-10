from collections import deque
from dictionary_data import get_valid_words

def solve_poople(start_word, target_word="poop", word_list=None):
    """Finds the shortest word ladder path from start_word to target_word using BFS."""
    start = start_word.lower()
    target = target_word.lower()
    
    if word_list is None:
        word_list = set()

    if start not in word_list:
        word_list.add(start)
    if target not in word_list:
        word_list.add(target)

    queue = deque([(start, [start])])
    visited = {start}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    while queue:
        current_word, path = queue.popleft()
        
        if current_word == target:
            return path
        
        for i in range(4):
            for char in alphabet:
                if char == current_word[i]:
                    continue
                next_word = current_word[:i] + char + current_word[i+1:]
                if next_word in word_list and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, path + [next_word]))
                    
    return None

# --- Main Execution ---
if __name__ == "__main__":
    start_word = input("Enter today's starting word: ").strip()

    if start_word:
        dictionary = get_valid_words()
        path = solve_poople(start_word, "poop", dictionary)
        
        if path:
            print(f"\nShortest solution ({len(path) - 1} steps):")
            print(" -> ".join(path).upper())
        else:
            print("\nNo valid path found!")

input("\nPress Enter to exit...")
