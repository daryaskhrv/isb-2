import numpy
import math

sequence = [1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,1,0,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,1,0,1,0,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,1,0,0,1,0,1,]

def frequency_bit_test (sequence: list) -> float:
    sum = 0
    for i in sequence:
        if i == 0:
            sum += -1
        else:
            sum += 1
    Sn = abs(sum)/(math.sqrt(len(sequence)))
    return math.erfc(Sn/math.sqrt(2))


def identical_bits_test(sequence: list) -> float:
    N=len(sequence)
    part1 = sequence.count(1)/N
    if not abs(part1-0.5) < 2/math.sqrt(N):
        return 0
    Vn = 0
    for i in range (0,N-1):
        if sequence[i] != sequence[i+1]:
            Vn += 1
    return math.erfc((abs(Vn -2*N*part1*(1-part1)))/(2*math.sqrt(2*N)*part1*(1-part1)))


def longest_sequence_test(sequence: list)-> float:
    bloks = numpy.array_split(sequence, 16)
    result=[]
    for blok in bloks:
        ones = 0
        max_ones = 0
        for i in blok:
            if i == 1:
                ones+=1
                max_ones = max(ones, max_ones)
            else:
                ones = 0
        result.append(max_ones)
    V=[result.count(0)+result.count(1),result.count(2),result.count(3),result.count(4)+result.count(5)+result.count(6)+result.count(7)+result.count(8)]
    pi = [0.2148, 0.3672, 0.2305, 0.1875]
    squareX = 0
    s=0
    for i in range (0,4):
        squareX += (pow((V[i]-16*pi[i]),2))/(16*pi[i])
    return squareX/2
            

if __name__ == '__main__':
    test1 = frequency_bit_test(sequence)
    #0.5958830905651779
    test2 = identical_bits_test(sequence)
    #0.4632060528974583
    test3 = longest_sequence_test(sequence)
    #squareX = 0.9697299296305197
    #gamma_function = 0.80857342