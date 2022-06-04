#Own submission

# version = input().split(".")
# int_version = list(map(int,version))


# if int_version[2] == 9:
#     int_version[2] = 0
#     int_version[1] = int_version[1] + 1
#     if int_version[1] >= 9:
#         int_version[1] = 0
#         int_version[0] = int_version[0] + 1
# else:
#     int_version[2] = int_version[2] + 1

# print(f"{int_version[0]}.{int_version[1]}.{int_version[2]}")

def next_version(version_number):
    version_number = int("".join(version_number)) + 1
    result = [str(num) for num in str(version_number)]
    print('.'.join(result))

    
data = input().split(".")
next_version(data)