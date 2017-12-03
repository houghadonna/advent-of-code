import csv

checksumA = 0
checksumB = 0

with open('2_checksum.tsv') as tsv:
	read = csv.reader(tsv, delimiter = "\t")
	for row in read:
		rowMin = None
		rowMax = None
		rowArr = []
		for col in row:
			i = 0			
			colInt = int(col)
			if rowMin == None:
				rowMin = colInt
				rowMax = colInt
			if colInt < rowMin:
				rowMin = colInt
			if colInt > rowMax:
				rowMax = colInt
			while i < len(rowArr):
				if (colInt % rowArr[i] == 0):
					checksumB = checksumB + (colInt / rowArr[i])
				elif (rowArr[i] % colInt == 0):
					checksumB = checksumB + (rowArr[i] / colInt)
				i+=1
			rowArr.append(colInt)
			print(rowArr, " - ", checksumB)

		checksumA = checksumA + (rowMax - rowMin)

print("ChecksumA = ", checksumA)
print("ChecksumB = ", checksumB)
exit 