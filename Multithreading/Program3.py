import threading

print("Start code")

def fun():
    print("In fun")

print(threading.current_thread().name)

fun()

