def loading(num):
    loading_status = f""
    if num == 100:
        print("100% Comпlete!")
        print("[%%%%%%%%%%]")
    else:
        percent = (num // 10) * '%'
        dots = (10 - (num // 10)) * '.'
        
        print(f"{num}% [{percent}{dots}]")
        print("Still loading...")


num = int(input())
loading(num)