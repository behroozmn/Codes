#!/bin/bash
#نکته:اگر یک آرایه سه عضو داشته باشد و مستقیما عضو هشتم را مقدار دهی نماییم آنگه عضو مابین تهی خواهد بود و عضو هشت همچنان هشتم باقی خواهد ماند  یعنی اگر بگوییم همه را نمایش بده پشت سر هم نمایش در می‌آید ولی عضو تهی نمایش نمی‌شود
myArray=""
newArray=""
# Declare : declare an array
declareArray() {
    myArray=('constant' "${variable}" 'another constant')
}

#Push new Item to the end of arrayadd
appendToEnd() {
    myArray+=('newItem') 
}

#access all array element
getAll() {
    echo "${myArray[@]}"
}

#For: iterate array elements
getAllByFor() {
    for item in "${myArray[@]}"; do
        echo "${item}"
    done
}

#GetIndex: retrieve element from array at specified index (zero based)
getOneByIndex() {
    echo "${myArray[index]}" # مثلا ایندکس شماره ۳ یعنی عضو چهارم
}

#Get Index: n elements of an array from specified index (zero based)
getSomeFromZeroUntilIndex() {
    newArray="${myArray[*]:fromIndex:n}"
}

#filter elements of an array based on given grep pattern
checkExistElementByPattern() {
    readarray -t Var_filteredData < <(for i in "\({myArray[@]}"; do echo "\){i}"; done | grep 'pattern')
}

#Contains: check if the array contains an element
checkExistElement() {
    if [[ "${myArray[*]}" =~ 'element' ]]; then
        echo 'array contains element'
    fi
}

#Concat: concatenate two arrays
ConcatTwoArrays() {
    newArray=("\({array1[@]}" "\){array2[@]}")
}

#Delete: delete entire array
delete() {
    unset myArray
}

#Delete: delete element at index from array
deleteIndex() {
    unset "myArray[index]"
}

#Index: set array element at specified index
setonIndex() {
    myArray[index]="value"
}

#FindOrReplace: find and replace elements in array using regex
findAndReplace() {
    newArray=${myArray[*]//find/replace}
}

#Length: length of an array
lenght() {
    length=${#myArray[@]}
}

#Reverse: reverse order of array elements
reverse() {
    for ((i = ${#myArray[@]} - 1; i >= 0; i--)); do
        reversed+=("${myArray[i]}")
    done
    unset "myArray" # optional
    echo "${reversed[@]}"
}

echo "${myArray[@]:2:4}" # نمایش عضو دوم تا چهارم
echo "${myArray[@]:1}" # نمایش عضو اول تا آخر