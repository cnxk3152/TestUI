package U3488p1;
/**
 * 这道题的主要目的是带你熟悉这个在线评测系统。你需要实现一个可执行程序，将来自标准输入的内容，原样输出到标准输出。在线评测系统将用系统内置的一些测试用例对你的程序进行评测。

输入：(这里对传给你的程序的输入格式进行说明)
一些字符串

输出：(这里对你的程序需要给出的输出格式进行说明)
与输入相同的字符串

约束：(这里对输入的字符和数字规模进行约束)
输入字符串仅包含大小写字母、数字、空格和标点符号，仅有一行

举例1：(这里是一些输入和期望输出的举例)
输入：
hello the world
输出：
hello the world

举例2：
输入：
hello world!
输出：
hello world!
 */
import java.io.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class U3488p1{
	private static Pattern patt;
	private static Pattern patt1;
	private static Pattern patt2;
	
	private static Matcher mat1;
	private static Matcher mat2;
	private static Matcher mat3;

	
	public static void main(String []args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //int n = Integer.parseInt(br.readLine().trim());
        
        String str=br.readLine().trim();
        String pattern="^(?![A-Za-z]+$)(?![A-Z0-9_\\W]+$)(?![a-z0-9\\W]+$)[\\w\\W]{8,}$";
        String pattern1="^(?![0-9]+$){6,}$";
        String pattern2="^(?![A-Za-z]+$){8,}$";
        
        patt=Pattern.compile(pattern);
        patt1=Pattern.compile(pattern1);
        patt2=Pattern.compile(pattern2);
        
        mat1=patt.matcher(str);
        mat2=patt1.matcher(str);
        mat3=patt2.matcher(str);

        
        if(mat1.matches())
        {
        System.out.println(str);
        }
        else if(!mat2.matches())
        {
        	System.out.println(str);
        }
        else if(!mat3.matches())
        {
        	System.out.println(str);
        }
        else
        {
        	System.out.println("error!!!");
        }
        
    }
}