import java.util.*;

public class AlgGrafos {
    public static void main(String args[]) {
        Random generator = new Random();
        
        Graph g1 = new Graph();
        for(int i = 0; i < 10; i++) {
            g1.add_vertex();
        }
        for(int i = 0; i < 20; i++) {
            g1.add_edge(generator.nextInt(10)+1, generator.nextInt(10)+1);
        }
        g1.add_edge(1, 2);

        g1.print();
        System.out.println("Maior grau: " + g1.max_degree()); 
        System.out.println("É não direcionado: " + g1.is_undirected()); 
        g1.BFS(1);
        System.out.println("É conexo: " + g1.is_connected()); 
    }
}
