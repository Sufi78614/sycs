fun main() {
    println("Mohammed Rafe 5089")
    println("===================")
    println("Enter a number:")
    val num = readLine()
    if (num != null) {
        if (num == num.reversed()) {
            println("$num is a palindrome.")
        } else {
            println("$num is not a palindrome.")
        }
    } else {
        println("Invalid input!")
    }
    println("Mohammed Rafe 5089")
}
