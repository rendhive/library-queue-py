import queue

q = queue.Queue()
q.put("Item 1")
q.put("Item 2")

size = q.qsize()
print("Ukuran antrean:", size)
# Fungsi: Memeriksa jumlah item dalam antrean menggunakan qsize().
# Kondisi: Ketika Anda ingin mengetahui berapa banyak item yang ada dalam antrean saat ini.
