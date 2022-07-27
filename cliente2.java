import java.io.*;
import java.net.*;

public class cliente2 extends servidor2 {
    public static void main(String[] args) {
        // dirección a conectarse
        final String HOST = "172.31.115.149";
        // Puerto al servidor
        DataInputStream in;
        DataOutputStream out;
        try {
            Socket sc = new Socket(HOST, PUERTO);
            in = new DataInputStream(sc.getInputStream());
            out = new DataOutputStream(sc.getOutputStream());
            // Enviamos mensaje
            out.writeUTF("Hola servidor soy JUANITO ");;
        
            //Se recibe el mensaje

            String mensaje = in.readUTF();
            System.out.println(mensaje);
            sc.close();
        } catch (IOException e) {
            System.out.println("Error de conexión: cliente" + e.getMessage());
        }
    }
}
