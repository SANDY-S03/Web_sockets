class BloomJoin:
    FILTER_SIZE = 10

    def main(self):
        # Sample relations (tables)
        relation1 = [
            "201, Manali",
            "202, Goa",
            "203, Rajastan",
            "204, Assam",
            "205, Indore"
        ]

        relation2 = [
            "201, Hill Station",
            "202, Beaches",
            "204, Deserts",
            "206, Hills Mountains",
            "207, Street Food"
        ]

        # Perform Bloom join
        result = self.bloom_join(relation1, relation2)

        # Print result
        for row in result:
            print(row)

    def bloom_join(self, relation1, relation2):
        # Create Bloom filter for relation 2
        bloom_filter = BloomFilter(self.FILTER_SIZE)
        for row in relation2:
            parts = row.split(",")
            key = parts[0]
            bloom_filter.add(key)

        # Perform join
        result = []
        for row in relation1:
            parts = row.split(",")
            key = parts[0]
            if bloom_filter.contains(key):
                result.append(row)

        return result


class BloomFilter:
    def __init__(self, filter_size):
        self.filter_size = filter_size
        self.bitset = [False] * filter_size

    def add(self, key):
        hash_values = self.get_hash_values(key)
        for hash_value in hash_values:
            self.bitset[hash_value] = True

    def contains(self, key):
        hash_values = self.get_hash_values(key)
        return all(self.bitset[hash_value] for hash_value in hash_values)

    def get_hash_values(self, key):
        hash_values = []
        hash_functions = [self.hash_function1, self.hash_function2, self.hash_function3]
        for hash_function in hash_functions:
            hash_values.append(hash_function(key))
        return hash_values

    def hash_function1(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31) + ord(char)
        return abs(hash_value) % self.filter_size

    def hash_function2(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 37) + ord(char)
        return abs(hash_value) % self.filter_size

    def hash_function3(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 41) + ord(char)
        return abs(hash_value) % self.filter_size


if __name__ == "__main__":
    bloom_join = BloomJoin()
    bloom_join.main()
