<?php
function factorial($n) {
  if ($n == 0 || $n == 1) {
    return 1;
  } else {
    return $n * factorial($n - 1);
  }
}

$number = 5; // Added missing semicolon
$factorialResult = factorial($number);
echo "Factorial of $number is: $factorialResult\n";
?>
