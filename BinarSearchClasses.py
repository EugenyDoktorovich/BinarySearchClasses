from array import array


arr = [1,2,3,4,5,6,19,28,34]



class BinarSearch:
    def __init__(self, array, element):
        self.array = array
        self.element = element
        print('Данные приняты, вызовите метод для операции над ними.')

    def __repr__(self):
        return f'Element: {self.element}   Array: {self.array}'


    def __getattr__(self, item):
        print(f'__getattr__({item})')
        return -1

    def __getattribute__(self, item):
        print(f'__getattribute__({item})')
        if item == 'y':  # запретим получать y
            raise AttributeError
        return super().__getattribute__(item)
        
    
    def binary_search_iterative(self):
        mid = 0
        start = 0
        end = len(self.array)
        step = 0

        while (start <= end):
            print("Subarray in step {}: {}".format(step, str(self.array[start:end+1])))
            step = step+1
            mid = (start + end) // 2

            if self.element == self.array[mid]:
                return mid

            if self.element < self.array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

if __name__ == '__main__':
    answer = BinarSearch(arr,19)
    print(answer.binary_search_iterative())
    print(answer)