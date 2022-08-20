# deque

# it is open from both end
# you can add/delete the elements from both the ends

from collections import deque

deque_obj = deque([1,2,3,4,5])

print(deque_obj)

print(deque_obj[2])

deque_obj.append(10)
print(deque_obj)

deque_obj.appendleft(11)
print(deque_obj)

deque_obj.pop()
print(deque_obj)

deque_obj.popleft()
print(deque_obj)

# deque_obj.rotate(2)
# print(deque_obj)

# deque_obj.rotate(-1)
# print(deque_obj)

deque_obj.rotate() # bydefault it considers 1
print(deque_obj)