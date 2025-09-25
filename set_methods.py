en = int(input())
en_s = set(input().split())
fr = int(input())
fr_s = set(input().split())

new_set_union = en_s.union(fr_s)
new_set_intersection = en_s.intersection(fr_s)
new_set_difference = en_s.difference(fr_s)
new_set_s_difference = en_s.symmetric_difference(fr_s)

print(len(new_set_union))
print(len(new_set_intersection))
print(len(new_set_difference))
print(len(new_set_s_difference))