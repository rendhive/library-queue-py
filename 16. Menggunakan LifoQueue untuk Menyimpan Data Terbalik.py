import queue

lifo_queue = queue.LifoQueue()
lifo_queue.put("First")
lifo_queue.put("Second")

while not lifo_queue.empty():
    item = lifo_queue.get()
    print("Diambil dari LIFO Queue:", item)

# Fungsi: Menggunakan LifoQueue untuk mengakses data dengan urutan terbalik.
# Kondisi: Ketika Anda ingin mengambil item terakhir yang dimasukkan ke antrean terlebih dahulu.
