fun main()
{
	println("Sufyan Ansari 5008")
	println("Enter The Two Number")
	var n1 = Integer.parseInt(readLine())
	var n2 = Integer.parseInt(readLine())

	println("value before swapping ")
	println("n1=$n1 & n2=$n2")	

	//var swap = n1
	//n1 = n2
	//n2 = swap
	
	n1 = n1 + n2
	n2 = n1 - n2
	n1 = n1 - n2

	println("value after swapping ")
	println("n1=$n1 & n2=$n2")
	println("Sufyan Ansari 5008")
}
