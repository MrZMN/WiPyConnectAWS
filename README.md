# WiPyConnectAWS
It's about the process of connecting WiPy with AWS IoT. And the relevant problems I faced.

   This essay is about connecting WiPy with AWS IoT services. And the point is the problem I've faced and the corresponding solutions. (Trust me, I must be the first person who have faced so many problems.)
   1. To connect WiPy with AWS, firstly you need to have an AWS account. So far all the services you need are for free.
   2. Then open the 'AWS IoT'. You need to offer your advice(WiPy board) an 'object'. You can do the relevant things in the following: https://docs.pycom.io/chapter/tutorials/all/aws.html  Trust me, it's very easy. Besides, you could also just click the 'induction training' on the left, and then click 'configure the devices'. It will provide pretty transparent instructions for you!
   3. After you do these things, you will have four files in your hand, which are 'XXX.private.key' 'XXX.public.key' 'root-CA.crt' 'XXX.cert.pem'. You should put there files(except for the public key) into your WiPy board. What's more, you also need a folder 'AWSIoTPythonSDK' and put it into your board either. (You can get it from: https://github.com/pycom/aws-pycom) The relevant instructions are also in this web page: https://docs.pycom.io/chapter/tutorials/all/aws.html
   4. Next, you need a 'main.py' and 'config.py', and you can get them from me! Don't forget to change the settings in 'config.py', which includes: WiFi settings, certificate files pathes, AWS_HOST.
   5. Put all the files above into your WiPy! BINGO!
   
   
   Trouble Shooting:
   The followings are the most important things you may want to know, which are the problems I've faced and the solutions:
   
   Problem 1: When you download 'root_CA.crt' from AWS, you may not download a file directly, but opened a new web page which includes the content of the certification.
   Solution1: Just copy the content(Remember: copy the whole content! Include '---begin certificate---' and 'end certificate---') and put them in a new '.txt'. Then name the file 'root-CA.crt'. It could be used then.
   
   Problem 2: The WiPy suddenly can't be connected to computer via WiFi. (The computer couldn't search the WiFi of the board) In this way I can't use FTP to transfer files among them.
   Solution 2: The WiPy contains two different modes: STA(station) moade and AP mode. And the WiPy could connect via WiFi only in AP mode. If you have to use FTP, you can use these codes:
    import machine
    from network import WLAN
    wlan = WLAN(mode=WLAN.AP)
    You can also change them in your 'main.py'. In this way your board will be back to AP mode.
    
    Problem 3: Sometimes you can't upload/download files to/from computer via USB. If you do so, it will show: 'Cannot read property 'split' of null'
    Solution 3: This is something really strange. I suggest you to reboot your board/reinstall the firmware. If these couldn't work, try to reset your board using the reset button on your board. (Honestly, do it when you have to.)
    
    Problem 4: Sometimes when you upload/download files using USB, it will show 'memory not enough'
    Solution 4: Try to clear your board. Use these codes:
    import os
    os.mkfs(‘/flash’)
    Provided by a friend..Really useful!
    
    Problem 5: The pathes in 'config.py' seem to be wrong. it always shows 'certificate file not found'
    Solution 5: Use FTP. By using USB you may face lots of path problems. Comparing with this, FTP is a much better choice! (If you can't connect via WiFi, return to Problem 2)
    
    Except for these problems and relevant solutions, if you still have some problems, try to do these things:
    Check your python environment
    Install Git environment
    Install AWS SDK for IoT
    Install FTDI driver
    
    That's all, thanks for reading!
    
