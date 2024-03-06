import time

def chooseKey():
    c = 0
    while(True):
        print("Chọn loại khóa: ")
        print("1. Khóa 128 bit")
        print("2. Khóa 192 bit")
        print("3. Khóa 256 bit")
        c = int(input("Nhập lựa chọn: "))
        if(1 <= c <= 3):
            break
        else: 
            print("Nhập sai lựa chọn!")
    
    if(c == 1):
        print("Bạn chọn khóa 128 bit")
        return 10, 16, 128
    elif(c == 2):
        print("Bạn chọn khóa 192 bit")
        return 12, 24, 192
    elif(c == 3):
        print("Bạn chọn khóa 256 bit")
        return 14, 32, 256

N, numOfChr, typeOfKey = chooseKey()

#khóa
# key = "2b7e151628aed2a6abf7158809cf4f3c"

def inputKey():
    key = input("Nhập key: ")
    while(len(key) != numOfChr*2):
        key = input("Số kí tự không hợp lệ, bạn đã chọn khóa %d bit, nhập lại key gồm %d kí tự: "%(typeOfKey, numOfChr*2))
    return key

def checkKey(key):
    for i in range(len(key)):
        if((not(ord("a") <= ord(key[i]) <= ord("f")) and (not(ord('0') <= ord(key[i]) <= ord('9'))))):
            return False
    return True

key = inputKey()

while(not checkKey(key)):
    key = inputKey("Hãy nhập key là chuỗi hex")
        

plainText = "" 
# 112233445566778899887766554433
# plainText = "1122334"
encryptText = ""
#0xd70x250x50x110x100x390x770xcf0xcd0x470x400xe60xb80xc40xb40x330xf50xc60xf40x130x970x200xff0x2a0x10x6a0xcc0x540xc00xcb0xd70x98


keyMatrix = [None] * 240

s_box = [
#     0      1     2     3     4     5     6     7     8     9     A     B     C     D     E     F
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],# 0
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],# 1
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],# 2
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],# 3
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],# 4
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],# 5
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],# 6
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],# 7
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],# 8
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],# 9
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],# A
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],# B
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],# C
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],# D
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],# E
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]# F

