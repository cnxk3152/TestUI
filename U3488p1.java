package U3488p1;
/**
 * ��������ҪĿ���Ǵ�����Ϥ�����������ϵͳ������Ҫʵ��һ����ִ�г��򣬽����Ա�׼��������ݣ�ԭ���������׼�������������ϵͳ����ϵͳ���õ�һЩ������������ĳ���������⡣

���룺(����Դ�����ĳ���������ʽ����˵��)
һЩ�ַ���

�����(�������ĳ�����Ҫ�����������ʽ����˵��)
��������ͬ���ַ���

Լ����(�����������ַ������ֹ�ģ����Լ��)
�����ַ�����������Сд��ĸ�����֡��ո�ͱ����ţ�����һ��

����1��(������һЩ�������������ľ���)
���룺
hello the world
�����
hello the world

����2��
���룺
hello world!
�����
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