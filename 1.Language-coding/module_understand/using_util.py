
# remember to use from package.module_name import functions, class
from string_functions.util import get_encrypted_str, return_len, Cat
from Modules_and_Packages.my_package.module_inside_package import hi

result = get_encrypted_str("hello")
print(result)

result = return_len("hello")
print(result)

c = Cat()
print(c.get_cat_color())

hi()
