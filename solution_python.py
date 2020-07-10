class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.history = []
        self.ptr = -1

    def add(self, num: int):
        # Adds number to current value

        self.value += num
        pointer = self.ptr

        # Check if within index, if so, insert into history
        if self.is_index(pointer+1):
            self.history.insert(pointer+1,num)
        else :
            self.history.append(num)
        
        # Move pointer
        self.ptr += 1
        pass

    def subtract(self, num: int):

        # The opposite of subtract, same procedure
        self.add(-num)
        pass

    def undo(self):
        pointer = self.ptr

        # If index is still within history, revert action
        if 0 <= pointer :
            self.value -= self.history[pointer]
            self.ptr -= 1
        pass

    def redo(self):
        pointer = self.ptr

        # If index is within future, redo action
        if self.is_index(pointer+1):
            self.value += self.history[pointer+1]
            self.ptr += 1
        pass

    def bulk_undo(self, steps: int):

        # Run undo function "steps" amount of times
        for x in range(steps):
            self.undo()
        pass

    def bulk_redo(self, steps: int):

        # Run redo function "steps" amount of times
        for x in range(steps):
            self.redo()
        pass

    def is_index(self, num:int):
        
        # Check if index is within bounds
        if 0 <= num < len(self.history):
            return True
        return False

