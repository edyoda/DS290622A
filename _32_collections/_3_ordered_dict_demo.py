# OrderedDict

# it's a child class of dict class
# it remembers the order in which the key was inserted

from typing import OrderedDict


dic = {
    "status":True,
    "total":5000,
    "err":500
}

ordered_dict = OrderedDict()
ordered_dict["a"] = "A"
ordered_dict["c"] = "C"
ordered_dict["d"] = "D"

print(ordered_dict)

print(ordered_dict["d"])
