states=['tamilnadu', 'kerala', 'andhra', 'karnataka', 'telungana']
print(states)
print("sorted list:", sorted(states))
print("original list:",states)
print("reversed using sorted():", sorted(states, reverse=True))
print("original list:",states)
states.reverse()
print("reversed list:", states)
states.reverse()
print("reversed again:", states)
states.sort()
print("sort list ", states)
states.sort(reverse=True)
print("reversed with sort", states)
print(states)