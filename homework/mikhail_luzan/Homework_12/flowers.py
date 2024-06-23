class Flowers:
    def __init__(self, kind, form, colour, stem_length, freshness, life_time, cost):
        self.kind = kind
        self.form = form
        self.colour = colour
        self.stem_length = stem_length
        self.freshness = freshness
        self.life_time = life_time
        self.cost = cost

    def __str__(self):
        return (
            f'{self.kind}, {self.form}, {self.colour}, {self.stem_length}, {self.freshness}, {self.life_time},'
            f' {self.cost}'
        )


class Roses(Flowers):
    def __init__(self, form, colour, stem_length, freshness, life_time, cost):
        super().__init__('Rose', form, colour, stem_length, freshness, life_time, cost)


class Lilies(Flowers):
    def __init__(self, form, colour, stem_length, freshness, life_time, cost):
        super().__init__('Lily', form, colour, stem_length, freshness, life_time, cost)


class Gypsophilas(Flowers):
    def __init__(self, form, colour, stem_length, freshness, life_time, cost):
        super().__init__('Gypsophila', form, colour, stem_length, freshness, life_time, cost)


class Bouquet:
    def __init__(self):
        self.flowers = []
        self.cost = 0

    def add_flower(self, flower):
        self.flowers.append(flower)
        self.cost += flower.cost

    def avg_life_time(self):
        if not self.flowers:
            return 0
        avg_time = sum(flower.life_time for flower in self.flowers) / len(self.flowers)
        return avg_time

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: flower.freshness)

    def sort_by_colour(self):
        self.flowers.sort(key=lambda flower: flower.colour)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length)

    def sort_by_cost(self):
        self.flowers.sort(key=lambda flower: flower.cost)

    def search_by_min_life_time(self, min_life_time):
        results = list(filter(lambda flower: flower.life_time >= min_life_time, self.flowers))
        return "\n".join(str(flower) for flower in results)

    def __str__(self):
        return "\n".join(str(flower) for flower in self.flowers)


rose_1 = Roses('Sentimental', 'red & white', 0.5, 95, 3, 6)
rose_2 = Roses('Sun Sprinkles', 'yellow', 0.5, 50, 4, 7)

lily_1 = Lilies('Night Rider Lily', 'red', 0.7, 80, 2, 10)
lily_2 = Lilies('Heartstrings', 'red & yellow', 0.7, 45, 3, 5)

gypsophila_1 = Gypsophilas('My Pink', 'pink', 0.4, 100, 8, 2)
gypsophila_2 = Gypsophilas('Million Stars', 'white', 0.4, 90, 7, 3)

bouquet = Bouquet()
bouquet.add_flower(rose_1)
bouquet.add_flower(rose_2)
bouquet.add_flower(lily_1)
bouquet.add_flower(gypsophila_2)

print(f'\nBouquet contains:\n{bouquet}')
print('\nPrice: ', bouquet.cost)
print('\nAverage Life Time: ', bouquet.avg_life_time())

bouquet.sort_by_freshness()
print("\nBouquet sorted by freshness:")
print(bouquet)

bouquet.sort_by_colour()
print("\nBouquet sorted by colour:")
print(bouquet)

bouquet.sort_by_stem_length()
print("\nBouquet sorted by stem length:")
print(bouquet)

bouquet.sort_by_cost()
print("\nBouquet sorted by cost:")
print(bouquet)

search_results = bouquet.search_by_min_life_time(7)
print("\nSearch results by MIN life time:")
print(search_results)
