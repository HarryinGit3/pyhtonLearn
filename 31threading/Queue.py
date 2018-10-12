import threading
from queue import Queue


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2;
    q.put(l)


def multithreading():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
    for i in range(4):
        t = threading.Thread(target=job, args=[data[i], q])
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)


if __name__ == '__main__':
    multithreading()
    a = [B101	varchar(40)	，
B102	varchar(32)	,
B103	varchar(128)	,
B104	varchar(14)	,
B105	varchar(14)	,
B106	varchar(14)	,
B201	char(2)	,
B202	json	,
B203	varchar(2000)	,
B204	varchar(256)	,
B205	point	,
B206	json	,
B207	varchar(2000)	,
B208	json	,
B209	varchar(2000)	,
B210	json	,
B211	varchar(2000)	,
B212	json	,
B213	varchar(2000)	,
B214	json	,
B215	json	,
         ]
