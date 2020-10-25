# TestUI
AirTest-Win  
Login on window aplliction Test UI Automation  
# Windows kit(SDK) tools
windows kit\bin\
Inspect.exe 定位无素windows
# android &ios
android studio UI automator view  tools->DDMS->android device monitor 定位元素开发环境
ios Accessibility Inspector Xcode->Open Developer Tool->Accessibility Inspector
# Airtest 跨平台的UI自动化测试框架

# Appium 是跨平台测试框架
Appium是一个开源、跨平台的测试框架，可以用来测试原生及混合的移动端应用。Appium支持IOS、Android及FirefoxOS平台。Appium使用WebDriver的json wire协议，来驱动Apple系统的UIAutomation库、Android系统的UIAutomator框架。Appium对IOS系统的支持得益于Dan Cuellar’s对于IOS自动化的研究。Appium也集成了Selendroid，来支持老android版本。

Appium支持Selenium WebDriver支持的所有语言，如java、Object-C、JavaScript、Php、Python、Ruby、C#、Clojure，或者Perl语言，更可以使用Selenium WebDriver的Api。Appium支持任何一种测试框架。如果只使用Apple的UIAutomation，我们只能用javascript来编写测试用例，而且只能用Instruction来运行测试用例。同样，如果只使用Google的UIAutomation，我们就只能用java来编写测试用例。Appium实现了真正的跨平台自动化测试。
iOS 9.3 and above: Apple's XCUITest
iOS 9.3 and lower: Apple's UIAutomation
Android 4.3+: Google's UiAutomator/UiAutomator2
Windows: Microsoft's WinAppDriver

# ADB
查看当前连接设备：
adb devices
如果发现多个设备：
adb -s 设备号 其他指令
adb -s devicel install xxx.apk

查看顶部Activity:
windows环境下:
adb shell dumpsys activity | findstr "mFocusedActivity"
Linux、Mac环境下：
adb shell dumpsys activity | grep "mFocusedActivity"

查看日志：
adb logcat
Logcat
adb logcat

打印日志文件。
adb logcat [options] [filter-specs]

当然可以像 Android Studio 一样只打印固定的日志

adb logcat *:V lowest priority, filter to only show Verbose level
adb logcat *:D filter to only show Debug level
adb logcat *:I filter to only show Info level
adb logcat *:W filter to only show Warning level
adb logcat *:E filter to only show Error level
adb logcat *:F filter to only show Fatal level
adb logcat *:S Silent, highest priority, on which nothing is ever printed

adb logcat -b <Buffer>

adb logcat -b radio View the buffer that contains radio/telephony related messages.
adb logcat -b event View the buffer containing events-related messages.
adb logcat -b main default
adb logcat -c Clears the entire log and exits.
adb logcat -d Dumps the log to the screen and exits.
adb logcat -f test.logs Writes log message output to test.logs .
adb logcat -g Prints the size of the specified log buffer and exits.
adb logcat -n <count> *Sets the maximum number of rotated logs to <count>. *

安装apk文件：
adb install xxx.apk
覆盖安装：
adb install -r xxx.apk

比分直接RUN出来的包是test-onlu的无法安装，推荐使用**-t**
adb install -r -t xxx.apk

卸载App:
adb uninstall com.zhy.app

如果想要保留数据，则：
adb uninstall -k com.zhy.app

往手机SDCard传递文件：
adb push 文件名 手机端SDCard路径
adb push 帅照.jpg /sdcard/

从手机端下载文件：
adb pull /sdcard/xxx.txt

查看手机端安装的所有app包名:
adb shell pm list packages

启动Activity:
adb shell am start 包名/完整Activity路径
adb shell am start com.***.***/com.***.aaa.MainActivity

如果需要携带参数(携带一个Intent,Key 为name):
adb shell am start com.***.aaa/com.***.aaa.MainActivity -e name ***
启动一个隐式的Intent:
adb shell am start -a "android.intent.action,VIEW" -d "https://www.google.com"

发送广播：
adb shell am broadcast -a "broadcastactionfilter"

屏幕截图：
可以使用screencap命令来进行手机屏幕截图，例如：
adb shell screencap /sdcard/screen.png

录制视频：
可以使用screenrecord[options] filename命令来录制屏幕视频，例如：
adb shell screenrecord /sdcard/demo.mp4

清除掉APP的缓存，还能把APP的数据给清空
adb shell pm clear com.example.packagename

查看所有App的名称：
adb shell pm list packages

查看手机上的APP名称。可以在后面加上 -f ，这样还能显示该APP的路径。
adb shell pm list packages -f 

adb shell input命令向屏幕输入一些信息
adb shell input text "insert%stext%shere"
%s表示空格。

adb shell input tap命令来模拟屏幕点击事件，例如：
adb shell input tap 500 1450
表示在屏幕上（500，1450）的坐标点上进行一次点击。

adb shell input swipe命令来模拟手势滑动事件，例如：
adb shell input swipe 100 500 100 1450 100
表示从屏幕坐标（100，500）开始，滑动到(100,1450)结束，整个过程耗时100ms.
模拟”**长按（long press）**操作，也就是2个坐标点相同，耗时超过500ms.
adb shell input swipe 100 500 100 500 500

adb shell input keyevent命令来模拟点按实体按钮的命令，例如：
adb shell input keyevent 25
命令表示调低音量。数字25是在AOSP源码中的KeyEvent类里卖弄定义的一个事件常量

am：
am(Activity Manager)命令来启动一个APP、启动Activity、启动广播和服务等等。
启动一个activity，最简单的命令可以使用adb shell am start com.package.name/com.package.name.ActivityName，例如：
adb shell am start com.example.crime/com.example.crime.MainActivity

