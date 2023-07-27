import threading
import pytest
import time


class MyThread(threading.Thread):
    def __init__(self,testThing:str,fileName:str) -> None:
        super().__init__()
        self.testThing=testThing
        self.fileName=fileName
    def run(self):
        print(f"線程{self.testThing}正在執行...")
        pytest.main([self.fileName,"--html=report.html"])
        print(f"線程{self.testThing}執行完成.")





# class MyThread(threading.Thread):
#     def __init__(self, thread_id, name) -> None:
#         super().__init__()
#         self.thread_id = thread_id
#         self.name = name

#     def run(self):
#         print(f"線程{self.name}正在執行...")
#         time.sleep(5)
#         print(f"線程{self.name}執行完成.")


# thread1 = MyThread(1, "Thread-1")
# thread2 = MyThread(2, "Thread-2")
# thread3 = MyThread(3, "Thread-3")

# thread1.start()
# thread2.start()
# thread3.start()

# thread1.join()
# thread2.join()
# thread3.join()
