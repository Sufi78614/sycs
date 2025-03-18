<?php
function factorial($n){
  if($n==0||$n==1){
    return 1;
  }else{
    return $n*factorial($n-1);
  }
}
$number = 5
$factorialResult = factorial($number);
echo"factorial of $number is : $factorialResult\n";
?>
