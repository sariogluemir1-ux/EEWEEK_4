found_part5 = False
for alyssa in range(1001):
    ben = alyssa - 20
    cindy = alyssa * 2
    if alyssa + ben + cindy == 1000:
        print(f"Tickets sold by Alyssa: {alyssa}")
        found_part5 = True
        break
