import java.net.*;
import java.io.*;
import java.util.*;
import java.math.*;

public class RsaS {

    public static void main(String args[]) {
        try {
            ServerSocket ss = new ServerSocket(6666);
            Socket s = ss.accept();
            DataInputStream di = new DataInputStream(s.getInputStream());

            int n = di.readInt();
            double c = di.readDouble();
            int d = di.readInt();

            BigInteger N = BigInteger.valueOf(n);
            BigInteger msgback;

            BigInteger C = BigDecimal.valueOf(c).toBigInteger();
            msgback = (C.pow(d)).mod(N);
            System.out.println("Derypted message is : " + msgback);

        } catch (Exception e) {
            System.out.println(e);
        }

    }
}
