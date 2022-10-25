from typing import Optional, Dict

class MyArray:
    def __init__(self) -> None:
        self.length = 0
        self.data: Dict = {}

    def get(self, index: int) -> Optional[int]:
        if index >= self.length:
            raise IndexError(f"Out of index - {index}")
        return self.data[index]

    def append(self, value: int) -> None:
        self.data[self.length] = value
        self.length += 1
        return 

    def pop(self) -> Optional[int]:
        if self.length == 0:
            raise IndexError("pop from empyt list")
        value = self.data[self.length-1]
        del self.data[self.length - 1]
        self.length -= 1
        return value
    
    def delete(self, index: int) -> int:
        if index >= self.length:
            raise IndexError(f"Out of index - {index}")
        value = self.data[index]
        self.unshift_items(index)
        return value

    def insert(self, index: int, value: int) -> None:
        """
        a = [0, 1, 2]
        a.insert(0, 3)
        a == [3, 0, 1, 2]
        """
        if index >= self.length:
            self.append(value)
            return 

        for i in range(self.length - 1, index, -1):
            current_value = self.data[i]
            self.data[i+1] = current_value

        index_value = self.data[index] 
        self.data[index + 1] = index_value
        self.data[index] = value
        self.length += 1


    
    def unshift_items(self, index: int) -> None:
        for i in range(index, self.length-1):
            self.data[i] = self.data[i + 1]
        
        del self.data[self.length - 1]
        self.length -= 1
        

    def show(self) -> None:
        print(self.data)





def main():
    my_array = MyArray()
    my_array.append(10)
    my_array.append(20)
    my_array.append(30)
    print(my_array.get(0))    
    # print(my_array.pop())
    my_array.delete(2)
    my_array.show()
    my_array.insert(-1, 40)
    my_array.show()





if __name__ == "__main__":
    main()