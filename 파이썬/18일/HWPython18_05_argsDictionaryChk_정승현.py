#HWPython18_05_argsDictionaryChk_정승현.py

def print_kwargs(**kwargs):
	print(kwargs)
	Keys = kwargs.keys()
	Value1 = kwargs.values()
	items1 = kwargs.items()
	print(Keys)
	print(Value1)
	print(items1)
print_kwargs(a=1)
print_kwargs(name='foo',age=3)

#-------------------------------------------------------------------------------------------------------------
