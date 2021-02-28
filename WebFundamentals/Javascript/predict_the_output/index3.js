var arr = [1,3,8,-5,0,-2,4,-1];
var newArr = [];
for(var i = 0; i< arr.length; i++){
    if(arr[i] < 0){
        newArr.push(arr[i]);
        arr[i] = arr[i] * -1;
    }
    else if(arr[i] == 0){
        arr[i] = "Zero";
    }
    else{
        arr[i] = arr[i] * -1;
    }
}
console.log(arr);
console.log(newArr);

// Prediction: (8), [-1, -3, -8, 5, 'Zero', 2, -4, 1]
// You're essentially creating a function that flips the +/- values from arr, and moves them to newArr :: unless that value is 0 in which case it prints the string 'Zero' in newArr
// The only caveat is 8, because it longer than the array length, so the for loop doesn't apply and it remains in arr.
// What I don't understand is why arr and newArr swapped values the way they did.