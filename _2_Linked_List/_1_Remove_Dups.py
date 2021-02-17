# Jacob Wahl
# <Date>
#
# Problem 2.1 - Write code to remove duplicates from an unsorted linked list.
#               FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?

from Linked_List import Linked_List


def removeDuplicates(list: Linked_List, use_datastructures=True) -> Linked_List:

    if len(list) <= 1:  # List is comprised of 1 or 0 elements
        return list

    # Using set
    if use_datastructures:
        seen = set()  # Store seen values here
        cur = list.head
        prev = None
        while cur != None:
            if cur.val in seen:
                # Remove cur from list
                prev.next = cur.next
            else:
                # Move on to next node
                seen.add(cur.val)
                prev = cur

            cur = cur.next

    else:  # Not using set
        cur = list.head
        while cur != None:
            runner = cur.next
            prev = cur
            # Cycle through list, checking if anything matches cur
            while runner != None:
                if runner.val == cur.val:
                    # Found matching val, must remove
                    prev.next = runner.next
                else:
                    prev = runner

                runner = runner.next
            cur = cur.next

    return list


test_case = Linked_List()
for i in [2, 2, 1, 2]:
    test_case.append(i)

print(removeDuplicates(test_case, False))
