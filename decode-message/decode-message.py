# Return the decoded message: Return a whitespace separated string based on a hidden message found within a given file
# Number of lines is expected to be odd!

# Input file example:
# 3 love
# 6 computers
# 2 dogs
# 4 cats
# 1 I
# 5 you

# To find the hidden message, arrange the lines in a pyramid structure:
#   1
#  2 3
# 4 5 6

# Output expected: "I love computers"


def decode_message(message_file: str) -> str:
    pair = []
    pyramid = []
    current_line = []
    decoded_arr = []
    pyramid_len = 1
    decoded = ""

    with open(message_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        number, word = line.split()

        # Python won't sort the number properly as a str, so we cast it to int
        pair.append((int(number), word))

    sorted_pair = sorted(pair)

    for number, word in sorted_pair:
        current_line.append((number, word))
        if len(current_line) == pyramid_len:
            pyramid.append(current_line)
            pyramid_len += 1
            current_line = []

    for line in pyramid:
        decoded_arr.append(line[-1][-1])

    decoded = " ".join(decoded_arr)
    return decoded


if __name__ == "__main__":
    print(decode_message("coded-message.txt"))
    print(decode_message("complex-coded-message.txt"))
