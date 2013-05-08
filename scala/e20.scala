//package euler

case class Docstring(s: String) extends scala.annotation.Annotation

def factorial(n: Int): BigInt = {
  Docstring("""
  Consumes an integer n and returns the n!, i.e. n factorial, 
  
  usage:
  scala> factorial(20)
  BigInt = 2432902008176640000
  """)
  if (n == 0) 1 else n * factorial(n-1)
}

implicit def int2factorial(n: Int) = {
  Docstring("""
  Creates a macro for the factorial function enabling it
  to be called as: n!

  usage:
  scala> 20!
  BigInt = 2432902008176640000
  """)
  class FactorialMacro(n: Int) { def ! =  factorial(n) }
  new FactorialMacro(n)
}

def sum(args: Int*) = {
  Docstring("""Sums an arbitrary number of integer argument""")
  var accum = 0
  for (arg <- args.elements) accum += arg
  accum
}

def digify(num: BigInt) = {
  Docstring("""Expands/splits an integer into a List[Int] of digits""")
  if (num == 0) List(0) else 
    (Stream.iterate(num)(_/10)takeWhile(_!=0)map(_%10)toList) reverse
}

object E20 {
  def main(args: Array[String]) {
    println(digify(100!) map { _.toString } map { Integer.parseInt } sum)
  } 
}

E20.main(args)
