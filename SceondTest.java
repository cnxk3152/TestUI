package U3488p1;
/**
 * 请使用递归的方式判断一个给定的整数是否为2的整数次幂。
提示：当一个数 n = 2^k （k为非负整数）时，我们说n是2的整数（k）次幂。比如 2、4、8、16都是2的整数次幂，但3、7、14就不是。

输入
一行，一个正整数n

输入约束：
1<=n<=2^31

输出
一行，数字1或0。
如果输入为2的整数次幂，则输出1，否则输出0。
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
