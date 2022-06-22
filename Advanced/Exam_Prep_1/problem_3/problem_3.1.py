def start_spring(**kwargs):
    result = ''
    spring_objects = {}
    for key, value in kwargs.items():
        if value not in spring_objects:
            spring_objects[value] = []
        spring_objects[value].append(key)

    sorted_collections_and_objects = sorted(spring_objects.items(), key=lambda x: (-len(x[1]), x[0]))
    for tuple_ in sorted_collections_and_objects:
        type_object = tuple_[0]
        list_of_objects = tuple_[1]
        sorted_list_of_objects = sorted(list_of_objects)
        result += f"{type_object}:\n"
        for obj in sorted_list_of_objects:
            result += f"-{obj}\n"
    return result.strip()


example_objects = {
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Water Lilly": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))


example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))