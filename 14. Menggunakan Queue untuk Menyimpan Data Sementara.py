import queue

q = queue.Queue()

# Menyimpan data sementara
data = ["data1", "data2", "data3"]
for item in data:
    q.put(item)

while not q.empty():
    print("Processing data:", q.get())

# Fungsi: Menggunakan antrean untuk menyimpan data sementara.
# Kondisi: Ketika Anda ingin menyimpan data yang akan diproses kemudian dalam antrean.
