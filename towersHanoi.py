def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         
# Driver code
n = 10
TowerOfHanoi(n, 'A', 'C', 'B')


def hanoi(n, fromTower, toTower, auxTower):
    if n == 1:
        print(f"Move disc {n} from {fromTower} to {toTower}")
        return

    hanoi(n - 1, fromTower, auxTower, toTower)
    print(f"Move disc {n} from {fromTower} to {auxTower}")
    hanoi(n - 1, auxTower, toTower, fromTower)

hanoi(3, 'A', 'B', 'C')