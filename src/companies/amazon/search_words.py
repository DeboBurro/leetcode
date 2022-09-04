def min_match_words(searchWord, resultWord):
    if len(resultWord) == 0:
        return 0
    if len(searchWord) == 0:
        return len(resultWord)
    p_search = 0
    p_result = 0
    while p_search < len(searchWord) and p_result < len(resultWord):
        if p_result == len(resultWord):
            return 0
        if searchWord[p_search] == resultWord[p_result]:
            p_search += 1
            p_result += 1
            continue
        else:
            p_search += 1
    return  len(resultWord) - p_result

searchWord = 'armaze'
resultWord = 'amazon'
print(min_match_words(searchWord, resultWord))