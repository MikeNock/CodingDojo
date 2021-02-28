var arr = [7,3,8,4,2,0,1];
for(var i = 0; i < arr.length; i++){ 
    if(arr[i] % 2 == 0){
        console.log(arr[i]);
    } 
    else{
        console.log("That is odd!");
    }
}

//  Prediction: That is odd!, That is odd!, 8, 4, 2, 0, That is odd!
// It loops through each number in each array position, takes a remainder based on it's divisibility of 2, and if the remainder == 0 prints the number in that array position, if not prints That is odd!
// Interesting that the debugger console in VSCode displays a 2 in a bubble to show that an item printed twice. Good info to know.

