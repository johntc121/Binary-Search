
'''
Iteratively and Recursively checks if a number is in a sequence.
'''
import doctest
       
def isMemberR(aseq, n):
    """(tuple, int) -> boolean

    Use binary search to check for membership
    of int n in sorted sequence, seq. Return 
    True if n is a member, else return False.

    >>> isMemberR((1, 2, 3, 3, 4), 4)
    True
    >>> isMemberR((1, 2, 3, 3, 4), 2)
    True
    >>> isMemberR('aeiou', 'i')
    True
    >>> isMemberR('aeiou', 'y')
    False
    >>> isMemberR((1, 3, 5, 7), 4)	    # even number of items in sequence - False
    False
    >>> isMemberR((23, 24, 25, 26, 27), 5)	    # odd number of items in sequence - False
    False
    >>> isMemberR((0, 1, 4, 5, 6, 8), 4)	# even number of items in sequence - True
    True
    >>> isMemberR((0, 1, 2, 3, 4, 5, 6), 3) # odd number of items in sequence - True
    True
    >>> isMemberR((1, 3), 1)		    # target is first (zeroth) item in sequence
    True
    >>> isMemberR((2, 10), 10)		    # target is last item in sequence
    True
    >>> isMemberR((99, 100), 101)		    # short sequence - False
    False
    >>> isMemberR((42,), 42)		    # one item sequence - True
    True
    >>> isMemberR((43,), 44)		    # one item sequence - False
    False
    >>> isMemberR((), 99)			    # empty sequence
    False
    """
    if len(aseq) == 0:
        return False
    else:
        mid = len(aseq) // 2

        if aseq[mid] == n:
            return True
        elif aseq[mid] > n:
            return(isMemberR(aseq[:mid], n))
        else:
            return(isMemberR(aseq[mid+1:], n))

def isMemberI(aseq, target):
    """(tuple, int) -> boolean

    Use binary search to check for membership
    of int n in sorted sequence seq. Return True
    if n is a member, else return False.
    

    >>> isMemberI((1, 2, 3, 3, 4), 4)
    True
    >>> isMemberI((1, 2, 3, 3, 4), 2)
    True
    >>> isMemberI((1, 3, 5, 7), 4)				# even number of items in sequence - False
    False
    >>> isMemberI((23, 24, 25, 26, 27), 5)		# odd number of items in sequence - False
    False
    >>> isMemberI((0, 1, 4, 5, 6, 8), 4)		# even number of items in sequence - True
    True
    >>> isMemberI((0, 1, 2, 3, 4, 5, 6), 3)	# odd number of items in sequence - True
    True
    >>> isMemberI((1, 3), 1)					# target is first (zeroth) item in sequence
    True
    >>> isMemberI((2, 10), 10)					# target is last item in sequence
    True
    >>> isMemberI((99, 100), 101)				# short sequence - False
    False
    >>> isMemberI((42,), 42)					# one item sequence - True
    True
    >>> isMemberI((43,), 44)					# one item sequence - False
    False
    >>> isMemberI((), 99)						# empty sequence
    False
    """
    if len(aseq) == 0:
        return False

    while len(aseq) > 0:
        #print(seq)
        mid = len(aseq) // 2

        if aseq[mid] == target:
            return True
        elif aseq[mid] > target:
            aseq = aseq[:mid]
        else:
            aseq = aseq[mid+1:]

    return False


print(doctest.testmod())
