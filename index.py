#!C:\python36\python.exe
print("Content-type:text/html")
print("")
print("""
<html>
<head>
	<title>home page</title>
	<link rel="icon" href="img/CT.png" />
	<style type="text/css">
	div{	color: black;
		text-align: center;
		background-color: skyblue;
		height: 70px;
		outline: 1px solid black;
	}
	</style>
</head>
<body bgcolor="#00FFD2">
	<center>
		<img src="img/CT.png" height="50" width="50"><br><br>
		this is a home page
	</center>
	<br><br>
	<div id="jan" >
		<a href="credit.py">Credit Transfer</a>
	</div>
</body>
</html>
""")
