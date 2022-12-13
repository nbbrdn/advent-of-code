package main

import (
	_ "embed"
	"flag"
	"fmt"
	"strconv"
	"strings"
)

//go:embed input.txt
var input string

func main() {
	var part int
	flag.IntVar(&part, "part", 1, "part 1 or 2")
	flag.Parse()
	fmt.Println("Running part", part)

	if part == 1 {
		ans := part1(input)
		fmt.Println("Output:", ans)
	} else {
		ans := part2(input)
		fmt.Println("Output:", ans)
	}

}

func part1(input string) int {
	if len(input) == 0 {
		panic("empty input.txt file")
	}
	elves := strings.Split(input, "\n\n")
	max := 0
	for _, elf := range elves {
		foods := strings.Split(elf, "\n")
		total := 0
		for _, weightStr := range foods {
			weight, err := strconv.Atoi(weightStr)
			if err != nil {
				continue
			}
			total += weight
		}
		if total > max {
			max = total
		}
	}
	return max
}

func part2(input string) int {
	return 0
}
