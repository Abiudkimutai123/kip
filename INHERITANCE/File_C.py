from File_A import ParentClass


obj = ParentClass()
obj.parentClassMethod()
obj.calculatenums(100,400)
obj.multiplynums(250,2)
obj.dividenums(5000,2)

from File_B import ChildClass



obj = ChildClass()
obj.childClassMethod()
from File_B import NumberClass

obj = NumberClass()
obj.numberClassMethod()
