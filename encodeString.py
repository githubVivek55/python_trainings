
def encode_string(input_string):
    result = []
    for word in input_string.split(" "):
        if len(word) < 3:
            # reverse word
            result.append(word[::-1])
        else:
            start = "234"
            end = "567"
            encoded_word = start + word[1:] + word[0] + end
            result.append(" "+encoded_word)
    return "".join(result).strip()

def decode_string(encoded_string):
    result = []
    for word in encoded_string.split(" "):
        if len(word) < 3:
            # reverse word
            result.append(word[::-1])
        else:
            decoded_word = word[3:-3]
            decoded_word = decoded_word[-1] + decoded_word[:-1]
            result.append(decoded_word)
    return " ".join(result)


if __name__ == "__main__":
    input_string = "Hello, World!"
    encoded_string = encode_string(input_string)
    print(f"Encoded string: {encoded_string}")
    decode_string = decode_string(encoded_string)
    print(f"Decoded string: {decode_string}")
