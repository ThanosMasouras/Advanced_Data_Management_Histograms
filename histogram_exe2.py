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


	return bins_boundaries, bins_values

def equidepth_histogram(income_data, bins):
	income_data.sort()
	bins_boundaries = []
	bins_values = []
	bin_size = len(income_data) // bins
	j = 0 
	for i in range(len(income_data)):
		if not bins_boundaries:
			bins_boundaries.append(income_data[i])
			bins_values.append(1)
		elif bins_values[j] < bin_size:
			bins_values[j] = bins_values[j] + 1
		elif j == bins -1:
			bins_values[j] = bins_values[j] + 1
			bins_boundaries.append(income_data[i])
		else:
			j = j + 1
			bins_values.append(1)
			bins_boundaries.append(income_data[i])

	return bins_boundaries, bins_values

def print_histograms(income_data, bins_boundaries1, bins_values1, bins_boundaries2, bins_values2):
	print('Number of rows with valid Income values:', len(income_data))
	print("Minimum income:", min(income_data))
	print("Maximum income", max(income_data))
	print("equiwidth:")
	for i in range(len(bins_boundaries1)-1):
		print("bin %d : [%.2f,%.2f),  numtuples:  %d)" % (i,bins_boundaries1[i],bins_boundaries1[i+1], bins_values1[i]))

	print("equidepth:")
	for i in range(len(bins_boundaries2)-1):
		print("bin %d : [%.2f,%.2f),  numtuples:  %d)" % (i,bins_boundaries2[i],bins_boundaries2[i+1], bins_values2[i]))

def get_ndata_from_range(bins_boundaries,bins_values, a,b):
	for i in range(len(bins_boundaries)-1):
		if a > bins_boundaries[i] and a< bins_boundaries[i+1]:
			a_bin = i
			
		
		if b > bins_boundaries[i] and b< bins_boundaries[i+1]:

			b_bin = i

	estimated_data = 0
	if a_bin == b_bin:
		diff = b - a
		diff_bin = bins_boundaries[b_bin+1] - bins_boundaries[a_bin]
		percentage = diff/diff_bin
		estimated_data = percentage * bins_values[a_bin]
	elif a_bin != b_bin:
		a_diff_bin = bins_boundaries[a_bin+1] - bins_boundaries[a_bin]
		a_percentage = (bins_boundaries[a_bin+1]-a) / a_diff_bin
		
		b_diff_bin = bins_boundaries[b_bin+1] - bins_boundaries[b_bin]
		b_percentage = (b-bins_boundaries[b_bin]) / b_diff_bin
		
		
		
		estimated_data = a_percentage*bins_values[a_bin] + b_percentage*bins_values[b_bin]
		for i in range(a_bin+1, b_bin):
			estimated_data += bins_values[i]
			
		
	print(estimated_data)

def get_actual_ndata(income_data,a,b):
	c = 0
	for i in range(len(income_data)-1):
		if income_data[i]>=a and income_data[i]<b:
			c += 1
	print(c)

def main():

	income_data = get_income_data('acs2015_census_tract_data.csv')
	a,b = equiwidth_histogram(income_data, 100)
	c,d = equidepth_histogram(income_data, 100)
	get_ndata_from_range(a,b,19000,55000)
	get_ndata_from_range(c,d,19000,55000)
	get_actual_ndata(income_data,19000,55000)



main()