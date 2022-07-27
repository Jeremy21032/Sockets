import java.net.ServerSocket;
import java.io.*;
import java.net.*;

public class servidor2 {
    public static final int PUERTO = 2103;
    public static void main(String[] args) throws Exception {
        ServerSocket servidor = null;
        Socket sc = null;
        DataInputStream in;
        DataOutputStream out;

        // Definición del puerto

        try {
            servidor = new ServerSocket(PUERTO);
            System.out.println("Servidor inicializado");
            while (true) {
                // esperar a que el cliente se conecte
                sc = servidor.accept();
                System.out.println("Cliente conectado");
                in = new DataInputStream(sc.getInputStream());
                out = new DataOutputStream(sc.getOutputStream());
                // Envío de mensaje desde el cliente
                String mensaje = in.readUTF();
                System.out.println(mensaje);

                // acknowledge → Para avisar que el mensaje fue recibido
                out.writeUTF("Mensaje recibido");

                // Cierro el socket
                sc.close();
                System.out.println("Cliente desconectado");

            }
        } catch (IOException e) {
            System.out.println("Error de conexión: servidor" + e.getMessage());
        }

    }
}
