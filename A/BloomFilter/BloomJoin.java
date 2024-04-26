import java.util.ArrayList;
import java.util.BitSet;
import java.util.List;

public class BloomJoin {

    // Bloom filter size
    private static final int FILTER_SIZE = 10;

    public static void main(String[] args) {
        // Sample relations (tables)
        List<String> relation1 = new ArrayList<>();
        List<String> relation2 = new ArrayList<>();

        // Fill relations with sample data
        // Format: "id, name"
        relation1.add("201, Manali");
        relation1.add("202, Goa");
        relation1.add("203, Rajastan");
        relation1.add("204, Assam");
        relation1.add("205, Indore");

        // Format: "id, branch"
        relation2.add("201, Hill Station");
        relation2.add("202, Beaches");
        relation2.add("204, Deserts");
        relation2.add("206, Hills Mountains");
        relation2.add("207, Street Food");

        // Perform Bloom join
        List<String> result = bloomJoin(relation1, relation2);

        // Print result
        for (String row : result) {
            System.out.println(row);
        }
    }

    public static List<String> bloomJoin(List<String> relation1, List<String> relation2) {
        // Create Bloom filter for relation 2
        BloomFilter bloomFilter = new BloomFilter(FILTER_SIZE);
        for (String row : relation2) {
            String[] parts = row.split(",");
            String key = parts[0];
            bloomFilter.add(key);
        }

        // Perform join
        List<String> result = new ArrayList<>();
        for (String row : relation1) {
            String[] parts = row.split(",");
            String key = parts[0];
            if (bloomFilter.contains(key)) {
                result.add(row);
            }
        }

        return result;
    }

    static class BloomFilter {
        private final BitSet bitSet;
        private final int filterSize;

        public BloomFilter(int filterSize) {
            this.filterSize = filterSize;
            this.bitSet = new BitSet(filterSize);
        }

        public void add(String key) {
            int hash1 = hashFunction1(key);
            int hash2 = hashFunction2(key);
            int hash3 = hashFunction3(key);
            bitSet.set(hash1);
            bitSet.set(hash2);
            bitSet.set(hash3);
        }

        public boolean contains(String key) {
            int hash1 = hashFunction1(key);
            int hash2 = hashFunction2(key);
            int hash3 = hashFunction3(key);
            return bitSet.get(hash1) && bitSet.get(hash2) && bitSet.get(hash3);
        }

        private int hashFunction1(String key) {
            int hash = 0;
            for (int i = 0; i < key.length(); i++) {
                hash = (hash * 31) + key.charAt(i);
            }
            return Math.abs(hash) % filterSize;
        }

        private int hashFunction2(String key) {
            int hash = 0;
            for (int i = 0; i < key.length(); i++) {
                hash = (hash * 37) + key.charAt(i);
            }
            return Math.abs(hash) % filterSize;
        }

        private int hashFunction3(String key) {
            int hash = 0;
            for (int i = 0; i < key.length(); i++) {
                hash = (hash * 41) + key.charAt(i);
            }
            return Math.abs(hash) % filterSize;
        }
    }
}
