def average_score(filename):
    total, count = 0, 0
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                _, score = line.split(',')
                total += int(score)
                count += 1
    return total / count if count > 0 else 0