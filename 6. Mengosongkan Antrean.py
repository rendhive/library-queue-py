import queue

q = queue.Queue()
q.put("Item 1")
q.put("Item 2")

# Mengosongkan antrean
while not q.empty():
    item = q.get()
    print("Mengambil dari antrean:", item)

# Fungsi: Mengambil semua item dari antrean hingga kosong.
# Kondisi: Ketika Anda ingin memproses semua item dalam antrean.
