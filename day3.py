# part one
with open("day3.txt") as f:
    nums = [line for line in f.readlines()]

def find_gamma():
    
    half = len(nums) // 2
    one_count = {}
    gamma_binary = []
    
    
    for num in nums:
        num = num.strip()
        for i in range(12):
            if num[i] == "1":
                if i in one_count:
                    one_count[i] += 1
                else:
                    one_count[i] = 1
            if num[i] == "0":
                if i in one_count:
                    one_count[i] += 0
                else:
                    one_count[i] = 0
  
    for i in one_count:
        if one_count[i] > half:
          gamma_binary.append("1")
        else:
            gamma_binary.append("0")
    final_num = "".join(gamma_binary)
    print("gamma binary = ", final_num)
    return final_num

def find_epsilon(g_num):
    e_num = ""
    for num in g_num:
        if num == "1":
            e_num += "0"
        else:
            e_num += "1"
    return e_num

  
def binary_to_decimal(binary_num):
    dec_num = int(binary_num, 2)

    return dec_num
   