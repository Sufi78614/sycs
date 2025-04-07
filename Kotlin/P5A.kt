fun factorial(num:Int):Int
{
	var f = 1
	for(i in 1..num)
	{
		f = f * i
	}
	return f
}
fun main()
{

	println("Mohammad Husain 5042")
	println("========================")
	println("Enter The Number :")
	var n = Integer.parseInt(readLine())
	var ans = factorial(n)
	println("Factorial of $n is $ans")
	println("Mohammad Husain 5042")

}