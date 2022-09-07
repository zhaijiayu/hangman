import hangman

def test_function_should_return_something():
	pattern = "____e"
	used_letters = list("abcde")
	word_list = ['about', 'abound']
	assert hangman.guess_next_letter(pattern, used_letters, word_list) is not None