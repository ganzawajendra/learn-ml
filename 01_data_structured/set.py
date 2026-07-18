data1 = {"Budi", "Ari", "Tata"}
data2 = {"Tata", "Dudung", "Rafli"}

# COMMON LIST METHOD
# uniq item, unordered

# =====================================
# .add(item) -> if item already in set, it deos nothing
# data1.add("Tatang") 
# data1.add("Budi")

# .update(set)
# data1.update(data2)
# data1.update({"Muna", "Abyan"})

# =====================================
# .remove(item) -> KeyError if the element doesn't exist
# data1.remove("Tata")
# data1.remove("Abdul")

# discard(item) -> not KeyError if the element doesn't exist
# data1.discard("Tata")
# data1.discard("Abdul")

# .pop() -> remove randomly, KeyError if the set is empty
# data1.pop()

# .clear()
# data1.clear()

# =====================================
# MATHEMATICAL OPERATION
# .union(set) -> combining everyone
# result = data1.union(data2)

# .difference(set) -> return set that contains the difference between two set
# result = data1.difference(data2)

# .difference_update(set) -> remove and update set the items that exist in other set
# data1.difference_update(data2)

# .intersection(set) -> return set that contains the similarity between two set
# result = data1.intersection(data2)

# .intersection_update(set) -> remove and update set the items that not contains between two set
# data1.intersection_update(data2)

# .isdisjoint(set) -> return True if the item doesn't contains in other set
# result = data1.isdisjoint(data2)

print(result)