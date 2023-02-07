from collections import Counter, defaultdict
import math

def prob(key, tokens):
	return float(tokens[key])/len(tokens)

def perplexity(tokens : defaultdict):
	returnable = (1.0/len(tokens))
	total = 0
	for key in list(tokens.keys()):
		total += math.log(prob(key, tokens)) * tokens['STOP']
	return 2 ** -(returnable * total)


# n of 1 = unigram, 2 = bigram.. n = ngram
def tokenize_data(file_name : str, n : int):
	# define the default dictionary
	returnable_dictionary = defaultdict(lambda:0)
	data = open(file_name, 'r').readlines()
	returnable_dictionary['<UNK>'] = 0
	total_word_count = 0
	for line in data:
		# split the line by spaces
		terms = []
		
		key = [str] * n
		for i, word in enumerate(line.split()):
			if n > 1:
				# determine whether we have a 'gram'
				# or if we are still figuring out what the 'gram' is
				key[i % n] = word
				if i > 0 and i % n == 0:
					# we need to combine the key and increase the value
					combined_key = ''
					for part in key:
						combined_key = combined_key + part
					returnable_dictionary[combined_key] += 1
					total_word_count += 1
			else:
				returnable_dictionary[word] += 1
				total_word_count += 1
		returnable_dictionary['<STOP>'] += 1
		
	for key in list(returnable_dictionary.keys()):
		if returnable_dictionary[key] < 3:	
			del returnable_dictionary[key]
			returnable_dictionary['<UNK>'] += 1
	
	# check section
	print("We counted", returnable_dictionary['<STOP>'], "<STOP>'s. There should be", len(data))

	return returnable_dictionary, total_word_count


def main():
	tokens, total_word_count = tokenize_data('1b_benchmark.' + input() + '.tokens', 1)
	print("Perplexity: ", perplexity(tokens)) 
	pass


main()

