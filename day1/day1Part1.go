package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"unicode"
)

func main() {
	file, err := os.Open("./input.txt")
	if err != nil {
		fmt.Println("Fuck: ", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	total := 0
	for scanner.Scan() {
		line := scanner.Text()
		nums := []string{}
		for i := 0; i < len(line); i++ {
			var char rune = rune(uint8(line[i]))
			if unicode.IsDigit(char) {
				nums = append(nums, string(char))
			}
		}
		number := nums[0] + nums[len(nums)-1]
		intnum, _ := strconv.Atoi(number)

		total += intnum
	}
	fmt.Println(total)
}
