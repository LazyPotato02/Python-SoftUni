def even_odd_filter(**kwargs):
    nums_dict = dict()

    # With list comprehensions

    for oper in kwargs:
        if oper == 'even':
            nums_dict[oper] = [x for x in kwargs[oper] if x % 2 == 0]
        else:
            nums_dict[oper] = [x for x in kwargs[oper] if x % 2 != 0]

    return dict(sorted(nums_dict.items(), key=lambda x : -len(x[1])))

