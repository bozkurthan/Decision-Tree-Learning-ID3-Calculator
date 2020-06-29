import math

total_entropy=1
total_instance=4

first_positive_examples = 3
first_negative_examples = 1

f1 = -(first_positive_examples / (first_positive_examples + first_negative_examples))
try:
    f2 = math.log2((first_positive_examples / (first_positive_examples + first_negative_examples)))
except:
    f2 = 0
f3 = (first_negative_examples / (first_positive_examples + first_negative_examples))
try:
    f4 = math.log2((first_negative_examples / (first_positive_examples + first_negative_examples)))
except:
    f4 = 0
first_entropy_result= f1* f2 - f3 * f4

second_positive_examples = 6
second_negative_examples = 1

s1 = -(second_positive_examples / (second_positive_examples + second_negative_examples))
try:
    s2 = math.log2((second_positive_examples / (second_positive_examples + second_negative_examples)))
except:
    s2 = 0
s3 = (second_negative_examples / (second_positive_examples + second_negative_examples))
try:
    s4 = math.log2((second_negative_examples / (second_positive_examples + second_negative_examples)))
except:
    s4 = 0

second_entropy_result= s1 * s2 - s3 * s4

third_positive_examples = 0
third_negative_examples = 0

if(third_positive_examples!=0 and third_negative_examples!=0):
    t1 = -(third_positive_examples / (third_positive_examples + third_negative_examples))
    try:
        t2 = math.log2((third_positive_examples / (third_positive_examples + third_negative_examples)))
    except:
        t2 = 0
    t3 = (third_negative_examples / (third_positive_examples + third_negative_examples))
    try:
        t4 = math.log2((third_negative_examples / (third_positive_examples + third_negative_examples)))
    except:
        t4 = 0
    third_entropy_result=  t1*t2  - t3 * t4
else:
    third_entropy_result=0


if(third_entropy_result == 0):
    info_gain= total_entropy - (((first_positive_examples+first_negative_examples) / total_instance)*first_entropy_result) - (((second_positive_examples+second_negative_examples) / total_instance)*second_entropy_result)
else:
    info_gain= total_entropy - (((first_positive_examples+first_negative_examples) / total_instance)*first_entropy_result) - (((second_positive_examples+second_negative_examples) / total_instance)*second_entropy_result) - (((third_positive_examples+third_negative_examples) / total_instance)*third_entropy_result)


print("first_given_entropy:",first_entropy_result)
print("second_given_entropy:",second_entropy_result)
print("third_given_entropy:",third_entropy_result)
print("given_info_gain:",info_gain)
