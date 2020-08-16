import random


def generate_text(letter_dict, depth, length, seed, saturation=1):
    text = seed
    for i in range(depth, length):
        previous_letters = text[i - depth:i]
        text += pick_random_letter(letter_dict[text[i]][previous_letters], saturation)
    return text


def pick_random_letter(next_letter_dict: dict, saturation):
    return random.choices(list(next_letter_dict.keys()), weights=[i ** saturation for i in list(next_letter_dict.values())], k=1)[0]


def get_preview(text, paragraphs):
    split_text = text.split("\n")
    return "\n".join(split_text[:paragraphs])
