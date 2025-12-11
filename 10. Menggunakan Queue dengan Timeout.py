import queue
import time

q = queue.Queue(maxsize=2)  # Ukuran maksimum

try:
    q.put("Item 1", timeout=1)
    q.put("Item 2", timeout=1)
    q.put("Item 3", timeout=1)  # Ini akan menunggu dan menjadi timeout
except queue.Full:
    print("Queue Full!")

# Fungsi: Menggunakan timeout saat memasukkan item ke dalam antrean.
# Kondisi: Ketika Anda ingin membatasi waktu tunggu saat menambahkan item ke antrean.
