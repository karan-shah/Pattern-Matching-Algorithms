def brute_force(txt, pat):
    stringLength = len(txt)
    patternLength = len(pat)

    if patternLength > stringLength:
        print("No Match Found")
    else:
        comparisons = 0
        found = []
        for i in range(0, (stringLength - patternLength) + 1):
            j = 0
            while j < patternLength and txt[i + j] == pat[j]:
                j = j + 1
                comparisons += 1
                if j == patternLength:
                    found.append(str(i+1))

            if(j < patternLength and txt[i + j] != pat[j]):
                comparisons += 1

        if(len(found) > 0):
            print("Matching Found At: " + ', '.join(found))
        else:
            print('No Matches found')
        print('Total Comparisions:', comparisons)


text = 'TTATAGATCTCGTATTCTTTTATAGATCTCCTATTCTT'
pattern = 'TCCTATTCTT'

print(f'\nSearching for "{pattern}" in "{text}".')

brute_force(text, pattern)