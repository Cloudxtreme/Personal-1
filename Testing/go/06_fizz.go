package main

import "fmt"

func main() {

for i := 0; i <= 100; i++{
  if i % 15 ==0 {
    fmt.Println(i, " -- FizzBuzz")
    } else if i%3 == 0 {
      fmt.Println(i, " -- fizz")
    } else if i%5 ==0 {
      fmt.Println(i, " -- buzz")
    } else {
      fmt. Println(i)
    }


  }
}
