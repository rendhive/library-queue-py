import queue
import threading

def producer(q):
    for item in range(5):
        q.put(item)
        print("Produced:", item)

q = queue.Queue()
thread = threading.Thread(target=producer, args=(q,))
thread.start()
thread.join()

while not q.empty():
    print("Consumed:", q.get())

# Fungsi: Menggunakan thread untuk menambahkan item ke antrean.
# Kondisi: Ketika Anda ingin menjalankan produsen dalam thread terpisah untuk menambahkan data ke antrean.
