import re
from functools import partial


def count_and_replace(filename):
    terrible_count = 0
    # Keeps track of whether "terrible" occurs an even or odd number of times
    even_count = False

    def repl(m, even_count):
        # Use a nonlocal statement to modify the outer variable
        nonlocal terrible_count
        terrible_count += 1
        return 'pathetic' if (even_count := not even_count) else 'marvellous'

    with open(filename, 'r') as file, open('result.txt', 'w') as result_file:
        for line in file:
            # Use partial to pass the even_count argument to the repl function
            new_line = re.sub(r'\bterrible\b', partial(repl, even_count=even_count), line, flags=re.I)
            result_file.write(new_line)

    return terrible_count


if __name__ == "__main__":
    filename = 'file_to_read.txt'
    terrible_count = count_and_replace(filename)
    print(f"The word 'terrible' appears {terrible_count} times in the file.")
