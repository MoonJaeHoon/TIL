my_key = ['a','b','c','d']
my_val = [100,90,40,100]
input_dict = {k:v for k,v in zip(my_key,my_val)}

max_key = max(input_dict,key=lambda k: input_dict[k])
print(max_key)

my_key = ['a','b','c','d']
my_val = [100,90,40,100]
input_dict = {k:v for k,v in zip(my_key,my_val)}

max_key = max(input_dict,key=input_dict.get)
print(max_key)