fun checkEvenOdd(num: Int) {
    if (num % 2 == 0) {
        println("$num is even")
    } else {
        println("$num is odd")
    }
}
// Main function
fun main() {
    println("Mohammad Husain 5042")
    println("Enter a number: ")
    println("=====================")
    val input = readLine() 
    if (input != null) {
        val num = input.toIntOrNull() 
        if (num != null) {
            checkEvenOdd(num)
        } else {
            println("Please enter a valid integer.")
        }
	println("Mohammad Husain 5042")
    }
}