inv_sbox = [
    [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
    [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
    [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
    [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
    [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
    [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
    [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
    [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
    [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
    [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
    [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
    [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
    [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
    [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
    [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]]

mixMatrix = [
        [2, 3, 1, 1], 
        [1, 2, 3, 1],
        [1, 1, 2, 3],
        [3, 1, 1, 2]]

invMixMatrix = [
        [0x0e, 0x0b, 0x0d, 0x09], 
        [0x09, 0x0e, 0x0b, 0x0d],
        [0x0d, 0x09, 0x0e, 0x0b],
        [0x0b, 0x0d, 0x09, 0x0e]]

rcon = [
    [0x01, 0x00, 0x00, 0x00],
    [0x02, 0x00, 0x00, 0x00], 
    [0x04, 0x00, 0x00, 0x00], 
    [0x08, 0x00, 0x00, 0x00], 
    [0x10, 0x00, 0x00, 0x00], 
    [0x20, 0x00, 0x00, 0x00], 
    [0x40, 0x00, 0x00, 0x00], 
    [0x80, 0x00, 0x00, 0x00], 
    [0x1b, 0x00, 0x00, 0x00], 
    [0x36, 0x00, 0x00, 0x00],
    [0x6c, 0x00, 0x00, 0x00],
    [0xd8, 0x00, 0x00, 0x00],
    [0xab, 0x00, 0x00, 0x00],
    [0x4d, 0x00, 0x00, 0x00],
    [0x9a, 0x00, 0x00, 0x00],
    [0x2f, 0x00, 0x00, 0x00]
]

#lấy phần tử trong bảng sbox
def getSbox(a):
    row = int(a / 0x10)
    column = int(a % 0x10)
    #print("gia tri can tim là sbox[%d][%d]: %d"%(row, column, s_box[row][column]))
    return s_box[row][column]

#lấy phần tử trong bảng inverse sbox
def getInvSbox(a):
    row = int(a / 0x10)
    column = int(a % 0x10)
    return inv_sbox[row][column]

# for i in range(256):
#     a = getSbox(i)
#     if(i != getInvSbox(a)): 
#         print(hex(i))
#         print(hex(getSbox(i)))
#         print(hex(getInvSbox(getSbox(i))))
    # print(hex(getSbox(i)))
    # print(hex(getInvSbox(i)))

#test hàm get_sbox
#print(hex(getSbox(0x12)))
# print(hex(getInvSbox(0x12)))

# hàm chuyển bản rõ thành mà trận trạng thái
def generateState(plainText):
    # plainText = input("Hãy Nhập bản rõ: "); 
    count = len(plainText)
    if(count % 16 == 0):
        # số ma trận trạng thái
        numState = int(count/16) 
        # print(numState)
        state = [[None] * 16] * numState
        
        for i in range(numState):
            lst = plainText[i*16: i*16 + 16]
            # print("lst: ", lst)
            state[i] = list(lst)
    else:
        numState = int(count/16) + 1
        state = [[None] * 16] * numState
        
        for i in range(numState - 1):
            lst = plainText[i*16: i*16 + 16]
            state[i] = list(lst)
        for i in range(16):
            if((numState - 1) * 16 + i < count):
                state[numState - 1][i] = plainText[(numState - 1) * 16 + i]
            else:
                state[numState - 1][i] = " "   #b'\x03'
    
    # print(state, i)
    for i in range(len(state)):
        for j in range(len(state[i])):
            state[i][j] = ord(state[i][j]) 
    return state

# hàm tạo ma trận trạng thái từ bản mã
def generateEncryptTextChr(encryptText):
    s = list(encryptText)
    numState = int(len(s) / 16)
    state = [[None]*2 for _ in range(numState)]
    for i in range(numState):
        state[i] = s[i*16 : i*16 + 16]
    for i in range(len(state)):
        for j in range(len(state[i])):
            state[i][j] = ord(state[i][j])
    return state

def generateEncryptText(encryptText):
    s = encryptText.split("0x")
    if(s[0] == ""): s.remove("")
    numState = int(len(s) / 16)
    state = [[None]*2 for _ in range(numState)]
    for i in range(numState):
        state[i] = s[i*16 : i*16 + 16]
    for i in range(len(state)):
        for j in range(len(state[i])):
            state[i][j] = int(state[i][j], 16)
    return state

def addRoundKey(arr, roundKey):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # print("arr =", arr[i][j],"rk = " , roundKey[j])
            arr[i][j] = arr[i][j] ^ roundKey[j]
            # print("result = ", arr[i][j])
    
    return arr

# #test hà addRoundKey
# a = [[0x04, 0x66, 0x81, 0xe5], [0x03, 0x62, 0x11, 0x85]]
# c = [[164, 156, 127, 242], [163, 152, 239, 146]]
# b = [0xa0, 0xfa, 0xfe, 0x17]
# print(addRoundKey(c, b))

def subBytes(arr):
    # print(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = getSbox(int(arr[i][j]))

    return arr

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b
def shift(arr):
    for i in range(3):
        arr[i], arr[i+1] = swap(arr[i], arr[i+1])
    return arr
def invShift(arr):
    for i in range(3, 0, -1):
        arr[i], arr[i-1] = swap(arr[i], arr[i-1])
    return arr

# a = [1, 2, 3, 4]
# print(invShift(a))
# print(invShift(a))

def shiftRows(arr):
    for k in range(len(arr)):
        for i in range(4):
            lst = arr[k][i * 4 : i * 4 + 4]
            for j in range(i):
                lst = shift(lst)
            for j in range(4):
                arr[k][i * 4 + j] = lst[j]
    return arr

def time2(a):
    a += a
    return a if (a < 256) else a ^ 0x11b 
def time3(a):
    b = a + a
    # print("b = ", b)
    if(b < 256):
        b ^= a
    else:
        b = b ^ 0x11b
        b ^= a
    return b if (b < 256) else b ^ 0x11b 

def mixColumns(arr):
    temp = [None] * 4   #ma trận chứa ma trận kết quả của phép nhân
    # result = [[None] * len(arr[0])]*len(arr)  #ma trận đích
    result = [[None]*len(arr[0]) for _ in range(len(arr))]
    # print(arr)
    for i in range(len(arr)):
        for j in range(4): # lấy từng cột thực hiện nhân ma trận
            for k in range(4): # tính kết quả từng phần tử trong cột
                for t in range(4): # lấy tưng phàn tử trong cột để thực hiên 
                    if(mixMatrix[k][t] == 2):
                        temp[t] = time2(arr[i][t*4 + j])
                    elif(mixMatrix[k][t] == 3):
                        temp[t] = time3(arr[i][t*4 + j])
                    else:
                        temp[t] = arr[i][t*4 + j]
                    # print("t = " , t , " k = " , k,"mix = ", mixMatrix[k][t], " arr: " , (arr[i][t*4 + j]), "temp",t," = " ,temp[t])

                result[i][k*4 + j] = temp[0] ^ temp[1] ^ temp[2] ^ temp[3]
                # print("i = ", i)
                # print("result: "  ,hex(result[i][k*4 + j]), "i", i, "k", k, "j", j)
                # print(arr)
                # print(result)
    
    return result
    
    

# #test hàm mixColumns
# a = [[0xd4, 0xe0, 0xb8, 0x1e, 0xbf, 0xb4, 0x41, 0x27, 0x5d, 0x52, 0x11, 0x98, 0x30, 0xae, 0xf1, 0xe5], 
#     [0xd4, 0xe4, 0xb4, 0x4e, 0xbf, 0x54, 0x51, 0x57, 0x5d, 0x32, 0x17, 0x88, 0x30, 0x9e, 0x51, 0xea]]
# arr = mixColumns(a)
# for i in range(len(arr)):
#     for j in range(len(arr[i])):    
#         if(j % 4 == 0): print()
#         print(hex(arr[i][j]), end=" ")
#     print()

def generateMatrixKey():
    for i in range(16):
        hexKey = key[i * 2: i * 2 + 2]
        # print(hexKey)
        keyMatrix[i] = int(hexKey, 16)
    
# n là lần lặp của mở rộng khóa
def rotWord(lst):
    for j in range(3): # đổi vị trí 0 cho 1 -> 1 cho 2 -> 2 cho 3 thì sẽ được 
        lst[j], lst[j + 1] = swap(lst[j], lst[j + 1])   
    # print("lst: ", lst)    
    return lst 

def subWords(lst):
    for i in range(4):
        lst[i] = getSbox(lst[i])
    return lst

def xorRcon(n, lst):
    for i in range(4):
        lst[i] ^= rcon[n][i]
    return lst

def xorKey(n, lst):
    for i in range(4):
        keyMatrix[(n+1)*16 + i] = keyMatrix[n*16 + i] ^ lst[i]
    for i in range(3):
        for j in range(4):
            keyMatrix[(n+1)*16 + 4 + i*4 + j] = keyMatrix[n*16 + 4 + i*4  + j] ^ lst[j]


def keyExpansion():
    generateMatrixKey()
    # print(keyMatrix)
    tempMatrix = [None] * 4
    for i in range(N):
        # print("i = ", i)
        tempMatrix = keyMatrix[i*16 + 3*4: i*16 + 3*4 + 4]
        # print("temp = ", tempMatrix)
        tempMatrix = rotWord(tempMatrix)
        # print(tempMatrix)
        tempMatrix = subWords(tempMatrix)
        # print(tempMatrix)
        tempMatrix = xorRcon(i, tempMatrix)
        # print(tempMatrix)
        xorKey(i, tempMatrix)
        # print(keyMatrix)
    
# keyExpansion()
# key = "2b7e151628aed2a6abf7158809cf4f3c"


def invShiftRow(arr):
    for k in range(len(arr)):
        for i in range(4):
            lst = arr[k][i * 4 : i * 4 + 4]
            for j in range(i):
                lst = invShift(lst)
            for j in range(4):
                arr[k][i * 4 + j] = lst[j]
    return arr

# a = [[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4], [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]]
# print(invShiftRow(a))

def invSubBytes(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = getInvSbox(int(arr[i][j]))

    return arr

# a = [[0xd4, 0xe0, 0xb8, 0x1e, 0x27, 0xbf, 0xb4, 0x41, 0xd4, 0xe0, 0xb8, 0x1e, 0x27, 0xbf, 0xb4, 0x41],
#      [0xd4, 0xe0, 0xb8, 0x1e, 0x27, 0xbf, 0xb4, 0x41, 0xd4, 0xe0, 0xb8, 0x1e, 0x27, 0xbf, 0xb4, 0x41]]
# [print(hex(i), end=" ") for item in invSubBytes(a) for i in item]


# 9 = 1001
def time9(a):
    result = (a << 3) ^ a
    if(result >= (256 << 2)):
        result ^= (0x11b << 2)
    if(result >= (256 << 1)):
        result ^= (0x11b << 1)
    if(result >= (256)):
        result ^= (0x11b)
    result &= 0xff
    return result
def timeB(a):
    result = (a << 3) ^ (a << 1) ^ a
    if(result >= (256 << 2)):
        result ^= (0x11b << 2)
    if(result >= (256 << 1)):
        result ^= (0x11b << 1)
    if(result >= (256)):
        result ^= (0x11b)
    result &= 0xff
    return result
def timeD(a):
    result = (a << 3) ^ (a << 2) ^ a
    if(result >= (256 << 2)):
        result ^= (0x11b << 2)
    if(result >= (256 << 1)):
        result ^= (0x11b << 1)
    if(result >= (256)):
        result ^= (0x11b)
    result &= 0xff
    return result
def timeE(a):
    result = (a << 3) ^ (a << 2) ^ (a << 1)
    if(result >= (256 << 2)):
        result ^= (0x11b << 2)
    if(result >= (256 << 1)):
        result ^= (0x11b << 1)
    if(result >= (256)):
        result ^= (0x11b)
    result &= 0xff
    return result



def invMixColumns(arr):
    temp = [None] * 4   #ma trận chứa ma trận kết quả của phép nhân
    # result = [[None] * len(arr[0])]*len(arr)  #ma trận đích
    result = [[None]*len(arr[0]) for _ in range(len(arr))]
    # print(arr)
    for i in range(len(arr)):
        for j in range(4): # lấy từng cột thực hiện nhân ma trận
            for k in range(4): # tính kết quả từng phần tử trong cột
                for t in range(4): # lấy tưng phàn tử trong cột để thực hiên 
                    if(invMixMatrix[k][t] == 0x09):
                        temp[t] = time9(arr[i][t*4 + j])
                    elif(invMixMatrix[k][t] == 0x0b):
                        temp[t] = timeB(arr[i][t*4 + j])
                    elif(invMixMatrix[k][t] == 0x0d):
                        temp[t] = timeD(arr[i][t*4 + j])
                    else:
                        temp[t] = arr[i][t*4 + j]
                        temp[t] = timeE(arr[i][t*4 + j])
                result[i][k*4 + j] = temp[0] ^ temp[1] ^ temp[2] ^ temp[3]
    
    return result

# a = [[0x04, 0xe0, 0x48, 0x28, 0x66, 0xcb, 0xf8, 0x06, 0x81, 0x19, 0xd3, 0x26, 0xe5, 0x9a, 0x7a, 0x4c], 
#      [0x04, 0xe0, 0x48, 0x28, 0x66, 0xcb, 0xf8, 0x06, 0x81, 0x19, 0xd3, 0x26, 0xe5, 0x9a, 0x7a, 0x4c]]
# [print(hex(i), end=" ") for item in invMixColumns(a) for i in item]

    
def myPrint(my_list):
    my_string = ''.join([hex(i) for sublist in my_list for i in sublist])
    # my_string = ''.join([chr(i) for sublist in my_list for i in sublist])
    print("Bản mã hóa: ", my_string)

def encrypt(plainText):
    state = generateState(plainText)
    keyExpansion()
    # print(keyMatrix)
    w0 = keyMatrix[:16]
    # print("w0 =", w0)
    state = addRoundKey(state, w0)
    # print("add round key 1: state = ", state)

    for i in range(N - 1):
        state = subBytes(state)
        # print("subbyte: ", state)
        state = shiftRows(state)
        # print("shifrow: ",state)
        state = mixColumns(state)
        # print("mixcol: ", state)
        w = keyMatrix[(i+1)*16:(i+1)*16 + 16]
        # print("i = ", i, "  w = ", w)
        state = addRoundKey(state, w)
        # print("addroukey: ", state)
    
    state = subBytes(state)
    state = shiftRows(state)
    wEnd = keyMatrix[N*16:N*16 + 16]
    # print("wend = ", wEnd)
    state = addRoundKey(state, wEnd)
    # print("ket qua: ", state)

    # print("bản rõ: ", plainText)
    # print("khóa: ", key)

    # print("bản mã: ", end="")
    # print(state)
    myPrint(state)
    # state = [[241, 156, 28, 253, 225, 227, 106, 143, 103, 170, 166, 218, 169, 113, 6, 3], [99, 115, 151, 206, 57, 6, 193, 40, 127, 226, 215, 37, 82, 41, 217, 100]]
    # for i in range(2):
    #     for j in range(16):
    #         print(chr(state[i][j]), end="")
    # s = "ñ∟ýáãjgª¦Ú©q♠♥csÎ9♠Á(â×%R)Ùd"

    # print("bản giải: ", end="")
    # for i in range(len(s)):
    #     print(ord(s[i]), end=" ")

def decrypt(plainText):
    state = generateEncryptText(plainText)
    # state = generateEncryptTextChr(plainText)
    # print(state)
    # print(len(state))
    keyExpansion()
    # print(keyMatrix)
    # print(len(keyMatrix))
    wEnd = keyMatrix[N*16:N*16 + 16]
    # print(wEnd)
    state = addRoundKey(state, wEnd)
    # print(state)
    state = invShiftRow(state)
    state = invSubBytes(state)
    
    for i in range(N, 1, -1):
        w = keyMatrix[(i-1)*16:(i-1)*16 + 16]
        # print("i = ", i, "  w = ", w)
        state = addRoundKey(state, w)
        state = invMixColumns(state)
        state = invShiftRow(state)
        state = invSubBytes(state)     
        
        # print(state)

    

    w0 = keyMatrix[0:16]
    # print("w0: ", w0)
    # print(state)
    state = addRoundKey(state, w0)
    # print(state)
    print("bản giải mã: ", end="")
    [print(chr(i), end="") for item in state for i in item]


def mainTest():
    state = generateState()
    # print(plainText)
    keyExpansion()
    w0 = keyMatrix[:16]
    state = addRoundKey(state, w0)
    for i in range(N - 1):
        state = subBytes(state)
        state = shiftRows(state)
        # state = mixColumns(state)
        w = keyMatrix[(i+1)*16:(i+1)*16 + 16]
        state = addRoundKey(state, w)
    state = subBytes(state)
    state = shiftRows(state)
    wEnd = keyMatrix[10*16:10*16 + 16]
    state = addRoundKey(state, wEnd)
    # print(state)
    myPrint(state)

    

    # print(state)
    keyExpansion()
    wEnd = keyMatrix[10*16:10*16 + 16]
    state = addRoundKey(state, wEnd)
    state = invShiftRow(state)
    state = invSubBytes(state)
    
    for i in range(N, 1, -1):
        w = keyMatrix[(i-1)*16:(i-1)*16 + 16]
        state = addRoundKey(state, w)
        # state = invMixColumns(state)
        state = invShiftRow(state)
        state = invSubBytes(state)     
    w0 = keyMatrix[0:16]
    state = addRoundKey(state, w0)
    # print(state)
    [print(chr(i), end="") for item in state for i in item]

# mainTest()

#hàm main
def main():
    print("Key: ", key)
    plainText = input("Nhap bản rõ: ")
    start = time.perf_counter()
    encrypt(plainText)
    end = time.perf_counter()
    print(f"Thời gian mã hóa: {end - start:0.4f} giây")
    encryptText = input("Nhập bản mã: ")
    start1 = time.perf_counter()
    decrypt(encryptText)
    end1 = time.perf_counter()
    print(f"\nThời gian giải mã: {end1 - start1:0.4f} giây")
    

#chạy hàm main
main()



# test cac ham
# state = generateState()
# keyExpansion()
# w0 = keyMatrix[0:16]

# # print(w0)
# print(state)
# n = 10
# for i in range(n):
#     state = addRoundKey(state, w0)
#     state = subBytes(state)
#     state = shiftRows(state)
#     state = mixColumns(state)
#     print("i = ", i, "state = ", state[1])
# print(state)
# for i in range(n):
#     print("i = ", i, "state = ", state[1])
#     state = invMixColumns(state)
#     state = invShiftRow(state)
#     state = invSubBytes(state)
#     state = addRoundKey(state, w0)

# print(state)





