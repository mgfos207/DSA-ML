class Queue:
    def __init__(self, list_obj):
        self.queue = list_obj
        print("Great job instantiating your Queue object one thing to note is that this data structure is FIFO (First in First Out)")

    def add_to_queue(self, val):
        if val is not None:
            if type(val) == list:
                self.queue.extend(val)
            else:
                self.queue.append(val)
        else:
            raise Exception("Please provide a value that is not Null")

    def remove_from_queue(self):
        try:
            return self.queue.pop(0)
        except Exception as e:
            print(f"Getting following issue from queue: {e}")

    def print_queue(self):
        print(self.queue)
    
    def info_queue(self):
        info = """
        Queues are a linear data structure that is FIFO in nature (First in First Out)
        The following operations can be done with their repsective Time Complexity:
        Add item - O(1)
        Remove item - O(1)
        Get Front - O(1)
        Get Rear - O(1)
        """
        print(info)

def main():
    queue_obj = Queue(list())
    queue_obj.add_to_queue([10,3,4,5,7,1])
    queue_obj.add_to_queue(3)

    queue_obj.print_queue()

    item_removed = queue_obj.remove_from_queue()
    print(item_removed)

    print(queue_obj.print_queue())
    queue_obj.info_queue()
    pass
if __name__ == "__main__":
    main()