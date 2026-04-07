def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    stop_set = set(stopwords)
    print(stop_set)
    new_list = []
    for word in tokens:
        if word not in stop_set:
            new_list.append(word)
        else:
            pass
    return new_list
            
    pass