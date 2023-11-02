from utils import logger


INSTANCE = [5, 2, 4, 6, 1, 3]

def insertion_sort(arr: list[int]) -> list[int]:
    """Sorts a list of integers using insertion sort algorithm."""
    
    logger.info('initial array:     ' + str(arr))
    
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1 
        
        while i > -1 and arr[i] > key:
            arr[i + 1] = arr[i]
            logger.info('on while loop:     ' + str(arr) + '   i: ' + str(i) + '   j: ' + str(j))
            
            i -= 1
        
        arr[i + 1] = key 
        logger.info('out while loop:    ' + str(arr) + '   i: ' + str(i) + '   j: ' + str(j))
        
    logger.info('final array:       ' + str(arr))


def main():
    insertion_sort(INSTANCE)





if __name__ == '__main__':
    main()