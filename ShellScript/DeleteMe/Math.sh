
# add two variables
result=$((int1 + int2))

# increment integer variable by 1
((int++)) #→  such as ((x++))
((++int))
((x+=5))  #→  افزودن عدد ۵ به عدد
# add int1 and int2 and assign the result to int1
((int1 += int2))

# exponentiate base to power
result=$((base ** power)) [or] echo $RANDOM



# EXPR
result=\((expr \){int1} + ${int2})
result=expr 1 + 1 #result: 2