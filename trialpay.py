import sys
import os

#1
# Check if string A is permatuation of string b
# O(n) solution

def isPerm(a,b):

	if len(a) == len(b):
		myDict = {}

		# Check if a char key already in dict
		# if it does, increment the count by 1, otherwise set it to 1
		for x in a:
			if x in myDict:
				myDict[x] = myDict[x] + 1
			else:
				myDict[x] = 1
		
		# Check if a char key exist in dict
		# If it does, decrement the count by 1				
		for x in b:
			if x in myDict:
				myDict[x] = myDict[x] - 1

		#check each value in myDict
		for key,value in myDict.items():
			if value != 0:
				return False

		return True	

	else:
		return False


'''print(isPerm('',''))
	print(isPerm('hello','elloh'))
	print(isPerm('hello','dfdfdfwwewwe'))

'''


#2 Check for Valid IP address
# Output : 'IPv4','IPv6','Neither'
#Best method would be using Regrex

def is_hex(s):
	try:
		int(s,16)
		return True
	except ValueError:
		return False


def checkIP(input_array):

	for x in range(0,len(input_array)):
		if '.' not in input_array[x] and ':' not in input_array[x]:
			print('Neither')
			continue
		
		#check for case if both . and : in the string (Invalid)
		if ('.' in input_array[x] and ':' in input_array[x]):
			print('Neither')
			continue

		#This is a good candidate for ipv4
		if '.' in input_array[x]:
			ip4 = input_array[x].split('.')
			#Check for the length of ipv4 address
			if len(ip4) !=4:
				print('Neither')
				continue

			#Check if all the substring in ip4 are between 0 and 255, and they are not letters
			bCriteria = True
			for x in ip4:
				if not x.isdigit():
					bCriteria = False
					break
				
				if int(x) < 0 or int(x) > 255:
					bCriteria = False
					break

			if bCriteria:
				print('IPv4')
			else:
				print('Neither')

		#This is a good candidate for ipv6
		else:
			ip6 = input_array[x].split(':')
			#Check for the length of ipv4 address
			if len(ip6) != 8:
				print('Neither')
				continue
			#Check if all the substring are hex characters
			bCriteria = True

			for x in ip6:
				# 0 and empty space are allowed in IPv6
				if x == '' or x == '0':
					continue

				if not is_hex(x):
					bCriteria = False
					break

			if bCriteria:
				print('IPv6')
			else:
				print('Neither')


ip_array = ['this is junk test', '','test','127.54:33.1', '127.0.0.1','999.999.34434.22','127.ada.fdfd.0','2602:306:c47e:e130:ed37:8cb1:4354:a31','2602:306:c47e:e130:ed37:8cb1::b31']
#checkIP(ip_array)




#3 Given N intergers, count the total pairs of intergers that hav the difference K
#This can be implemented using hash in O(n), brute force is also an option with O(n2)
def find_diff(aList,diff):
	
	myDict = {}
	for x in aList:
		if x in myDict:
			myDict[x] = myDict[x]+1
		else:
			myDict[x] = 1
	count=0
	for x in aList:
		temp = x + diff
		if temp in myDict:
			if (temp != x):
				count = count+1
			elif (myDict[temp] > 1):
				count = count+1

	return count

count = find_diff([1,5,3,4,2],2)
#print(count)


'''
public class Solution {
    static long mod = 1000000007;

    public static void main(String[] args) throws IOException {
        InputReader reader = new InputReader(System.in);
        int X = reader.readInt();
        int Y = reader.readInt();
        int Z = reader.readInt();
        long[][][] c = new long[X+1][Y+1][Z+1];
        long[][][] dp = new long[X+1][Y+1][Z+1];
        long answer = 0;
        for (int x=0; x<=X; x++) {
            for (int y=0; y<=Y; y++) {
                for (int z=0; z<=Z; z++) {
                    if (x == 0 && y == 0 && z == 0) {
                        c[x][y][z] = 1;
                    } else {
                        long count = 0;
                        long value = 0;
                        if (x > 0) {
                            count += c[x-1][y][z];
                            value += 4*c[x-1][y][z]+10*dp[x-1][y][z];
                        }
                        if (y > 0) {
                            count += c[x][y-1][z];
                            value += 5*c[x][y-1][z]+10*dp[x][y-1][z];
                        }
                        if (z > 0) {
                            count += c[x][y][z-1];
                            value += 6*c[x][y][z-1]+10*dp[x][y][z-1];
                        }
                        c[x][y][z] = count%mod;
                        dp[x][y][z] = value%mod;
                        answer += dp[x][y][z];
                        answer %= mod;
                    }
                }
            }
        }
        System.out.println(answer);
    }'''

import numpy as np

def calc_lucky_num(xx,yy,zz):

	MOD = (10**9)+7
	count = np.zeros((xx+1,yy+1,zz+1))
	dp = np.zeros((xx+1,yy+1,zz+1))
	result = 0

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

	print("Sum is: "+str(result))


my_input = input("Enter an input for X Y Z  (ex. 1 2 3): ")
rInput = my_input.split(" ")
calc_lucky_num(int(rInput[0]),int(rInput[1]),int(rInput[2]))