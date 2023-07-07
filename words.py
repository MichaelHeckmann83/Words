import os
import time

start = time.process_time()

path = os.path.join(os.path.expanduser("~"), "Desktop", "words.txt")
if os.path.exists(path):
    with open(path) as file:
        lines = file.read()
    alpha = {chr(c): lines.lower().count(chr(c)) for c in range(10, 123)}
    alpha = {c: n for c, n in alpha.items() if n != 0}
    alpha = dict(sorted(alpha.items(), key=lambda i: i[1], reverse=True))
    word_count = alpha.get("\n")
    print(word_count)
    char_count = len(lines) - word_count
    print(char_count)
    alpha.pop("\n")
    print(alpha)
    beta = {c: n / word_count for c, n in alpha.items()}
    print(beta)
    gamma = {c: n / char_count for c, n in alpha.items()}
    print(gamma)
else:
    print("no file")

print(time.process_time() - start)
