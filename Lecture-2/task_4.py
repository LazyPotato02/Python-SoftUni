input_chars = [x for x in input()]
unique_chars = set(input_chars)
s = sorted(unique_chars)
output = ('{0}: {1} time/s'.format(x, input_chars.count(x)) for x in s)
print (*output, sep='\n')