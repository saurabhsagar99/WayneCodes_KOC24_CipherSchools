class Date:
	def __init__(self, d, m, y):
		self.d = d
		self.m = m
		self.y = y

monthDays = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]

def countLeapYears(d):
	years = d.y

	if (d.m <= 2):
		years -=1
	ans = int(years / 4)
	ans -= int(years / 100)
	ans += int(years / 400)
	return ans



def getDifference(dob, presentdate):

	n1 = dob.y * 365 + dob.d

	for i in range(0, dob.m - 1):
		n1 += monthDays[i]

	n1 += countLeapYears(dob)
	n2 = presentdate.y * 365 + presentdate.d
	for i in range(0, presentdate.m - 1):
		n2 += monthDays[i]
	n2 += countLeapYears(presentdate)


	return (n2 - n1)

dob= input("Enter Your DOB as DD/MM/YYYY:")
dob=[int(i) for i in dob.split("/")]
dob=Date(dob[0],dob[1],dob[2])
presentdate =input("Enter Present Day as DD/MM/YYYY:")
presentdate=[int(i) for i in present.split("/")]
presentdate=Date(presentdate[0],present[1],presentdate[2])

print("The no days person alive:",getDifference(dob,presentdate))

