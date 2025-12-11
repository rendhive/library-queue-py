import queue

status_queue = queue.Queue()

# Menyimpan status
for status in ["Started", "In Progress", "Completed"]:
    status_queue.put(status)

while not status_queue.empty():
    print("Status:", status_queue.get())
# Fungsi: Menggunakan antrean untuk menyimpan dan mengambil status aplikasi.
# Kondisi: Ketika Anda ingin menjaga pelacakan status di sepanjang eksekusi aplikasi.
