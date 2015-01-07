class HashTable(object):
	def __init__(self,size):
		self.size = size
		self.slots = [None] * self.size
		self.table = [None] * self.size

	def hash_gen(self,size,key):
		return (key%size)

	def put(self, key, data):
		hash_val = key % self.size
		if self.slots[hash_val] == None:
			self.slots[hash_val] = key
			self.table[hash_val] = data
		else:
			if self.slots[hash_val] == key:
				self.table[hash_val] == data
			else:
				self.hash_table_refactor()
				self.put(key,data)

	def hash_table_refactor(self):
		new_slots = [None] * (2 * self.size)
		new_table = [None] * (2 * self.size)
		new_size = len(new_slots)
		for i in range(0, len( self.slots)):
			if self.slots[i] != None:
				hash_val = self.slots[i] % new_size
				if new_slots[hash_val] == None:
					new_slots[hash_val] = self.slots[i]
					new_table[hash_val] = self.table[i]
		self.slots = new_slots
		self.table = new_table
		self.size = self.size * 2


	def print_table(self):
		print self.slots
		print self.table

