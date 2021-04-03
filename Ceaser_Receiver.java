import java.io.*;
import java.net.*;
public class Ceaser_Receiver{
	public static void main(String args[]) throws Exception{
			ServerSocket ss=new ServerSocket(6666);  
			Socket s=ss.accept();
			DataInputStream dis=new DataInputStream(s.getInputStream());
			DataOutputStream dout=new DataOutputStream(s.getOutputStream()); 

			System.out.println("\nReceiver is Ready...");
			//int key=Integer.parseInt(dis.readUTF());
			String encryptstr=(String)(dis.readUTF());
			String decryptstr=" ";
			char ch;
			System.out.println("Cipher Text from the sender is : "+encryptstr);
			//System.out.println("Key is : "+key);
			
			for(int k = 1; k<27; k++)
			{
			for(int i = 0; i <encryptstr.length(); ++i)
			{
				ch = encryptstr.charAt(i);
			
			if(ch >= 'a' && ch <= 'z')
			{
	            ch = (char)(ch - k);
	            
	            if(ch < 'a')
				{
	               	ch = (char)(ch + 'z' - 'a' + 1);
	           	}
	        	decryptstr+= ch;
	       	}
	        else if(ch >= 'A' && ch <= 'Z')
			{
	            ch = (char)(ch - k);
				if(ch < 'A')
				{
	                ch = (char)(ch + 'Z' - 'A' + 1);
	           	}
	            decryptstr+= ch;
	        }
	        else 
			{
	        	decryptstr += ch;
	        }
			
			}
			System.out.println("Decrypted(Plain) Text For Key Value "+ k +": "+decryptstr);
			decryptstr=" ";
			}
			
			dout.flush();
			ss.close();
			dout.close();

		}

}



							
				
			
			
		