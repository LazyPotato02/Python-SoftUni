wanted_chars = input().split(", ")
accepted_words = input()
final_list = [re for re in wanted_chars if re in accepted_words]

print(final_list)