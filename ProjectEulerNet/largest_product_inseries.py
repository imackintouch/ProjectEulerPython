import sys
#
# Find the sequence of seq_length digits in a string of numerical characters that has the largest product
# of such a sequence. The default sequence length is 13.
#
#
#See web URL: https://projecteuler.net/problem=8 for a fuller description
#
#
series='73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'

#
# default main input of 13 if no arguments
#
if len(sys.argv)<2:
    seq_length=13
else:
    print(sys.argv[1])
    seq_length=int(sys.argv[1])

#
# Scan through the series sequence of numeric characters
#
count=0
max_product = 0
sequence_count = 0
for n in (series):
    #
    # For each character in our series, we gather up the next 12 characters.
    # Otherwise we keep working out the product assuming that we don't have enough
    # left to have a full sequence of 13 digits. Note: The range function requires the
    # endpoint to be 1 more than what we need hence count+13 instead of count+12
    #
    sequence_product = 1
    if (len(series)>=count+seq_length):
        for p in range(count, count+seq_length):
            #if p!=count:
            #   print("*",end="")
            print(series[p],end="")
            if (p != (count + seq_length-1)):
                print ("*",end="")
            sequence_product = sequence_product * int(series[p])

    else:
        continue
    #
    # Keep track of the the maximum product so far.
    #
    print()

    if sequence_product > max_product:
        max_product=sequence_product
        max_sequence_id=sequence_count

    sequence_count = sequence_count + 1
    print("sequence_product is:%d Sequence count is:%d\n" % (sequence_product, sequence_count))
    #
    # Move forward one character to calaculate a new
    # 13 digit sequence product.
    #
    count = count + 1

print("Total number of characters read to calculate product is:",count)
print("Max product is:%d found at sequence:%d" % (max_product, max_sequence_id))