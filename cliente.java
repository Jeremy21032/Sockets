import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;

public class cliente {
    public static void main(String[] args) throws Exception {
        try {
            System.out.println("Esperando conexión.....");
            InetAddress localAddress = InetAddress.getLocalHost();
            try {
                Socket clienteSocket = new Socket(localAddress, 6000);
                //PrintWriter out = new PrintWriter(clienteSocket.getOutputStream(), true);
                //BufferedReader br = new BufferedReader(new InputStreamReader(clienteSocket.getInputStream()));}
                System.out.println("conectado");

            } catch (IOException e) {
                // TODO: handle exception
            }
        } catch (IOException e) {
            // TODO: handle exception
        }
    }
}
