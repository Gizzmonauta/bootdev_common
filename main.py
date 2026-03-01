def boolean_search(query_terms, inverted_index):
    docs_for_all = set()

    if len(query_terms) == 1 and query_terms[0] in inverted_index:
        return sorted(inverted_index[query_terms[0]].keys())
    
    if len(query_terms) == 0:
        return []

    for term in query_terms:
        if term not in inverted_index:
            return []

        term_docs_dict = inverted_index[term]
        term_docs_set = set(term_docs_dict.keys())

        if not docs_for_all:
            docs_for_all = term_docs_set
        else:
            docs_for_all = docs_for_all.intersection(term_docs_set)

    result = list(docs_for_all)
    result.sort()
    return result
