import queue

bounded_queue = queue.Queue(maxsize=2)

try:
    bounded_queue.put('Item 1', timeout=1)
    bounded_queue.put('Item 2', timeout=1)
    bounded_queue.put('Item 3', timeout=1)  # Ini akan timeout
except queue.Full:
    print("Antrean sudah penuh!")

# Fungsi: Mengatur ukuran maksimum antrean untuk membatasi jumlah item.
# Kondisi: Ketika Anda perlu memantau berapa banyak item yang dapat disimpan dalam antrean.
