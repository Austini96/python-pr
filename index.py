#!C:\Users\Austin\AppData\Local\Programs\Python\Python310\python.exe
import sys

def enc_print(string='', encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')

enc_print("Content-type:text/html")
enc_print()
enc_print("""
<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
  <ol>
    <li><a href="1.html">HTML</a></li>
    <li><a href="2.html">CSS</a></li>
    <li><a href="3.html">JavaScript</a></li>
  </ol>
  <h2>WEB</h2>
  <p style="margin-bottom:45px;"><a href="https://en.wikipedia.org/wiki/World_Wide_Web" target="_blank" title="WWW specification">The World Wide Web (WWW)</a>, commonly known as the Web, is an information system where documents and other web resources are identified by Uniform Resource Locators (URLs, such as https://example.com/), which may be interlinked by hyperlinks, and are accessible over the Internet.[1][2] The resources of the Web are transferred via the Hypertext Transfer Protocol (HTTP), may be accessed by users by a software application called a web browser, and are published by a software application called a web server. The World Wide Web is built on top of the Internet, which pre-dated the Web by over two decades.</br>

<br>English scientist Tim Berners-Lee co-invented the World Wide Web in 1989 along with Robert Cailliau. He wrote the first web browser in 1990 while employed at CERN near Geneva, Switzerland.[3][4] The browser was released outside CERN to other research institutions starting in January 1991, and then to the general public in August 1991. The Web began to enter everyday use in 1993–1994, when websites for general use started to become available.[5] The World Wide Web has been central to the development of the Information Age and is the primary tool billions of people use to interact on the Internet.[6][7][8][9][10]</br>

<br>Web resources may be any type of downloaded media, but web pages are hypertext documents formatted in Hypertext Markup Language (HTML).[11] Special HTML syntax displays embedded hyperlinks with URLs, which permits users to navigate to other web resources. In addition to text, web pages may contain references to images, video, audio, and software components, which are either displayed or internally executed in the user's web browser to render pages or streams of multimedia content.</br>

<br>Multiple web resources with a common theme and usually a common domain name make up a website. Websites are stored in computers that are running a web server, which is a program that responds to requests made over the Internet from web browsers running on a user's computer. Website content can be provided by a publisher or interactively from user-generated content. Websites are provided for a myriad of informative, entertainment, commercial, and governmental reasons.</p>
  <img src="photo.jpg" width="100%">
</body>
</html>
""")
