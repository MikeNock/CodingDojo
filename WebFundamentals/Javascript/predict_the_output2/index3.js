function highFive(num){
        for(var i=0; i<num; i++){
            if(i == 5){
                console.log("High Five!");
            }
            else{
                console.log(i);
            }
        }
    }

// Prediction: 
// 1,2,3,4,High Five!
// However this only occurs if the function is called. Since the function is not called, nor given a numerical value, nothing is returned.