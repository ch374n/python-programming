# program to execute all dependancies of task before execution of task itself

class Task:
	def __init__(self, name, dependancies = None):
		self.name = name
		self.dependancies = dependancies
		self.state = False 

	def execute(self):
		if self.dependancies is not None:
			for task in self.dependancies:
					if task.state is False:
						task.execute()
		print('executing : ' + self.name)
		self.state = True

def main():
	
	task_e = Task('E')
	task_d = Task('D', [task_e])
	task_a = Task('A')
	task_b = Task('B', [task_a])
	task_c = Task('C', [task_b, task_a, task_d])
	task_f = Task('F', [task_c])
	task_f.execute()

main()
