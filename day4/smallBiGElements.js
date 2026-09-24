function findSmallBigNumbers(array) {
    smallNumber = bigNumber = array[0]
    for(let i = 0; i < array.length; i++) {
        if (array[i] < smallNumber)
            smallNumber = array[i]
        if(array[i] > bigNumber)
            bigNumber = array[i]
    }
    console.log(i) // Error
    return [smallNumber, bigNumber]
}

numbers = [23, 2, 19, 29, 5, 17, 11, 13, 7, 3]
console.log(`User given numbers are ${numbers}`)
smallBig = findSmallBigNumbers(numbers)
console.log('Small Number is ', smallBig[0], ' Big Number = ', smallBig[1])
alert(`SmallNumber = ${smallBig[0]}, BigNumber=${smallBig[1]}`)
