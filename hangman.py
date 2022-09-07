import string, random
import pytest

def guess_next_letter(pattern, used_letters, word_list):
    """Returns a letter from the alphabet.
    Input parameters:
				pattern: current state of the game board, with underscores "_" in the
            places of spaces (for example, "____e", that is, four underscores
            followed by 'e').
        used_letters: letters you have guessed in previous turns for the same
            word (for example, ['a', 'e', 's']).
        word_list: list of words from which the game word is drawn.
    """
    curr_pos = 0
    frequency = catulate_letter_frequency(word_list)
    word = random.choice(word_list)
    pattern = ''
    for i in word:
        pattern = pattern + "_"
        pass
    j = 1
    while j <= 10:
        if "_" in pattern:
            probe_letter = frequency[curr_pos][0]
            curr_pos = curr_pos + 1
            used_letters.append(probe_letter)
            pattern = "";
            for i in word:
                if i in used_letters:
                    pattern = pattern + i
                else:
                    pattern = pattern + "_"
            print(pattern)
        else:
            break
        j += 1
    if "_" in pattern:
        return None
    else:
        return pattern
    

def catulate_letter_frequency(word_list):
    letter_frequency = dict();
    for i in string.ascii_lowercase:
        letter_frequency[i] = 0
        pass
        
    for word in word_list:
        for letter in word:
            letter_frequency[letter] = letter_frequency[letter] + 1
            pass
        pass
    return sorted(letter_frequency.items(), key = lambda x:x[1], reverse = True)


if __name__ == "__main__":
    
    pattern = "____e"
    word_list = ['about', 'abound']
    used_letters = list("abcde")
    answer = guess_next_letter(pattern, used_letters, word_list)
    print(answer)
    pytest.main(["--html=生成测试报告的路径.html","test.py"])