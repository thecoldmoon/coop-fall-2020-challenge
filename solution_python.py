class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.history = []
        self.ptr = -1

    def add(self, num: int):
        self.value += num
        pointer = self.ptr

        if self.is_index(pointer+1):
            self.history.insert(pointer+1,num)
        else :
            self.history.append(num)
        
        self.ptr += 1
        pass

    def subtract(self, num: int):
        self.add(-num)
        pass

    def undo(self):
        pointer = self.ptr
        if 0 <= pointer :
            self.value -= self.history[pointer]
            self.ptr -= 1
        pass

    def redo(self):
        pointer = self.ptr
        if self.is_index(pointer+1):
            self.value += self.history[pointer+1]
            self.ptr += 1
        pass

    def bulk_undo(self, steps: int):
        for x in range(steps):
            self.undo()
        pass

    def bulk_redo(self, steps: int):
        for x in range(steps):
            self.redo()
        pass

    def is_index(self, num:int):
        if 0 <= num < len(self.history):
            return True
        return False

