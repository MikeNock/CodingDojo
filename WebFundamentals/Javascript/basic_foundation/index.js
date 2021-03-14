// Number 1
console.log('Number 1 - Get 1 to 255')
function evens(){
    var evens = [];
    for(i=1;i<256;i++){
        evens.push(i);
    }
    return evens;
}
console.log(evens());


// Number 2
console.log('Number 2 - Add evens up to 1000')
function addEvens(){
    var sum = 0;
    for(var i=1;i<=1000;i++){
        if(i%2==0){
            sum = sum +i;
        }
    }
    return sum;
}
console.log(addEvens());

// Number 3
console.log('Number 3 - Sum up odd numbers to 5000')
function addOdds(){
    var Sum=0;
    for(var i=0; i<=5000; i++){
        if(i%2==1){
            Sum = Sum + i
            console.log('Num:', i + ', Sum: ', Sum + ",")
        }
    }
    return Sum;
}
console.log(addOdds());

// Number 4
console.log('Number 4 - Iterate a array')
function sumArray(arr){
    var sum = 0;
    for(var i=0; i<arr.length;i++){
        sum =sum + arr[i];
    }
    return sum;
}
console.log(sumArray([1,2,3]))

// Number 5
console.log('Number 5 - Find Max')
function max(arr){
    var max_num = arr[0]
    for(var i=0;i<arr.length;i++){
        if(arr[i]>max_num){
            max_num=arr[i];
        }
    }
    return max_num;
}
console.log(max([1,2,3]));

// Number 6
console.log('Number 6 - Find Average')
function avg(arr){
    var sum = 0;
    var average = 0;
    for(var i=0;i<arr.length;i++){
        sum = sum + arr[i];
    }
    average = sum / arr.length;
    return average;
}
console.log(avg([1,2,3]))

// Number 7
console.log('Number 7 - Array Odd')
function oddNums(){
    var odds = []
    for(var i=0;i<50;i++){
        if(i%2==1){
            odds.push(i);
        }
    }
    return odds;
}
console.log(oddNums())

// Number 8
console.log('Number 8 - Greater than Y')
function greater_than(arr){
    var Y = 5;
    var top = [];
    for(var i=0;i<arr.length;i++){
        if(arr[i]>Y){
            top.push(arr[i]);
        }
    }
    return top;
}
console.log(greater_than([1,2,3,4,5,6,7,8,9,10]))

// Number 9
console.log('Number 9 - Squares')
function squares(arr){
    var squared = [];
    var tmp = 0
    for(var i=0;i<arr.length;i++){
        tmp = arr[i] * arr[i];
        squared.push(tmp)
    }
    return squared;
}
console.log(squares([1,2,3,4,5]))

// Number 10
console.log('Number 10 - Negatives')
function neg_neg(arr){
    var newArr = [];
    for(var i=0;i<arr.length;i++){
        if(arr[i]<0){
            arr[i]=0;
            newArr.push(arr[i]);
        }
        else{
            newArr.push(arr[i])
        }
    }
    return newArr;
}
console.log(neg_neg([-1,-2,3,4]))

// Number 11
console.log('Number 11 - Max/Min/Avg')
function max_min_avg(arr){
    var max = arr[0];
    var min = arr[0];
    var sum = 0;
    var avg = 0;
    var newArr = [];
    for(var i=0;i<arr.length;i++){
        sum = sum + arr[i];
        if(arr[i]>max){
            max = arr[i];
        }
        else if(arr[i]<min){
            min = arr[i];
        }
    }
    avg = sum / arr.length;
    newArr.push(max);
    newArr.push(min);
    newArr.push(avg);
    return newArr;
}
console.log(max_min_avg([1,2,3,4,5,6,7,8,9,10]))

// Number 12
console.log('Number 12 - Swap Values')
function swap(arr){
    var tmp = arr[arr.length-1];
    arr[arr.length-1] = arr[0];
    arr[0] = tmp;
    return arr;
}
console.log(swap([1,2,3,4,5]));

// Number 13
console.log('Number 13 - Number to String')
function dojo_neg(arr){
    var newArr = [];
    for(var i=0;i<arr.length;i++){
        if(arr[i]<0){
            arr[i]='Dojo';
            newArr.push(arr[i]);
        }
        else{
            newArr.push(arr[i])
        }
    }
    return newArr;
}
console.log(dojo_neg([-1,-2,3,4]))