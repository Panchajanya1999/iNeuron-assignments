# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):

        # create a function that will append the 
        # nodes in a list
        def ll_list(ll):
            _list = []
            currn = ll
            while currn is not None:
                _list.append(currn.val)
                currn = currn.next
            return _list
        
        # function to reverse a list
        def revlist(l):
            _list = []
            for i in range(len(l)-1, -1, -1):
                _list.append(l[i])
            return _list
        
        # function to rverse a int
        def revint(n):
            rev = 0
            while n > 0:
                rev = rev * 10 + n % 10
                n //= 10
            return rev
        
        # function to convert a list
        # to an integer
        def listint(list):
            integer = 0
            for digit in list:
                integer *= 10
                integer += digit

            return integer
        
        # function to convert an integer
        # to a list
        def intlist(integer):
            list_of_digits = []
            if integer == 0:
                list_of_digits.append(0)
                return list_of_digits
            while integer > 0:
                remainder = integer % 10
                list_of_digits.append(remainder)
                integer //= 10

            return list_of_digits
        
        # function to convwert list to LL
        def list_to_linked_list(list):
            head = None
            current_node = None
            for item in list:
                new_node = ListNode(item)
                if head is None:
                    head = new_node
                    current_node = new_node
                else:
                    current_node.next = new_node
                    current_node = new_node

            return head

        
        # convert the ll to a list
        _list1 = revlist(ll_list(l1))
        _list2 = revlist(ll_list(l2))
        #print(_list1)
        #print(_list2)

        # convert them to ints
        int1 = listint(_list1)
        int2 = listint(_list2)
        #print(int1, int2)

        # reverse them
        int1 = revint(int1)
        int2 = revint(int2)
        #print(int1, int2)

        # add the integrs
        sum = int1 + int2
        #print(sum)

        l1 = intlist(sum)
        #print(l1)

        return list_to_linked_list(l1)

# create a linked list
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# create a linked list
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# create an instance of the class
sol = Solution()

# call the function
result = sol.addTwoNumbers(l1, l2)

# print the result
while result is not None:
    print(result.val, end=" ")
    result = result.next
print()
