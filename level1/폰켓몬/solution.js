function solution(nums) {
  var answer;
  var canGetMonNum = Math.floor(nums.length / 2);
  var setNums = new Set(nums);
  var setNumsSize = setNums.size;
  if (setNumsSize >= canGetMonNum) {
    answer = canGetMonNum;
  } else {
    answer = setNumsSize;
  }
  return answer;
}
