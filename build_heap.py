# python3


def build_heap(data):
    swaps = []
    ##TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n=len(data)
    for i in range(n//2,-1,-1):
        sort(data,i,swaps)
        

    return swaps
def sort(data,i,swaps):
        n=len(data)
        left=2 * i +1
        right=2*i+2
        lar=i
        if left < n and data[left]<data[lar]:
            lar=left
        if right < n and data[right] < data[lar]:
            lar=right
        if i != lar:
            data[i],data[lar]=data[lar],data[i]
            swaps.append((i,lar))
            sort(data,lar,swaps)


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    test=input()
    if 'F' in test:
        test_file = input()
        with open("tests/"+test_file, 'r') as f:
            n=int(f.readline())
            #print(n)
            data = list(map(int, f.readline().split()))
            #print(data)
    else:
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
