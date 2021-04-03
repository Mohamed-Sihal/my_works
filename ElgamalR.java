import java.math.*;
import java.util.*;
import java.security.*;
import java.io.*;
import java.net.*;

public class ElgamalR {
    public static void main(String args[]) {
        try {
            ServerSocket ss = new ServerSocket(6666);
            Socket s = ss.accept();
            DataInputStream di = new DataInputStream(s.getInputStream());

            BigInteger brmodp = new BigInteger(di.readUTF());
            BigInteger secret = new BigInteger(di.readUTF());
            BigInteger p = new BigInteger(di.readUTF());
            BigInteger EC = new BigInteger(di.readUTF());

            BigInteger crmodp = brmodp.modPow(secret, p);
            BigInteger d = crmodp.modInverse(p);
            BigInteger ad = d.multiply(EC).mod(p);
            System.out.println("Decrypted Number : " + ad);

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
