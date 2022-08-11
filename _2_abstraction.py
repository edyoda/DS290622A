from abc import ABC,abstractmethod

class College(ABC):
    @abstractmethod
    def exam_ticket(self):
        pass

    def timing(self):
        return "10am - 1pm"

class ClassRoomA(College):
    def exam_ticket(self):
        return "IT Exam Ticket"

class ClassRoomB(College):
    def exam_ticket(self):
        return "CS Exam Ticket"

class ClassRoomC(College):
    def exam_ticket(self):
        return "BSC Exam Ticket"



obj = ClassRoomA()
print(obj.exam_ticket())
print(obj.timing())