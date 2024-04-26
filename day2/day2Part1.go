package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, err := os.ReadFile("./test.txt")
	if err != nil {
		fmt.Println("Fuck: ", err)
		return
	}
	defer file.Close()
	maxColors := map[string]int{
		"red":   12,
		"green": 13,
		"blue":  14,
	}
	scanner := bufio.NewScanner(file)
	total := 0
	for scanner.Scan() {
		line := scanner.Text()
	}

	fmt.Println("Hello World.")
}
