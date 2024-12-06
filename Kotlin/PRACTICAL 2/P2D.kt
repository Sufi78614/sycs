fun main() 
{	
	println("Sufyan Ansari 5008")
	println("Enter a Year:")
	val year = Integer.parseInt(readLine())

    	if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) 
	{
        	println("$year is a Leap Year")
    	} 
	else 
	{
        	println("$year is not a Leap Year")
    	}
	println("Sufyan Ansari 5008")
}
