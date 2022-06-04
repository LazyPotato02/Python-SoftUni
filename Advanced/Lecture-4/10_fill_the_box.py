def fill_the_box(h, l, w, *args):
    volume = h * l * w
    cubes = args[:args.index('Finish')]
    num_cubes = sum(cubes)
    diff = abs(volume - num_cubes)
    if volume > num_cubes:
        return f"There is free space in the box. You could put {diff} more cubes."
    else:
        return f'No more free space! You have {diff} more cubes.'