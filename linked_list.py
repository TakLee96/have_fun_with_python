class Link:
	def __init__(self, first, rest=()):
		self.first = first
		if isinstance(rest, Link):
			self.rest = rest
		elif rest:
			rest = list(rest)
			self.rest = Link(rest[0], rest[1:])
		else:
			self.rest = ()

	def __len__(self):
		return 1 + len(self.rest)

	def __getitem__(self, index):
		def getitem(self, index):
			if index == 0:
				return self.first
			else:
				try:
					return getitem(self.rest, index - 1)
				except TypeError:
					raise IndexError("Linked List index out of bound")
				except AttributeError:
					raise IndexError("Linked List index out of bound")
		if index >= 0:
			return getitem(self, index)
		else:
			return getitem(self, len(self) + index)

	def __setitem__(self, index, value):
		def setitem(self, index, value):
			if index == 0:
				self.first = value
			else:
				try:
					setitem(self.rest, index - 1, value)
				except TypeError:
					raise IndexError("Linked List index out of bound")
				except AttributeError:
					raise IndexError("Linked List index out of bound")
		if index >= 0:
			setitem(self, index, value)
		else:
			setitem(self, len(self) + index, value)

	def __add__(self, other):
		if not self:
			return other
		elif not other:
			return self
		else:
			return Link(self.first, self.to_list[1:] + other.to_list)

	@property
	def to_list(self):
		return [elem for elem in self]

	def append(self, value):
		current = self
		while current.rest:
			current = current.rest
		current.rest = Link(value)

	def __repr__(self):
		rest_str = ""
		if self.rest:
			rest_str = ", " + repr(self.rest)
		return "Link({0}{1})".format(repr(self.first), rest_str)

	def __str__(self):
		return str(self.to_list())

	def __cmp__(self, other):
		return self.to_list == other.to_list

	def __contains__(self, value):
		return value in self.to_list
