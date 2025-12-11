import queue

class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name

    def __lt__(self, other):
        return self.priority < other.priority

priority_queue = queue.PriorityQueue()
priority_queue.put(Task(2, "Task 2"))
priority_queue.put(Task(1, "Task 1"))

while not priority_queue.empty():
    task = priority_queue.get()
    print("Diambil dari Priority Queue:", task.name)

# Fungsi: Menggunakan PriorityQueue dengan objek kustom berdasarkan aturan prioritas.
# Kondisi: Ketika Anda perlu mengeksekusi objek yang memiliki beberapa atribut sebagai predikat untuk prioritas.
