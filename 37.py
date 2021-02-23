def towerOfHanoi(disk, source, temp, destination):
    if disk == 1:
        print('Move disk 1 from rod {} to rod {}'.format(source, destination))
        return
    towerOfHanoi(disk-1, source, destination, temp)
    print('Move disk {} from rod {} to rod {}'.format(disk, source, destination))
    towerOfHanoi(disk-1, temp, source, destination)


def main():
    print('A: Source\nB: Temporary\nC:Destination')
    towerOfHanoi(int(input("Enter number of disks: ")), 'A', 'B', 'C')


if __name__ == "__main__":
    main()
