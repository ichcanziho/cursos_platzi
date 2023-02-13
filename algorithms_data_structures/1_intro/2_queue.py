class MyQueue:

    def __init__(self, queue_size: int = 5):
        self.queue = [0] * queue_size if queue_size != 0 else list()
        self.queue_size = queue_size
        self.rear = -1

    def en_queue(self, value) -> None:
        if self.rear == self.queue_size - 1:
            print("la cola está llena")
        else:
            self.rear += 1
            self.queue[self.rear] = value
            print(f"Se ha añadido el valor: {value} - current queue: {self.queue}, rear {self.rear}")

    def de_queue(self) -> None:
        if self.rear == -1:
            print("la pila está vacia")
        else:
            print(f"Se ha eliminado el valor: {self.queue[0]}", end="")
            del self.queue[0]
            self.queue += [0]
            print(f" - current queue: {self.queue}, rear {self.rear}")
            self.rear -= 1


if __name__ == '__main__':
    # Creando nuestro UDD
    queue = MyQueue(5)
    # Probando el queue
    queue.de_queue()
    queue.en_queue(1)
    queue.en_queue(2)
    queue.de_queue()
    queue.de_queue()
    queue.de_queue()
    queue.en_queue(6)
    queue.en_queue(7)
    queue.en_queue(8)
    queue.en_queue(9)
    queue.de_queue()
    queue.de_queue()
    queue.de_queue()
    queue.en_queue(1)
    queue.en_queue(2)
