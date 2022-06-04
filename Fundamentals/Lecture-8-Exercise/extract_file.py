file = input().split("\\")


file_name = file[-1]
final_file = file_name.split(".")

print(f"File name: {final_file[0]}")
print(f"File extension: {final_file[1]}")