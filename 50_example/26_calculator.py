import operator

def calc(to_solve):
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                 '**': operator.pow,
                  '%': operator.mod,
                  '//': operator.floordiv}
    op, first_s, second_s = to_solve.split()
    first = int(first_s)
    second = int(second_s)
    
    return operations[op](first, second)

def calc_args(to_solve):
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}
    op, *numbers = to_solve.split()
    if not numbers:
        return 0

    output = int(numbers[0])
    for one_number in numbers[1:]:
        output = operations[op](output, int(one_number))
    return output

def apply_to_each(f, seq):
    return [f(one_item)
            for one_item in seq]

def transform_lines(f, infilename, outfilename):
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for one_line in infile:
            outfile.write(f(one_line))