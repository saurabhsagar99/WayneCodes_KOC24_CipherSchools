class Date:
	def __init__(self, d, m, y):
		self.d = d
		self.m = m
		self.y = y

monthDays = [31, 28, 31, 30, 31, 30,31,31,30,31,30,31]


def countLeapYears(d):

	years = d.y
	if (d.m <= 2):
		years -= 1
	ans = int(years / 4)
	ans -= int(years / 100)
	ans += int(years / 400)
	return ans


def getDifference(dt1, dt2):
	n1 = dt1.y * 365 + dt1.d

	for i in range(0, dt1.m - 1):
		n1 += monthDays[i]

	
	n1 += countLeapYears(dt1)


	n2 = dt2.y * 365 + dt2.d
	for i in range(0, dt2.m - 1):
		n2 += monthDays[i]
	n2 += countLeapYears(dt2)


	return (n2 - n1)


dob=input("Enter your DOB as DD/MM/YYYYY : ")
dob=[int(i) for i in dob.split("/")]
dob=Date(dob[0],dob[1],dob[2])
PD=input("Enter Present Day as DD/MM/YYYYY : ")
PD=[int(i) for i in PD.split("/")]
PD=Date(PD[0],PD[1],PD[2])


print("\nThe number of days the person is alive:",getDifference(dob, PD))
