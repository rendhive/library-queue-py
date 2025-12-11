import queue
import threading
import time

def process_data(q):
    while True:
        item = q.get()
        if item is None:
            break  # Hentikan loop
        print("Memproses:", item)
        time.sleep(1)
        q.task_done()

q = queue.Queue()
threads = []
for _ in range(3):
    thread = threading.Thread(target=process_data, args=(q,))
    threads.append(thread)
    thread.start()

# Menambahkan data ke antrean
for item in range(10):
    q.put(item)

# Menunggu semua item diproses
q.join()

# Menghentikan threads
for _ in range(3):
    q.put(None)
for thread in threads:
    thread.join()

# Fungsi: Menyinkronkan akses ke resource dengan menggunakan antrean.
# Kondisi: Ketika Anda ingin memastikan bahwa resource diakses dengan aman oleh beberapa thread.
