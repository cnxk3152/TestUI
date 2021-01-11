package U3488p1;

/**
 * һ�����͵ĵ绰���������£�

1 2 3
4 5 6
7 8 9
* 0 #

��ָ����������֮����ƶ����뱻���������������x��y�����ľ���ֵ֮�͡����磬6������ľ�����0����3��5��9�ľ�����1����2��4��8��#�ľ�����2����1��7��0�ľ�����3����*�ľ�����4��
����Ҫ����һ�£���һ������ָ����Ҫ�ƶ�����С�����Ƕ��٣�������ָ��ʼλ���ڡ�5����

����
һ�У�һ���ַ�������ʾ��Ҫ���ĵ绰���롣

����Լ��
�绰�����ÿһλ���������֡�0������9�������ܳ��ȷ�Χ�� [3,20]

���
һ����������ʾ�������������ָ������Ҫ�ƶ��ľ���

����
����
911
���
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
	            System.out.println("������һ������");
	            break;
	        } else if (Character.isDigit(chars[i])) {
	            digit++;
	            String c1 = String.valueOf(chars[i]);
	            int res =Integer.valueOf(c1);
	            numTemp.add(res);
	        }else{
	            other++;
	            System.out.println("������һ������");
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
	        System.out.print("������3��20λ����");
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
