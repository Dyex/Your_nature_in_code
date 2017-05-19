# Maximise the matching substrings between two strings by using gaps only
# Ask for gap value mismatch value and match value at input

# Need to implement a tree to find all the possible solutions, this method only finds one of the best scoring solutions.
import numpy as np

print("Enter the nucleotide sequences")
string1 = input().strip().upper()
string2 = input().strip().upper()
len1 = len(string1)
len2 = len(string2)

print("Enter the gap penalty")
gap_value = int(input().strip())

print("Enter the match value")
match_value = int(input().strip())

print("Enter the mismatch penalty")
mismatch_value = int(input().strip())

gap = gap_value
first = []
second = []

#Initialising the matrix
matrix = np.zeros([len1+1,len2+1], dtype = int)
traceback = np.zeros([len1+1,len2+1], dtype = str)

'''def prob(a,b):
    if a == 'A' and b == 'G':
        return 5
    elif a == 'G' and b == 'A':
        return 5
    elif a == 'C' and b == 'T':
        return 4
    elif a == 'T' and b == 'C':
        return 4
    else:
        return 2'''


def Score(a,b,match_value,mismatch_value):
    if a == b:
        return match_value
    else:
        return mismatch_value

def Initialise_Traceback(matrix):
    traceback[0][0] = 'X'
    for i in range(1,len(string2)+1):
        matrix[0][i] = 'L'
    for i in range(1,len(string1)+1):
        matrix[i][0] = 'U'


def Initialse(matrix):
    gap = gap_value
    matrix[0][0] = 0

    for i in range(1,len2+1):
        matrix[0][i] = gap
        gap = gap + gap_value

    gap = gap_value

    for i in range(1,len1+1):
        matrix[i][0] = gap
        gap = gap + gap_value

def Max_Score(matrix,traceback):
    for i in range(1,len1+1):
        for j in range(1,len2+1):

            Maximum = max( matrix[i-1][j-1]
            #+ prob(string1[i],string2[j])
            +Score(string1[i-1],string2[j-1],match_value,mismatch_value),
            matrix[i-1][j]+gap, matrix[i][j-1]+gap)
            matrix[i][j] = Maximum

            if Maximum - gap == matrix[i-1][j]:
                traceback[i][j] = 'U'
            elif Maximum - gap == matrix[i][j-1]:
                traceback[i][j] = 'L'
            else:
                traceback[i][j] = 'D'

def Min_Score(matrix,traceback):
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            Minimum = min( matrix[i-1][j-1]
            #+ prob(string1[i],string2[j])
            +Score(string1[i-1],string2[j-1],match_value,mismatch_value),
            matrix[i-1][j]+gap, matrix[i][j-1]+gap)
            matrix[i][j] = Minimum
            if Minimum - gap == matrix[i-1][j]:
                traceback[i][j] = 'U'
            elif Minimum - gap == matrix[i][j-1]:
                traceback[i][j] = 'L'
            else:
                traceback[i][j] = 'D'

def Path(traceback,first,second):

    i = len(string1)
    j = len(string2)
    order = []
    start = traceback[i][j]
    node = start

    while(node != 'X'):
        order.append(node)
        if(node == 'D'):
            #node = 'P'
            node = traceback[i-1][j-1]
            i -= 1
            j -= 1
            first.append(string1[i])
            second.append(string2[j])
        elif(node == 'U'):
            #node = 'P'
            node = traceback[i-1][j]
            i -= 1
            first.append(string1[i])
            second.append('_')
        elif(node == 'L'):
            #node = 'P'
            node = traceback[i][j-1]
            j -= 1
            first.append('_')
            second.append(string2[j])
    return order

Initialse(matrix)
Initialise_Traceback(traceback)

if(gap_value >= 0):
    Min_Score(matrix,traceback)
else:
    Max_Score(matrix,traceback)

print("The following is the scoring matrix")
print(matrix)
print("The following is the traceback matrix")
print(traceback)
order = Path(traceback,first,second)
print("This is the order to be followed")
print(order)
print("First Nucleotide Alignment")
print(list(reversed(first)))
print("Second Nucleotide Alignment")
print(list(reversed(second)))
