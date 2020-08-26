import java.util.HashMap;

public class Vertex {
    public Integer id;
    private HashMap<Integer,Vertex> nbhood;

    public Vertex ( int id ) {
        this.id = id;
        nbhood = new HashMap<Integer,Vertex>();
    }
    
    public void add_neighbor( Vertex viz ) {
        nbhood.put(viz.id, viz);
    }

    public int size() {
        return nbhood.size();
    }

    public void remove(Integer id) {
        nbhood.remove(id);
    }
    
    public void print() {
        System.out.print("\nId do vertice = " + id + ", Vizinhança: " );
        for( Vertex v : nbhood.values())
            System.out.print(" " + v.id );
    }

    public boolean hasSon (int u) {
        return (nbhood.get(u) != null);
    }

    public HashMap<Integer,Vertex> getAdj() {
        return nbhood;
    }


}