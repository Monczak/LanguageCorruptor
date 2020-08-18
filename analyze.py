def analyze_text(text, depth):
    result = {}

    for i in range(depth, len(text) - 1):
        previous_letters = text[i - depth:i]
        if text[i] in result:
            if previous_letters in result[text[i]]:
                if text[i + 1] in result[text[i]][previous_letters]:
                    result[text[i]][previous_letters][text[i + 1]] += 1
                else:
                    result[text[i]][previous_letters][text[i + 1]] = 1
            else:
                result[text[i]][previous_letters] = {}
                result[text[i]][previous_letters][text[i + 1]] = 1
        else:
            result[text[i]] = {}
            result[text[i]][previous_letters] = {}
            result[text[i]][previous_letters][text[i + 1]] = 1

    return result


def scale_dict(letter_dict, factor):
    for current_letter in letter_dict:
        for previous_letters in letter_dict[current_letter]:
            for next_letter in letter_dict[current_letter][previous_letters]:
                letter_dict[current_letter][previous_letters][next_letter] *= factor


def merge_dicts(main_dict, new_dict):
    for current_letter in new_dict:
        if current_letter in main_dict:
            for previous_letters in new_dict[current_letter]:
                if previous_letters in main_dict[current_letter]:
                    for next_letter in new_dict[current_letter][previous_letters]:
                        if next_letter in main_dict[current_letter][previous_letters]:
                            main_dict[current_letter][previous_letters][next_letter] += \
                                new_dict[current_letter][previous_letters][next_letter]
                        else:
                            main_dict[current_letter][previous_letters][next_letter] = \
                                new_dict[current_letter][previous_letters][next_letter]
                else:
                    main_dict[current_letter][previous_letters] = new_dict[current_letter][previous_letters]
        else:
            main_dict[current_letter] = new_dict[current_letter]