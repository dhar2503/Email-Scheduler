import csv

with open('scripts/Spring_User.csv','w') as csvfile:
	fieldnames = ['From Email','Body','Subject','Receiver']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	with open('scripts/mail_path_1.txt') as f1:
		for line1 in f1:
			file = line1
			with open(file) as f2:
				reader = csv.DictReader(f2)
				for row in reader:			
					with open('scripts/Mail_User.txt','r') as f:
						for line in f:
							cleanedLine = line.strip()
							writer.writerow({'From Email':row['From Email'], 'Body':row['Body'],'Subject': row['Subject'],'Receiver':cleanedLine+'@email.local'})
		