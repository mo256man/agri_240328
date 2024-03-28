import psutil
import datetime

class Memory():
	def __init__(self):
		self.filename = "memory.csv"
		self.process = psutil.Process()
		memory_info = self.process.memory_info()
		self.memory = psutil.virtual_memory()
		self.is_available = False

	def show(self, text):
		if self.is_available:
			memory_info = self.process.memory_info()
			rss = memory_info.rss
			vms = memory_info.vms

			total = self.memory.total
			available = self.memory.available
			percent = self.memory.percent
			used = self.memory.used
			free = self.memory.free
			active = self.memory.active

			str_date = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")
			msg = f"{str_date},{text},{rss},{vms},{total},{available},{percent},{used},{free},{active}\n"
			with open(self.filename, "a", encoding="utf-8") as f:
				f.write(msg)

if __name__ == "__main__":
	memory = Memory()
	memory.show("個別")
	print("done.")
