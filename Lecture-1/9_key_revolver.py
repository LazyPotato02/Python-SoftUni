from collections import deque


def reload_gun() -> None:
    global bullets
    global barrel
    for _ in range(barrel_size):
        if bullets: 
            barrel.append(bullets.pop())
    return None

bullet_cost = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
intel_value = int(input())
earnings = 0

barrel = deque()
reload_gun()

while True:
    if bullets and not barrel:
            print('Reloading!')
            reload_gun()

    if not (bullets or barrel) or not locks:
        break
    
    bullet = barrel.popleft()
    earnings -= bullet_cost
    if bullet <= locks[0]:
        print('Bang!')
        locks.popleft()
    else:
        print('Ping!')

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earnings += intel_value
    print(f"{len(bullets) + len(barrel)} bullets left. Earned ${earnings}")
