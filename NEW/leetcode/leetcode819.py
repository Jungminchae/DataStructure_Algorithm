def mostCommonWord(paragraph, banned):
    import re
    from collections import Counter 
    preprocessed = re.sub("[^\w]", " ", paragraph)
    preprocessed_list = [ word.lower() for word in preprocessed.split() if word.lower() not in banned ]
    
    count_dict = Counter(preprocessed_list)
    most = count_dict.most_common()
    return most[0][0]