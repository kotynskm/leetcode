var twoSum = function(nums, target) {
    for(let i = 0; i < nums.length; i++){
      // second loop for num at j
      for(let j = i + 1; j < nums.length; j++){
        // add num at i and num at j and check if it is the target num, if it is return i,j
        if(nums[i] + nums[j] === target){
          return [i,j];
        }
      }
    }
  }