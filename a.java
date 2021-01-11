package U3488p1;

/**
 * 一个典型的电话拨号盘如下：

1 2 3
4 5 6
7 8 9
* 0 #

手指在两个按键之间的移动距离被定义成这两个键的x、y坐标差的绝对值之和。比如，6到自身的距离是0，到3、5、9的距离是1，到2、4、8、#的距离是2，到1、7、0的距离是3，到*的距离是4。
现在要你算一下，拨一个号手指所需要移动的最小距离是多少？假设手指初始位置在“5”。

输入
一行，一个字符串，表示需要拨的电话号码。

输入约束
电话号码的每一位仅包含数字“0”到“9”，且总长度范围是 [3,20]

输出
一个整数，表示拨完这个号码手指最少需要移动的距离

例子
输入
911
输出
6
 */
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class a {
	public static void main(String[] args)
	{
	    List<Integer> numTemp = new ArrayList();
	    Map<Integer,int[][]> mapTemp = new HashMap<>();
	    int sumMap = 0;
	    Scanner sc=new Scanner(System.in);
	    String s = sc.next();
	    int alpha = 0, digit = 0, other = 0;
	    char[] chars = s.toCharArray();
	    for (int i = 0; i < s.length(); i++){
	        if (Character.isAlphabetic(chars[i]))
	        {
	            alpha++;
	            System.out.println("请输入一串数字");
	            break;
	        } else if (Character.isDigit(chars[i])) {
	            digit++;
	            String c1 = String.valueOf(chars[i]);
	            int res =Integer.valueOf(c1);
	            numTemp.add(res);
	        }else{
	            other++;
	            System.out.println("请输入一串数字");
	            break;
	        }
	    }
	    if (3 <= digit && digit <= 20)
	    {
	        mapTemp.put(0,MapPhoneCall(5));
	        for (int j = 1; j <= numTemp.size(); j++)
	        {
	            mapTemp.put(j, MapPhoneCall(numTemp.get(j-1)));
	        }
	    } else {
	        System.out.print("请输入3至20位数字");
	    }
	    for (int x = 0; x < digit; x++)
	    {
	        int temp = 0;
	        temp = distancesum(mapTemp.get(x)[0], mapTemp.get(x+1)[0]);
	        sumMap += temp;
	    }
	    System.out.println(sumMap);
	}

	private static  int distancesum(int[] x, int[] y)
	{
	    int sum = 0;
	    for (int i = 0; i < 2; i++)
	    {
	        for (int j = i + 1; j < 2; j++)
	        {
	            sum = (Math.abs(x[i] - y[i]) + Math.abs(x[j] - y[j]));
	        }
	    }

	    return sum;
	}

	private static int[][] MapPhoneCall(int x)
	{
	    Map<Integer,int[][]> phoneCall=new HashMap<>();
	    phoneCall.put(0, new int[][]{{0,-2}});
	    phoneCall.put(1, new int[][]{{-1, 1}});
	    phoneCall.put(2, new int[][]{{0, 1}});
	    phoneCall.put(3, new int[][]{{1,1}});
	    phoneCall.put(4, new int[][]{{-1,0}});
	    phoneCall.put(5, new int[][]{{0,0}});
	    phoneCall.put(6, new int[][]{{1,0}});
	    phoneCall.put(7, new int[][]{{-1,-1}});
	    phoneCall.put(8, new int[][]{{0,-1}});
	    phoneCall.put(9, new int[][]{{1,-1}});
	    return phoneCall.get(x);
	}
}
