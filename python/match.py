def levenshtein(training_file, haystack):
    if len(training_file) < len(haystack):
        return levenshtein(haystack, training_file)
 
    # len(training_file) >= len(haystack)
    if len(haystack) == 0:
        return len(training_file)
 
    previous_row = range(len(haystack) + 1)
    for i, c1 in enumerate(training_file):
        current_row = [i + 1]
        for j, c2 in enumerate(haystack):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than haystack
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]

def levenshteinPercentage(training_file, haystack):
    return (levenshtein(training_file, haystack) / max(len(training_file),len(haystack))) * 100