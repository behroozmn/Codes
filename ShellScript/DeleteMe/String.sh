#if strings are not equal
if [[ "${string1}" != "${string2}" ]]; then
    echo "The two strings are different"
fi

#remove leading and trailing white space
trimmed=$(echo -e "${string}" |  sed -e 's/^[[:space:]]*//' | sed -e 's/[[:space:]]*$//')

#remove all white space(s)
trimmed=$(echo -e "${string}" | tr -d '[:space:]')

#[Trim left]remove leading white space(s)
trimmed=$(echo -e "${string}" | sed -e 's/^[[:space:]]*//')

#[Trim Right]remove trailing white space(s)
trimmed=$(echo -e "${string}" | sed -e 's/[[:space:]]*$//')

#reverse string characters
reversed=$(echo -e "${string}" | rev)

#random string from provided characters with desired length (default: 8)
randomString=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 8 ; echo '')

#check whether string contains substring
if [[ "${string}" == *"${substring}"* ]]; then
    echo "${string} contains: ${substring}"
fi

#concatenate two strings(string+string)
string="${string1}${string2}"

#get length of a variable that is a string
behrooz=123456
echo "${#behrooz}" output:6

# Example
${variable-name-here:index-of-character:number-of-characters-from-index-onwards-to-return}

#Example
MyString="behroozMohammadiNasabSahzabi"
echo "${MyString:0:5}"   #[output] → behro
echo "${MyString:20:6}"  #[output] → bSahza
echo "${MyString:0:5}"   #[output] → behro

# Not Empty
if [[ -n "${string}" ]]; then
    echo "string is not empty"
fi

# is Empty
if [[ -z "${string}" ]]; then
    echo "empty string"
fi

# Contain SubString
if [[ "\({string}" == *"\){substring}"* ]]; then
    echo "\({string} contains: \){substring}"
fi
