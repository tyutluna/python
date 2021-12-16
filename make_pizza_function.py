# we can call the functions from other file by import
# module_name.function_name()
import pizza_function_arbitrary_argument

# call all of the function from that file
pizza_function_arbitrary_argument.make_pizza(16, 'pepperoni')
pizza_function_arbitrary_argument.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# we can also just import specific functions
# by from module_name import function_name
# from module_name import function_0, function_1, function_2

