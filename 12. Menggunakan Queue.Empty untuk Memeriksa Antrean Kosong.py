import queue

q = queue.Queue()

try:
    item = q.get_nowait()  # Mengambil item tanpa menunggu
except queue.Empty:
    print("Antrean kosong!")

# Fungsi: Menangani situasi di mana antrean kosong saat mengambil item.
# Kondisi: Ketika Anda ingin mengambil item tanpa memblokir eksekusi.
