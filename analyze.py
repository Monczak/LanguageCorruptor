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
