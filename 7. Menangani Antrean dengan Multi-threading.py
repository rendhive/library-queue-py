import queue
import threading
import time

def worker(q):
    while not q.empty():
        item = q.get()
        print("Processing:", item)
        time.sleep(1)  # Simulasi pemrosesan
        q.task_done()  # Tandai bahwa item sudah diproses

q = queue.Queue()
for i in range(5):
    q.put(f"Item {i+1}")

threads = []
for _ in range(2):  # Membuat 2 thread pekerja
    thread = threading.Thread(target=worker, args=(q,))
    threads.append(thread)
    thread.start()

q.join()  # Menunggu hingga semua item selesai diproses
print("Semua item telah diproses.")
# Fungsi: Menggunakan antrean dengan thread untuk pemrosesan paralel.
# Kondisi: Ketika Anda ingin menjalankan proses secara bersamaan dan berbagi data menggunakan antrean.
