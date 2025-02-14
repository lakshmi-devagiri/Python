# (Que example. Class deque is used to convert List as a Que) FIFO
from collections import deque
que = deque(['ram', 'ravi', 'venkat'])
print (que)
print ("appending")
que.append('venu')
print (que)
print ("popped = " , que.popleft())
print (que)
print ("popped = ", que.popleft())
print (que)