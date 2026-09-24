import threading
import time

done = True


def worker(text):
    counter=0
    while done:
        time.sleep(1)
        counter+=1
        print(text,counter)

t1 = threading.Thread(target=worker,daemon=True,args=("abc",))
t1.start()

input("enter to stop")
done = False