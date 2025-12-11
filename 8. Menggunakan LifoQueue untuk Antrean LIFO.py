import queue

lifo_queue = queue.LifoQueue()

lifo_queue.put("Item 1")
lifo_queue.put("Item 2")

item = lifo_queue.get()
print("Diambil dari LIFO Queue:", item)
# Fungsi: Menggunakan LifoQueue untuk model antrean LIFO (Last In First Out).
# Kondisi: Ketika Anda ingin mengambil item terakhir yang dimasukkan terlebih dahulu.