启动带有参数，则使用**-e**标签
adb shell am start com.example.crime/com.example.crime.SecondActivity -e argus_name QiuShui
启动带的参数一般是Key-value形式，这里的key是argus_name,Value是QiuShui.
除了默认启动的activity外，打开其他的activity时，需要在清单文件中添加android:exported="true"属性。
要启动一个隐式的Intent，也就是说需要传入action等参数，在ADB调试桥中可以得知Intent的参数规范，比如**-a表示action**,-c表示category,-d表示data_uri,-e表示添加额外Key-Value信息。例如：
adb shell am start -a "android.intent.action.VIEW" -d "https://www.google.com"

am 也能发送广播和启动服务。比如启动一个广播，一般要添加一个**-a**：
adb shell am broadcast -a "our.specified.action"
还可以在上述命令后面添加**-e**来添加额外的信息。

使用下面的命令可以直接让手机重启：
adb shell am broadcast -a android.intent.action.BOOT_COMPILETED
启动一个服务也是类似，例如:
adb shell am startservice "com.example.crime/com.example.crime.MyService"

## dumpsys:获取系统数据。
dumpsys命令可以提供非常多的系统信息。
可以通过adb shell service list来查看dumpsys能提供查询信息的服务，常用的有：
服务	类名	功能
activity	ActivityManagerService	AMS相关信息
package	PackageManagerService	PMS相关信息
window	WindowManagerService	WMS相关信息
input	InputManagerService	IMS相关信息
power	PowerManagerService	PMS相关信息
procstats	ProcessStatsService	进程统计
battery	BatteryService	电池信息
alarm	AlarmManagerService	闹钟信息

adb shell dumpstate
和命令直译差不多，dumps state


adb shell dumpsys [options]
adb shell dumpsys activity 查看信息，会有很长的代码，分析其结构，可以把上述命令得到的信息拆分为:
dumpsys activity intents
dumpsys activity broadcasts
dumpsys activity providers
dumpsys activity permissions
dumpsys activity services
dumpsys activity recents
dumpsys activity activities
dumpsys activity processes
即adb shell dumpsys activity a等价于adb shell dumpsys activity activities命令等。注意：providers的缩写是prov、permissions的缩写是perm。

adb shell dumpsys activity | grep -i 'run'

查看APP有那些进程，使用adb shell dumpsys activity p <packagename> | grep -i ‘ProcessRecord’ | grep -i 'PID’
，然后程序会输出信息，你可以数一下有多少个PID开头，有多少个就表示有几个进程。还可以知道分别的进程名和PID等等。
查看APP使用了那些服务，使用 adb shell dumpsys activity s <package name> | grep -i ‘ServiceRecord’ 命令，显示结果中可以看出是谁推送的服务。
查看当前APP的内存使用情况，使用**adb shell dumpsys meminfo <package name>**命令，显示结果可以知道当前APP内存使用情况。
meminfo	MemBinder	内存
  
查看进程信息：
使用adb shell ps命令查看进程信息。可以在该命令后加包名，来查看某个应用程序的进程信息。
查看CPU使用情况：
使用**adb shell top **命令来查看系统CPU使用情况。（ctrl+c结束）

## System
adb root
获取 root 权限。

adb sideload

adb shell ps
打印进程状态。

adb shell top
展现上层 CPU 进程信息。

adb shell getprop
获取 Android 系统服务属性

adb shell setprop
设置服务属性。

68人点赞
Android

## Network
adb shell netstat
主要用于网络统计。

adb shell ping
没啥好说的，和 PC 的 ping 命令一样的。

adb shell netcfg
通过配置文件配置和管理网络连接。

adb shell netcfg [<interface> {dhcp|up|down}]

adb shell ip
主要用于显示一些数据
adb shell ip [OPTIONS] OBJECT

## File Manager
adb pull
从 Android 设备下载文件到 PC。
adb pull <remote> [local]

其中 <remote> 代表文件在设备中的地址，[local] 代表存放目录。

adb push
把 PC 的文件存放到 Android 设备。
adb push <local> <remote>

adb shell ls
列出目录内容。
adb shell ls [options] <directory>

adb shell cd
和一般的 PC 的 cd 差不多，主要用于切换目录。
adb shell cd <directory>

adb shell rm
删除文件或者目录
adb shell rm [options] <file or directory>

adb shell mkdir
创建一个文件夹
adb shell mkdir [options] <directory name>

adb shell touch
创建一个新文件或者改变文件修改时间
adb shell touch [options] <file>

adb shell pwd
定位当前的操作位置
adb shell pwd

adb shell cp
字面意思，很好理解，复制。
adb shell cp [options] <source> <dest>

adb shell mv
移动或者更名文件
adb shell mv [options] <source> <dest>

## Wireless  
adb connect
无限调试必备命令，需要保证设备和 PC 在同一局域网内，所以可通过远程桌面达到远程调试的结果。
adb connect <host>[:<port>]

此处安利一下无限调试设置方法：
打开设备的调试模式，允许 USB 以 MTP 模式传输，确保设备和 PC 能正常连接，可以通过 adb shell 或者 adb devices 等进行验证。
确保已连接后，依次执行以下命令：
adb root
adb remount
adb pull /system/build.prop ./
在 adb 命令执行的文件夹下的 build.prop 中加入命令 service.adb.tcp.port=5555
执行 adb push ./build.prop /system/ 后重启设备
结束后断开 USB 连接线，输入 adb connect 设备IP:5555 确认可以正常连接。

adb usb
设置设备以 USB 形式连接 PC。

## ADB Debugging
adb forward
端口映射，将 PC 端的某端口数据重定向到手机端的一个端口。

adb forward <local> <remote>

adb kill-server
终止 adb 进程。
adb kill-server


