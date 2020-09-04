class Unit:
	def __init__(self,a,b):
		self.key=a
		self.val=b
		self.next=None
		self.prev=None


class LinkedList:
	def __init__(self,cap:int):
		self.element={}
		self.len=cap
		self.top=Unit(None,-1)
		self.tail=Unit(None,-1)
		self.top.next=self.tail
		self.tail.prev=self.top

	def get(self,key):
		if key in self.element.keys():
			cur=self.element[key]
			cur.prev.next=cur.next
			cur.next.prev=cur.prev
			cur.next=self.top.next
			cur.prev=self.top
			cur.next.prev=cur
			self.top.next=cur
			return self.element[key].val
		else:
			return -1

	def update(self,key,value):
		if key in self.element.keys():
			self.element[key].val=value
			cur=self.element[key]
			cur.prev.next=cur.next
			cur.next.prev=cur.prev
			cur.next=self.top.next
			cur.prev=self.top
			cur.next.prev=cur
			self.top.next=cur
		else:
			new_unit=Unit(key,value)
			new_unit.next=self.top.next
			new_unit.next.prev=new_unit
			new_unit.prev=self.top
			self.top.next=new_unit
			new_information={key:new_unit}
			self.element.update(new_information)
			if len(self.element)>self.len:
				self.element.pop(self.tail.prev.key)
				self.tail.prev=self.tail.prev.prev
				self.tail.prev.prev.next=self.tail


