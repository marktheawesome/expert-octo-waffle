package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func main() {
	file, err := os.Open("./input.txt")
	if err != nil {
		fmt.Println("Fuck:", err)
		return
	}
	defer file.Close()

	textNumbers := map[string]int{
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}
	scanner := bufio.NewScanner(file)
	total := 0
	for scanner.Scan() {
		line := scanner.Text()
		var number [100]int
		for key := range textNumbers {
			index := strings.Index(line, key)
			lastindex := strings.LastIndex(line, key)
			if index != -1 {
				number[index] = int(textNumbers[key])
			}
			if lastindex != -1 {
				number[lastindex] = int(textNumbers[key])
			}

		}
		for i := 0; i < len(line); i++ {
			var char rune = rune(uint8(line[i]))
			if unicode.IsDigit(char) {
				number[i], _ = strconv.Atoi(string(char))
			}
		}
		a := 0
		b := 0
		for i := range number {
			if number[i] != 0 {
				a = (int(number[i]) * 10)
				break
			}
		}
		for i := len(number) - 1; i >= 0; i-- {
			if number[i] != 0 {
				b = number[i]
				break
			}
		}
		total += a + b

	}
	fmt.Println(total)
}
