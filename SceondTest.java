package U3488p1;
/**
 * ��ʹ�õݹ�ķ�ʽ�ж�һ�������������Ƿ�Ϊ2���������ݡ�
��ʾ����һ���� n = 2^k ��kΪ�Ǹ�������ʱ������˵n��2��������k�����ݡ����� 2��4��8��16����2���������ݣ���3��7��14�Ͳ��ǡ�

����
һ�У�һ��������n

����Լ����
1<=n<=2^31

���
һ�У�����1��0��
�������Ϊ2���������ݣ������1���������0��
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SceondTest {
  private static int
  isPowerOfTwo(int n)
  {
	  int a;
	  if(n<=1&&n>=(2<<31))
	  { 
		  a=0;
	  }
	  
	  if((n & (n-1))==0)
	  {
		  a=1;
		  
	  }else
	  {
		  a=0;
	  }
	 return a; 
  }
  public static void main(String[] args) throws IOException
  {
	  BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
	  String s=br.readLine();
	  int n=Integer.parseInt(s);
	  
	  System.out.println(isPowerOfTwo(n));
	  
  }
}
