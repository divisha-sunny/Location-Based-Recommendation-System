import csv

# read flash.dat to a list of lists
datContent = [i.strip().split() for i in open("data\\ml-10M100K\\ratings.dat").readlines()]

# write it as a new CSV file
with open("data\\ml-10M100K\\ratings.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(datContent)