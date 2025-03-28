def sort_data(filename):
    countries = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            name, area, population = line.strip().split(',')
            area = float(area)
            population = int(population)
            countries.append([name, area, population])

    sorted_by_area = sorted(countries, key=lambda x: x[1], reverse=True)
    sorted_by_population = sorted(countries, key=lambda x: x[2], reverse=True)
    
    return sorted_by_area, sorted_by_population
    
def print_results(sorted_by_area, sorted_by_population):
    if sorted_by_area is None or sorted_by_population is None:
        return
    
    print("\nВідсортовано за площею (від більшої до меншої):")
    print("   Назва країни | Площа       | Населення")
    print("-" * 50)
    for country in sorted_by_area:
        print(f"{country[0]:<15} | {country[1]:>10.2f} | {country[2]:>12,}")
    
    print("\nВідсортовано за населенням (від більшого до меншого):")
    print("   Назва країни | Площа      | Населення")
    print("-" * 50)
    for country in sorted_by_population:
        print(f"{country[0]:<15} | {country[1]:>10.2f} | {country[2]:>12,}")

if __name__ == "__main__":
    filename = "mkr1.txt"
    sorted_by_area, sorted_by_population = sort_data(filename)
    print_results(sorted_by_area, sorted_by_population)