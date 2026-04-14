def find_keyword_lines(filename, keyword):
    results = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f, start=1):
            if keyword in line:
                results.append(i)
    return results