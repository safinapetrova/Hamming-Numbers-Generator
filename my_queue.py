from exceptions import QueueError


class Node:
    """Узел связного списка для очереди."""

    def __init__(self, node_value):
        self.node_value = node_value
        self.next_node = None


class Queue:
    """Реализация очереди на основе связного списка."""

    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.queue_size = 0

    def enqueue(self, element_value):
        """Добавление элемента в конец очереди."""
        new_node = Node(element_value)
        if self.rear_node is None:
            self.front_node = new_node
            self.rear_node = new_node
        else:
            self.rear_node.next_node = new_node
            self.rear_node = new_node
        self.queue_size += 1

    def dequeue(self):
        """Удаление и возврат элемента из начала очереди."""
        if self.front_node is None:
            raise QueueError("Невозможно удалить элемент из пустой очереди")

        removed_value = self.front_node.node_value
        self.front_node = self.front_node.next_node

        if self.front_node is None:
            self.rear_node = None

        self.queue_size -= 1
        return removed_value

    def peek(self):
        """Возврат первого элемента без удаления."""
        if self.front_node is None:
            raise QueueError("Невозможно посмотреть элемент в пустой очереди")
        return self.front_node.node_value

    def is_empty(self):
        return self.queue_size == 0

    def __len__(self):
        return self.queue_size

    def __str__(self):
        elements_list = []
        current_node = self.front_node
        while current_node:
            elements_list.append(str(current_node.node_value))
            current_node = current_node.next_node
        return "Queue: " + ", ".join(elements_list)
