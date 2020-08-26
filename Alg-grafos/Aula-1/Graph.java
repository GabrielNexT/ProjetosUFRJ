import java.beans.VetoableChangeListener;
import java.util.*;

public class Graph {
    private HashMap<Integer,Vertex> vertex_set;
    private List<Boolean> vis = new ArrayList<Boolean>();

    public Graph() {
        vertex_set = new HashMap<Integer,Vertex>();
    }
    
    public void add_vertex() {
        Vertex v = new Vertex( vertex_set.size()+1 );
        vertex_set.put( v.id, v );
    }
    
    public void add_arc( Integer id1, Integer id2) {
        Vertex v1 = vertex_set.get(id1);
        Vertex v2 = vertex_set.get(id2);
        v1.add_neighbor( v2 );
    }

    public void add_edge( Integer id1, Integer id2) {
        Vertex v1 = vertex_set.get(id1);
        Vertex v2 = vertex_set.get(id2);
        v1.add_neighbor( v2 );
        v2.add_neighbor( v1 );
    }

    public int max_degree() {
        int maior = -(int)1e9;
        for(Map.Entry<Integer,Vertex> tmp : vertex_set.entrySet()) {
            Vertex u = tmp.getValue();
            maior = Math.max(maior, u.size());
        }
        return maior;
    }

    public boolean is_undirected() {
        return true;
    }

    
    public Graph subjacent() {
        HashMap<Integer,Vertex> tmp = vertex_set;

        for(int i = 1; i < tmp.size(); i++) {
            for(Map.Entry<Integer,Vertex> u : tmp.get(i).getAdj().entrySet()) {
                if(u.getKey() == i) {
                    tmp.get(u.getKey()).remove(i);
                }
            }
        }

        return this;
    }

    public boolean is_connected() {
        boolean ok = true;
        for(int i = 0; i <= vertex_set.size(); i++) vis.add(false);
        dfs(1);
        for(int i = 1; i <= vertex_set.size(); i++) if(!vis.get(i)) ok = false;
        vis.clear();
        return ok;
    }

    private void dfs(int u) {
        if(vis.get(u)) return;
        vis.set(u, true);
        for(Map.Entry<Integer, Vertex> tmp : vertex_set.get(u).getAdj().entrySet())
            dfs(tmp.getKey());
    }
    
    public void BFS( Integer id_raiz ) {
        boolean[] vis = new boolean[vertex_set.size()+1];
        Arrays.fill(vis, false);
        vis[id_raiz] = true;
        Queue<Integer> q = new LinkedList<Integer>();
        q.add(id_raiz);
        while(!q.isEmpty()) {
            Vertex u = vertex_set.get(q.remove());
            for(Map.Entry<Integer, Vertex> tmp : u.getAdj().entrySet()) {
                if(vis[tmp.getKey()]) continue;
                else {
                    vis[tmp.getKey()] = true;
                    q.add(tmp.getKey());
                }
            }
        }
    }

    public void print() {
        System.out.println("Grafo: ");

        for(int i = 1; i <= vertex_set.size(); i++)
            vertex_set.get(i).print();
        System.out.println();
    }
}

