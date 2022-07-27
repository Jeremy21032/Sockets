import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class servidor {

    public static void main(String[] args) throws Exception {
        System.out.println("Servidor");
        try (ServerSocket serverSocket = new ServerSocket(6000)) {
            System.out.println("Esperando conexión.....");
            Socket clienteSocket = serverSocket.accept();
            System.out.println("Contectado al cliente");
        } catch (IOException e) {
            // TODO: handle exception
        }
    }
}