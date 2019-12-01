def shiftTable(text, pattern):
    table = dict.fromkeys(text, len(pattern))
    for i in range(len(pattern) - 1):
        table[pattern[i]] = len(pattern) - i - 1
    return table


def horspool(text, pattern):
    table = shiftTable(text, pattern)
    print(f'Shift table: {table}')
    skip = 0
    comparisons = 0
    found = []

    while skip + len(pattern) <= len(text):
        i = len(pattern) - 1

        while i >= 0 and text[skip+i] == pattern[i]:
            comparisons += 1
            i -= 1
            if i < 0:
                found.append(str(skip + 1))
                if skip + len(pattern) <= len(text):
                    skip += table[text[skip + len(pattern) - 1]]

        if skip+len(pattern) <= len(text) and text[skip+i] != pattern[i]:
            comparisons += 1
            skip += table[text[skip + len(pattern) - 1]]

    print(f'Total comparisons: {comparisons}')
    return found


if __name__ == "__main__":

    text = 'TTATAGATCTCGTATTCTTTTATAGATCTCCTATTCTT'
    pattern = 'TCCTATTCTT'

    print(f'\nSearching for "{pattern}" in "{text}".')

    match = horspool(text, pattern)
    if(len(match) > 0):
        print(f"Match found at position {', '.join(match)}")
    else:
        print('No Matches found')