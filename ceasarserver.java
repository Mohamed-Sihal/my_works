import java.io.DataInputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.*;
import java.io.*;
import java.util.*;

class ceasarserver {

	public static void main(String args[]) {
		try {
			String ALPHABET = "abcdefghijklmnopqrstuvwxyz";
			int shiftKey;
			Scanner sc = new Scanner(System.in);
			ServerSocket serverSocket = new ServerSocket(5000);
			System.out.println("Waiting for Client...");
			Socket socket = serverSocket.accept();
			System.out.println("Client Connected...");
			DataInputStream dis = new DataInputStream(socket.getInputStream());
			DataOutputStream dout = new DataOutputStream(socket.getOutputStream());
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			System.out.println("Enter the key size");
			shiftKey = sc.nextInt();
			System.out.println("Enter the plain text");
			String message = "";
			message = sc.next();
			// message= br.readLine();
			System.out.println("Client Plain Text is : " + message);
			System.out.println("length of the plain text is " + message.length());
			message = message.toLowerCase();
			String cipherText = "";
			for (int i = 0; i < message.length(); i++) {
				int charPosition = ALPHABET.indexOf(message.charAt(i));
				int keyVal = (shiftKey + charPosition) % 26;
				char replaceVal = ALPHABET.charAt(keyVal);
				cipherText += replaceVal;
			}
			cipherText = cipherText.toUpperCase();
			System.out.println("Cipher is:" + cipherText);
			dout.writeUTF(cipherText);
			serverSocket.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
