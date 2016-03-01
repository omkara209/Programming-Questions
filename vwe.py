import numpy as np

def calc_lucky_num(xx,yy,zz):

	MOD = (10**9)+7
	#count = np.zeros((xx+1,yy+1,zz+1))
	#dp = np.zeros((xx+1,yy+1,zz+1))
	count = matrix = [[[0 for x in range(zz+1)]for x in range(yy+1)] for x in range(xx+1)]
	dp = matrix = [[[0 for x in range(zz+1)]for x in range(yy+1)] for x in range(xx+1)]
	result = 0
	#print(count)

	for x in range(0,xx+1):
		for y in range(0,yy+1):
			for z in range(0,zz+1):
				if  x == 0 and y == 0 and z == 0:
					count[x][y][z] = 1
				else:
					cnt = 0
					val = 0

					cnt = cnt + count[x-1][y][z]
					val += 4*count[x-1][y][z] + 10*dp[x-1][y][z]
				
					cnt = cnt + count[x][y-1][z]
					val += 5*count[x][y-1][z] + 10*dp[x][y-1][z]

					cnt = cnt + count[x][y][z-1]
					val += 6*count[x][y][z-1] + 10*dp[x][y][z-1]

					count[x][y][z] = cnt%MOD
					dp[x][y][z] = val%MOD

					result = result + dp[x][y][z]
					result = result%MOD

	print("Sum is: "+str(result))

my_input = input("Enter an input for X Y Z  (ex. 1 2 3): ")
rInput = my_input.split(" ")
calc_lucky_num(int(rInput[0]),int(rInput[1]),int(rInput[2]))


'''matrix = [[[0 for x in range(3)] for x in range(2)]for x in range(1)]
print(matrix)

matrix2 = np.zeros((1,2,3))
print(matrix2)'''