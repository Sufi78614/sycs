fun main() 
{	
	println("Keriwala Abdullah 5021")
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
	println("Keriwala Abdullah 5021")
}
