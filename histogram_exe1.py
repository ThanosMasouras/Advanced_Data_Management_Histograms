#ATHANASIOS MASOURAS 2752
import csv
import numpy as np
from matplotlib import pyplot as plt


def get_income_data(file):
	income = []
	with open(file, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if row['Income'] != '':
				income.append(float(row['Income']))
	return income


def equiwidth_histogram(income_data, bins):
	min_income = min(income_data)
	max_income = max(income_data)
	bin_width = (max_income - min_income) / 100
	bins_boundaries = []
	bins_values = [0] * bins

	for i in range(bins+1):
		bins_boundaries.append(round(min_income + (bin_width*i),2))

	for i in range(len(income_data)):
		for j in range(bins):
			if income_data[i] == bins_boundaries[j]:
				bins_values[j] = bins_values[j] + 1
				break
			elif income_data[i] < bins_boundaries[j]:
				bins_values[j-1] = bins_values[j-1] + 1
				break
			elif income_data[i] > bins_boundaries[-2]:
				bins_values[-1] = bins_values[j-1] + 1
				break

	print_histogram(income_data, bins_boundaries, bins_values)

def equidepth_histogram(income_data, bin_size):
	income_data.sort()
	bins_boundaries = []
	bins_values = []
	j = 0 
	for i in range(len(income_data)):
		if not bins_boundaries:
			bins_boundaries.append(income_data[i])
			bins_values.append(1)
		elif bins_values[j] < bin_size:
			bins_values[j] = bins_values[j] + 1
		else:
			j = j + 1
			bins_values.append(1)
			bins_boundaries.append(income_data[i])

	print("equidepth:")
	for i in range(len(bins_boundaries)-1):
		print("range %d : [%d,%d),  numtuples:  %d)" % (i,bins_boundaries[i],bins_boundaries[i+1], bin_size))

	if len(bins_boundaries)%2 == 1:	
		print("range %d  : [%d,%d),  numtuples:  %d)" % (i+1,bins_boundaries[-1],bins_boundaries[-1], bins_values[-1]))

def print_histogram(income_data, bins_boundaries, bins_values):
	print('Number of rows with valid Income values:', len(income_data))
	print("Minimum income:", min(income_data))
	print("Maximum income", max(income_data))
	print("equiwidth:")
	for i in range(len(bins_boundaries)-1):
		print("range %d : [%d,%d),  numtuples:  %d)" % (i,bins_boundaries[i],bins_boundaries[i+1], bins_values[i]))


def main():

	income_data = get_income_data('acs2015_census_tract_data.csv')
	equiwidth_histogram(income_data, 100)
	equidepth_histogram(income_data, 729)


main()