from itertools import permutations
import keyword
import random

def has_prime_perm(num,r=2):
    total_list = get_count_of_permutations(num,r)
    for x in total_list:
        if(check_prime_or_not(x)):
            return True
    return False

def has_only_prime_perms(num,r=2):
    total_list = get_count_of_permutations(num,r)
    for x in total_list:
        if(not check_prime_or_not(x)):
            return False
    return True
    
def prime_perms(num,r=2):
    new_list = []
    total_list = get_count_of_permutations(num,r)
    for x in total_list:
        if(check_prime_or_not(x)):
            new_list.append(x)
    if len(new_list) != 0:
        return {
            "total": total_list,
            "Prime": new_list
        }
    else:
        return "No Prime Number"
    
def get_count_of_permutations(total, r=2) :
    result = map(join_tuple_string, list(permutations(total,r)))
    return list(result)

def check_prime_or_not(num):
    flag = False
    if num == 1:
        return False
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        # check if flag is True
        if flag:
            return False
        else:
            return True


# function that converts tuple to string
def join_tuple_string(strings_tuple) -> str:
    return int(''.join(strings_tuple))


def check_word_is_keyword(fname):
    words = [];
    with open(fname,'r') as f:
        for line in f:
            for word in line.split():
                if(keyword.iskeyword(word)):
                    words.append(word)
    return words

def check_word_is_keyword_count(fname):
    words = check_word_is_keyword(fname)
    wfreq=[words.count(w) for w in words]
    return dict(zip(words,wfreq))
                
                


def file_counter(fname):
    num_words = 0
    num_lines = 0
    num_charc = 0
    num_spaces = 0
    with open(fname, 'r') as f:
        for line in f:
            num_lines += 1
            word = 'Y'
            for letter in line:
                if (letter != ' ' and word == 'Y'):
                    num_words += 1
                    word = 'N'
                elif (letter == ' '):
                    num_spaces += 1
                    word = 'Y'
                for i in letter:
                    if(i !=" " and i !="\n"):
                        num_charc += 1
                         
    print("Number of words in text file: ",
          num_words)
     
    print("Number of lines in text file: ",
          num_lines)
     
    print('Number of characters in text file: ',
          num_charc)
     
    print('Number of spaces in text file: ',
          num_spaces)


def get_list(num):
    total = []
    for i in range(1,num):
        new_list = random.choices(list(range(1, 15)),k=10)
        total.append(new_list)
    return avg_count(total,num)

def selectionSort_count( itemsList ):
    cnt = 0;
    n = len( itemsList )
    for i in range( n - 1 ): 
        minValueIndex = i

        for j in range( i + 1, n ):
            if itemsList[j] < itemsList[minValueIndex] :
                minValueIndex = j

        if minValueIndex != i :
            temp = itemsList[i]
            itemsList[i] = itemsList[minValueIndex]
            itemsList[minValueIndex] = temp
            cnt = cnt + 1;

    return cnt

def avg_count(data,num):
    status = {}
    add = 0;
    for i in data:
        add = add + selectionSort_count(i)
    status["total swape"] = add
    status["average of swape"] = (add/num)
    return status;
        