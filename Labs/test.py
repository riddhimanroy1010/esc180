import time

print(2020 - time.time() // (365 * 24 * 60 * 60))
cur_time = time.time()
for i in range(100):
    print(i)
finish_time = time.time()
print(finish_time - cur_time)