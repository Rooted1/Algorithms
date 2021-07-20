# method should return the node that is n nodes from the tail of the linked list

from linked_list import LinkedList, Node

test_list = LinkedList()
test_list.add('e')
test_list.add('d')
test_list.add('c')
test_list.add('b')
test_list.add('a')

test_result = test_list.n_from_last(0)

print(test_result)