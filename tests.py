import math
sequence1 = [1,0,1,1,0,1,0,1,0,0,1,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,1,1,0,0,0,1,1,0,1,0,0,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,1,0,1,0,0,0,1,0,0]
s2 = [1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,1,0,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,1,0,1,0,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,1,0,0,1,0,1,]

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


if __name__ == '__main__':
    #p_1 = frequency_bit_test(s2)
    #print(len(s2), p_1)
    identical_bits_test(s2)
    '''for i in range (0,4):
        print(i)'''