nULL = "NULL"
def get_similarity_value(base_word : str,target_word : str,minimumRequierment):
    result = 0
    target_word_turn = 0
    distance = 0
    similarity = 0
    for char in base_word:
        if char != target_word[target_word_turn]:
            distance += 1
            if similarity >= minimumRequierment:
                result += similarity
                similarity = 0
                target_word_turn = 0
        else:
            similarity += 1        
            target_word_turn += 1
        if similarity == len(target_word):
            result += similarity
            return result - distance
    if similarity >= minimumRequierment:
        result += similarity
    if (result == 0):
        return nULL
    return result - distance
def top_result(all_words : list,all_vals : list):
    bestResult = all_words[0]
    bestResultVal = all_vals[0]
    bestTurn = 0
    turn = 0
    for val in all_vals:
        if (val > bestResultVal):
            bestResult = all_words[turn]
            bestResultVal = val
            bestTurn = turn
        turn += 1
    return [bestResult,bestTurn]
def Reverse(Input : list):
    result = []
    for turn in range(1,len(Input) + 1,):
        result.append(Input[-turn])
    return result
def search(target_word : str,all_words : list):
    result = []
    vals = []
    nulls = []
    for word in all_words:
        vals.append(get_similarity_value(word,target_word,3))
    turn = 0
    for val in vals:
        if (val == nULL):
            nulls.append(all_words.pop(turn + 1))
            vals.pop(turn + 1)
    while len(all_words) > 0:
        best = top_result(all_words,vals)
        result.append(best[0])
        all_words.remove(best[0])
        vals.pop(best[1])
    result += nulls
    return Reverse(result)

#for tests
#a = search("amirali",[":|","big amir","amirali the hard",":|"])
#for b in a:
#    print(b)