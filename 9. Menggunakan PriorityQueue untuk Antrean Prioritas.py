import queue

priority_queue = queue.PriorityQueue()

# Menambahkan item dengan prioritas
priority_queue.put((2, "Item 2"))
priority_queue.put((1, "Item 1"))
priority_queue.put((3, "Item 3"))

while not priority_queue.empty():
    item = priority_queue.get()
    print("Diambil dari Priority Queue:", item[1])

# Fungsi: Menggunakan PriorityQueue untuk menambahkan item dengan prioritas.
# Kondisi: Ketika Anda ingin item dikeluarkan dari antrean berdasarkan prioritas bukan urutan masukan.
