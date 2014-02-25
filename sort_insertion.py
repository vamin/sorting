import fileinput
from timer import Timer

l = []
for i in fileinput.input():
    l.append(int(i))

def sort_insertion(l):
    for i in xrange(1, len(l)):
        j = i
        while j > 0 and l[j-1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]
            j = j-1
    return l

def sort_insertion_n_mem(l):
    for i in xrange(1, len(l)):
        j = i
        while j > 0 and l[j-1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]
            j = j-1
    return l

in_place = True
with Timer() as t:
    if in_place:
        l = sort_insertion(l)
    else:
        l = sort_insertion_n_mem(l)

print l
print('List length: %i' % len(l))
print('Sort time: %.05fs' % t.interval)