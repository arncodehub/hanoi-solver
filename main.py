def move_disk(disk_from, disk_to):
    print(f"Move disk from {disk_from} to {disk_to}!")

def move_via(disk_from, disk_via, disk_to):
    move_disk(disk_from, disk_via)
    move_disk(disk_from, disk_to)
    move_disk(disk_via, disk_to)

def hanoi(disk_count, disk_from, disk_via, disk_to):
    if disk_count == 1:
        move_disk(disk_from, disk_to)
        return
    if disk_count == 2:
        move_via(disk_from, disk_via, disk_to)
        return
    hanoi(disk_count-1, disk_from, disk_to, disk_via)
    move_disk(disk_from, disk_to)
    hanoi(disk_count-1, disk_via, disk_from, disk_to)

def main():
    print("Towers of Hanoi\n")
    print("I can solve a Tower of Hanoi puzzle for you.\n")
    try:
        number_of_disks = input("How many disks are being used? ")
    except:
        print("\n\nIt seems I cannot solve this for you. Sorry!")
        exit()
    print("")
    try:
        number_of_disks = int(number_of_disks)
    except:
        print("It seems I cannot solve this for you. Sorry!")
        exit()
    hanoi(number_of_disks, "A", "B", "C")

if __name__ == "__main__":
    main()
