import random

s_midl = "asdfghjkl"
s_low = "zxcvbnm"
s_upp = "qwertyuiop"
all_sim = "asdfghjklzxcvbnmqwertyuiop"

list_letter = [s_midl, s_low, s_upp, all_sim]
level = 0
count_attempt = 16
count_len = 10

# random.sample(population, k) - список длиной k из последовательности population. Значение не повторяються.
# psw = ''.join([random.choice(ls) for x in range(12)]) значения могут повторяться.
for i in range(0, count_attempt):
    s_question = ''.join([random.choice(list_letter[level]) for x in range(count_len)])

    print(s_question)
    s_ask = input("input string : ")

    if s_ask == s_question:
        print("ok")
        count_attempt -= 1
        # count_len += 1

        if count_attempt < 13:
            level = 1
        if count_attempt < 9:
            level = 2
        if count_attempt < 5:
            level = 3
    else:
        print("try another")
