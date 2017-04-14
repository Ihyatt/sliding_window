import re
class HomeValues:
	def __init__(self, _file):
		self._file = _file

	def increasing_sub_sequence(self):
		#opens  and parses input file passed in through class initialization
		new_file = open(self._file).readlines()
		window = int(new_file[0].split(" ")[1])
		days = new_file[1].split(" ")
		for day in days:
			day = int(day)
		if window > len(days):
			return "invalid input"

		#storage of windows
		increase = {}
		decrease = {}
		
		#set of iterations which will track increasing or dercreasing sequences
		for i in range(len(days) - (window - 1)):
			increase[i] = []
			decrease[i] = []
			
			day = i
			while day < (i + window):
				start = day
				end = i + window - 1
				increasing_sub_seq = []
				decreasing_sub_seq = []
				while start < end:
					if days[start] < days[start + 1]:
						if days[start] not in increasing_sub_seq:
							increasing_sub_seq.append(days[start])
						if days[start + 1] not in increasing_sub_seq:
							increasing_sub_seq.append(days[start + 1])

						if [days[start], days[start + 1]] not in increase[i]:
							increase[i].append([days[start], days[start + 1]])

					if days[start] > days[start + 1]:
						decreasing_sub_seq.append(days[start])
						if days[start] not in decreasing_sub_seq:
							decreasing_sub_seq.append(days[start])
						if days[start + 1] not in decreasing_sub_seq:
							decreasing_sub_seq.append(days[start + 1])
						
						if [days[start], days[start + 1]] not in decrease[i]:
							decrease[i].append([days[start], days[start + 1]])
					start += 1

				if len(increasing_sub_seq) > 1:
					if increasing_sub_seq not in increase[i]:
						increase[i].append(increasing_sub_seq)
				if len(decreasing_sub_seq) > 1:
					if decreasing_sub_seq not in decrease[i]:
						decrease[i].append(decreasing_sub_seq)
				day += 1
		#prints differences of increasing vs decreasing sequences
		for i in range(len(days) - (window - 1)):
			total = len(increase[i]) - len(decrease[i])
			print total

if __name__ == '__main__':
	f = HomeValues('input.txt')
	print f.increasing_sub_sequence()
	g = HomeValues('input2.txt')
	print g.increasing_sub_sequence()
	h = HomeValues('input3.txt')
	print h.increasing_sub_sequence()



