def main():
    with open('input.txt') as f:
        elvs_calories = []

        elv_calories = 0

        for line in f:
            try:
                num = int(line)
                elv_calories += num
            except ValueError:
                elvs_calories.append(elv_calories)
                elv_calories = 0

        elvs_calories.sort(reverse=True)
        max_three_sum = sum(elvs_calories[:3])
        print(max_three_sum)


if __name__ == '__main__':
    main()
