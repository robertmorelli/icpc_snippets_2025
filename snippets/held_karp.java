import java.util.Scanner;
//https://stackoverflow.com/questions/2229651/what-is-the-most-effective-way-to-erase-individual-bits-in-a-bitset-is-it-xor-o
//https://stackoverflow.com/questions/7790233/how-to-clear-the-most-significant-bit
public class Tsp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(), S, tmp, i, j, k, b, s_no_k_n, cur, best, full, s, m, u, v;
        short x;
        short[] G = new short[(1 << n) * n];//dp table for held-karp. needs to be n*2^n
        short[] dist = new short[n * n];//adjacency matrix
        int[] k_scratch = new int[n];//used to encourage vectorization in the tight loop
        final short INF_EDGE = (short)(Short.MAX_VALUE / n);//the sum of n edges should not overflow a short
        final short INF_WEIGHT = Short.MAX_VALUE;//nothing is added to this so we just use straight max
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                x = scanner.nextShort();
                if (i == j) dist[n * j + i] = INF_EDGE;// self edges are NEVER valid in an h-cycle. this is to avoid special cases in the tight loop
                else dist[n * j + i] = x;
            }
        }
        //base case for dp. in this case its every shortest path ending in element 0 of length 1 which
        //by definition is direct edges (in a complete graph)
        for (k = 1; k < n; k++) G[(1 << k) * n + k] = dist[n * k];
        for (s = 2; s < n; s++) {
            S = ((1 << s) - 1) << 1;//this is s-1 bits that start not in the 1s place as a basis set
            while ((31 - Integer.numberOfLeadingZeros(S)) < n) {
                //check that highest element in bitset is still valid
                tmp = S; i = 0;
                while (tmp != 0) {
                    //remove lowest bit repeatedly to extract elements from set
                    k_scratch[i++] = Integer.numberOfTrailingZeros(tmp);
                    //https://softwareengineering.stackexchange.com/questions/219721/clearing-the-lowest-set-bit-of-a-number
                    tmp &= tmp - 1;
                }
                for (i = 0; i < s; i++) {
                    k = k_scratch[i];
                    //not sure this helps but prob doesnt hurt
                    s_no_k_n = (S & ~(1 << k)) * n;
                    best = INF_WEIGHT;
                    for (j = 0; j < s; j++) {
                        //huge brain move: use the k scratch for m too since we are truly looking at a square
                        m = k_scratch[j];
                        //the path in subset S that ends with edge m->k
                        cur = G[s_no_k_n + m] + dist[k * n + m];
                        if (cur < best) best = cur;
                    }
                    //best case for a subproblem that ends in k
                    G[S * n + k] = (short)best;
                }
                //https://programmingforinsomniacs.blogspot.com/2018/03/gospers-hack-explained.html
                //successor function for permutations on k elements in a bitset
                //some arcane wizardry honestly
                u = S & -S; v = u + S;
                S = v + (((v ^ S) / u) >> 2);
            }
        }
        //we are closing the circuit so S is now all elements
        //this part is closing the path into a cycle
        full = ((1 << (n - 1)) - 1) << 1;
        best = INF_WEIGHT;
        for (k = 1; k < n; k++) {
            cur = G[full * n + k] + dist[k];
            if (cur < best) best = cur;
        }
        System.out.println(best);
    }
}