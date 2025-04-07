fun Reverse(n:Int):Int
{
	var a = n
	var rev = 0
	while(a > 0)
	{
		var r = a % 10
		rev = rev * 10 + r
		a = a / 10
	}
	return rev
}

fun main()
{
	println("Mohammad Husain 5042")
	println("================================")
	
	println("Enter the number:")
	var n = Integer.parseInt(readLine())

	var ans = Reverse(n)
	println("The Reversed Number is : $ans")
	println("Mohammad Husain 5042")
}