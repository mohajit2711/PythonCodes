from collections import deque
#importing library for queue operations
queue = deque(["Mohajit", "Paul" , "Aashay " , "Kulkarni"])
#queue value assignment
queue.append("Yogesh")
print ("Element added is " , queue)
#appending queue
print("Element popped is " , queue.popleft())
#popping left element
print("Element popped is " , queue.pop())
#general pop from right element
print(queue)
#printing final queue
