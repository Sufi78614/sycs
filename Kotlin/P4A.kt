fun main()
{
	println("Mohammad Husain 5042")
	println("===================")
	println("Enter the number :")
	var num = Integer.parseInt(readLine())

	var sum = 0
	var rev = 0

 	while(num > 0)
	{
		var r = num % 10
		sum = sum + r
		rev = rev * 10 + r
		num = num / 10
	}

	println("sum of digits is : $sum")
	println("Reverse of number is : $rev")
	println("Mohammad Husain 5042")
}