import queue
import threading
import time

def consumer(q):
    while True:
        item = q.get()
        if item is None:  # Jika item adalah None, hentikan loop
            break
        print("Consumed:", item)
        time.sleep(1)
        q.task_done()

q = queue.Queue()
thread = threading.Thread(target=consumer, args=(q,))
thread.start()

for item in range(5):
    q.put(item)

q.join()  # Tunggu sampai semua item diproses
q.put(None)  # Hentikan consumer
thread.join()

# Fungsi: Menggunakan antrean untuk mengelola data antar thread.
# Kondisi: Ketika Anda memiliki produsen dan konsumen yang berbagi data.
