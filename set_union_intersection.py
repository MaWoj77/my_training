en = int(input())
en_s = set(input().split())
fr = int(input())
fr_s = set(input().split())

new_set_union = en_s.union(fr_s)
new_set_intersection = en_s.intersection(fr_s)

print(len(new_set_union))
print(len(new_set_intersection))