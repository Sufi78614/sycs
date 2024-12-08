fun main()
{
	println("Sufyan Ansari 5008")
	println("Enter the TWO Integer Numbers: ")

	var num1 = Integer.parseInt(readLine())
	var num2 = Integer.parseInt(readLine())

	var a = num1 + num2
	var b = num1 - num2
	var c = num1 * num2
	var d = num1 / num2
	var e = num1 % num2

	println("The Number1 is:$num1")
	println("The Number2 is:$num2")
	println("The Addition is: $a")
	println("The Subtraction is: $b")
	println("The Multiplication is: $c")
	println("The Division is: $d")
	println("The Modulus is: $e")
}