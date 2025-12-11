import queue
import threading
import time

def notifier(q):
    time.sleep(2)  # Simulasi penundaan
    q.put("Notifikasi: Tugas selesai!")

q = queue.Queue()
notification_thread = threading.Thread(target=notifier, args=(q,))
notification_thread.start()

# Tunggu notifikasi
notification = q.get()
print(notification)

# Fungsi: Menggunakan antrean untuk menerima notifikasi dari thread lain.
# Kondisi: Ketika Anda ingin memberitahu bagian dari program bahwa suatu tugas telah selesai.
