fun main() 
{
	println("Sufyan Ansari 5008")
    	println("Enter a character:")
    	val char = readLine()?.lowercase()?.get(0)
    
    	if (char in listOf('a', 'e', 'i', 'o', 'u'))
 	{
        	println("$char is a Vowel")
    	}
	else 
	{
        	println("$char is not a Vowel")
    	}
	println("Sufyan Ansari 5008")
}
