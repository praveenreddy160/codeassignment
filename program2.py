input_file = "soccer.dat"

def read_soccer_data(input_file):

	with open(input_file, "r") as fb_obj:
		data = fb_obj.readlines()
	return data

def extract_cols(row):
	rows = row.split(" ")
	if len(rows) < 10:
		return False
	records = []
	index = 0 
	while len(records) < 10:
		try:
			value = rows[index].strip()
			index+=1
			if value == 'Team':
				break
			if len(value):
				records.append(value)
		except Exception as e:
			break
	indices_to_access = [1,6,8]
	if len(records) == 10:
		return list(map(records.__getitem__, indices_to_access))
	
	return []

def calculate_min_diff(data_list):
	max_diff_record = [10000, 0]
	for row in data_list:
		cols = extract_cols(row)
		if not cols:
			continue
		diff = abs(int(cols[1]) - int(cols[2]))
		if diff < max_diff_record[0]:
			max_diff_record[0] = diff
			max_diff_record[1] = cols
	return max_diff_record

if __name__ == "__main__":

	print(f"Reading the input file {input_file}")
	data = read_soccer_data(input_file)
	max_diff_record = calculate_min_diff(data)
	print(f"Team with smallest difference is {max_diff_record[0]} and Goals for and against are {max_diff_record[1][1]} and {max_diff_record[1][2]}")

