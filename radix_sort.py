from time import perf_counter


def counting_sort(sequence, place):

	# ----------------------------- ex: 121 432 564 23 1 45 788 -----------------------------
	# ------------------------------------ place = 1 ----------------------------------------

	# ---------- INICIALIZAR ARRAYS ---------- #
	output = [0] * len(sequence)
	count = [0] * 10

	# ---------- COUNT DOS ELEMENTOS ---------- #
	for i in range(len(sequence)):
		index = sequence[i] // place  # 121 // 1 -> 121
		count[index % 10] += 1  # 121 % 10 -> 1, count de = +1

	# count = 0 2 1 1 1 1 0 0 1

	# ---------- SUM COUNT DOS ELEMENTOS ---------- #
	for i in range(1, 10):
		count[i] += count[i - 1]

	# count =  0 2 3 4 5 6 6 6 7

	# ---------- SORT ---------- #

	i = len(sequence) - 1  # i = 6
	while i >= 0:
		index = sequence[i] // place  # 788 // 1 -> 788
		output[count[index % 10] - 1] = sequence[i]  # output[count[8] - 1] = 788
		# count =  0 2 3 4 5 6 6 6 7
		# count[index % 10] - 1 = x 1 2 3 4 5 x x 6
		# output = 121 1 432 23 564 45 788
		count[index % 10] -= 1
		i -= 1

	for i in range(len(sequence)):
		sequence[i] = output[i]


def radix_sort_LSD(sequence):
	max_element = max(sequence)  # permite saber quantos loops fazer
	pos_digito = 1
	while max_element // pos_digito > 0:
		counting_sort(sequence, pos_digito)
		pos_digito *= 10


def main():
	sequence = []
	N = int(input())
	for i in range(N):
		sequence += [int(input())]

	tik = perf_counter()
	radix_sort_LSD(sequence)
	tok = perf_counter()
	total_time = tok - tik
	"""for element in sequence:
		print(element)"""
	print(total_time)
	with open("radix" + ".txt", "a") as writing:
		writing.write(str(total_time) + "\n")


if __name__ == "__main__":
	main()
