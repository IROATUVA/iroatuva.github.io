import sys # An included library with Python install.
from datetime import date # An included library with Python install.
import datetime # An included library with Python install.
import os # An included library with Python install.

months = {1:"Jan", 2:"Feb", 3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}

top_banner = '''.barlist {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

.bar {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.bar a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #4CAF50;
}
</style>
</head>
<body>
'''
heading = '<!DOCTYPE HTML>\n<html>\n<head><!Content created by Mohit Srivastav. IRO Treasurer term Spring 2020-Fall 2020>\n'

def bulleted_list_maker(obj_list):
	if isinstance(obj_list,list):
		code_text = ''
		code_text += '<ul>\n'
		for i in obj_list:
			code_text += '\t<li><h2> ' + i + ' </h2></li>\n'
		code_text += '</ul>\n'
		return code_text
	else:
		return None


def write_HTML():
	import shutil
	bank_charts = []
	mainPageGraph = ""
	for files in os.listdir("."):
		if "Bank_Account_Data_IRO" in files:
			shutil.copy(files, "iroatuva.github.io")
			bank_charts.append(files)
			if mainPageGraph == "":
				mainPageGraph = files
			else:
				date_from = mainPageGraph[22:30].split('_')
				date_from = datetime.datetime(int(date_from[2]),int(date_from[0]),int(date_from[1]))
				date_compared = files[22:30].split('_')
				date_compared = datetime.datetime(int(date_compared[2]),int(date_compared[0]),int(date_compared[1]))
				if date_compared < date_from:
					mainPageGraph = files


	shutil.copy("BoFa.csv","iroatuva.github.io")


	day = str(date.today())
	day = day.split('-')
	day = day[1] + '-' + day[2] + '-' + day[0]

	with open('BoFa.csv') as read:
		x = read.readline().split(',')[1]
		for last_line in read:
			pass
		last_line = last_line.split(',')[0]
	cur_amt = str(format(float(x),','))
	last_line = last_line.split('/')
	with open('BoFa.csv') as min_max:
		money = {}
		for line in min_max:
			line = line.replace('\n','').split(',')
			money[float(line[1])] = line[0]

	code_text = ''
	min_num = str(format(min(money),','))
	max_num = str(format(max(money),','))

	min_date = money[min(money)].split('/')
	min_date = months[int(min_date[0])] + ' ' + min_date[1] + ', ' + min_date[2]
	minimum = 'The minimal amount in the account was $' + min_num + ' on ' + min_date

	max_date = money[max(money)].split('/')
	max_date = months[int(max_date[0])] + ' ' + max_date[1] + ', ' + max_date[2]
	maximum = 'The maximal amount in the account was $' + max_num + ' on ' + max_date

	min_max = [minimum, maximum]

######################################## THE MAIN PAGE #####################################

	code_text += heading
	code_text += '<style>\n'
	code_text += 'img{border-style: double; width:100%;}\n'
	code_text += top_banner
	code_text += '''<ul class = "barlist">
  <li class = "bar"><a class="active" href="./">Home</a></li>
  <li class = "bar"><a href="datapage">Day-by-day Data</a></li>
  <li class = "bar"><a href="https://www.iroatuva.org/about">About</a></li>
  <li class = "bar"><a href="charts">Extra Charts and Graphs</a></li>
  <li class = "bar"><a href="branch">Statistics by Branch</a></li>
</ul>\n'''
	code_text += '<h1 style = "text-align:center;"> International Relations Organization at UVA\'s Data Webpage</h1>\n'
	code_text += '<h2 style = "background-color:tomato; text-align:center;"> IRO at UVA is not officially affiliated with the university</h2>\n'
	code_text += '<h2 style = "text-align:center;"> Last Updated ' + day + '</h2>\n'
	code_text += '<h2 style = "text-align:center;"> <strong> The IRO bank account has $' + str(cur_amt) + ' as of now </strong></h2>\n'
	code_text += '<h2 style = "text-align:center";> Since ' + months[int(last_line[0])] + ' ' + last_line[1] + ', ' + last_line[2] + ':</h2>\n'
	code_text += bulleted_list_maker(min_max)
	code_text += '<figure>\n'
	code_text += '<img src = "' + mainPageGraph + '" alt = "A graph of the bank account">\n'
	code_text += '<figcaption style = "text-align:center;"> The Bank Account Over Time </figcaption>\n'
	code_text += '</figure>\n'
	code_text +='</body>\n</html>'
	print(code_text)
	with open('index.html','w+',encoding = 'utf-8') as g:
		g.write(code_text)
		code_text = '' #You are now done with the main page
	shutil.move('index.html','iroatuva.github.io/index.html')
	bank_charts.remove(mainPageGraph)


################################################ THE DAY-BY-DAY DATA PAGE ############################
	code_text += heading
	code_text += '<style>\n'
	code_text += top_banner
	code_text += '''<ul class = "barlist">
  <li class = "bar"><a href="../">Home</a></li>
  <li class = "bar"><a class="active" href="./">Day-by-day Data</a></li>
  <li class = "bar"><a href="https://www.iroatuva.org/about">About</a></li>
  <li class = "bar"><a href="../charts">Extra Charts and Graphs</a></li>
  <li class = "bar"><a href="../branch">Statistics by Branch</a></li>
</ul>\n'''
	code_text += '</style>\n</head>\n<body>\n'
	code_text += '<h1 style = "text-align:center;"> Tables of Raw Data</h1>\n'
	code_text += '''<select class="default" id="data_shower" name="data_shower">
        <option value="" selected>Select the type of data you want to show</option>
        <option value="1">Bank Account Data</option>
        <option value="2">I have nothing else this is a placeholder for future data</option>
    </select>\n'''
	code_text += '<div id = "one" style="display:none" "width:100%";>\n'
	code_text += '<table style="width:100%";>\n'
	code_text += '''<tr>
	<th colspan = "2"> <h1> Bank Account Data by Day </h1> </th>
</tr>\n'''
	code_text += '''<tr>
	<th> Date </th>
	<th> Amount </th>
</tr>\n'''
	with open('Bofa.csv') as f:
		for line in f:
			line = line.strip().split(',')
			code_text += '<tr>\n' + '\t' + '<th> ' + line[0] + ' </th>\n'
			code_text += '\t<th> ' + line[1] + ' </th>\n'
			code_text += '</tr>\n'
	code_text += '</table>\n</div>\n'
	code_text += '<div id = "two" style = "display:none;"> Placeholder </div>\n'
	code_text += '<script>\n'
	code_text += '''var elem = document.getElementById("data_shower");
var x = ["one","two"];
elem.onchange = function(){
	if (elem.value == ""){
		for(var i = 0; i < x.length; i++){
    		document.getElementById(x[i]).style.display = "none";
    	}
	}
    if (elem.value == "1"){
    	for(var i = 0; i < x.length; i++){
    		document.getElementById(x[i]).style.display = "none";
    	}
			document.getElementById("one").style.display = "block";
    } else if(elem.value == "2"){
    	for(var i = 0; i < x.length; i++){
    		document.getElementById(x[i]).style.display = "none";
    	}
      document.getElementById("two").style.display = "block";
      }
};\n'''
	code_text += '</script>\n</body>\n</html>'
	with open('datapage.html','w+',encoding = 'utf-8') as f:
		f.write(code_text)
		code_text = ''
	shutil.move('datapage.html','iroatuva.github.io/datapage.html') #You are now done with the data page

######################### THERE IS NO ABOUT PAGE. TAKE OFF YOUR CLOTHES ###########################


######################## Extra charts and graphs page ##############################################
	code_text += heading
	code_text += '<style>\n'
	code_text += 'img{border-style: double; width:100%;}\n'
	code_text += top_banner
	code_text += '''<ul class = "barlist">
  <li class = "bar"><a href="../">Home</a></li>
  <li class = "bar"><a href="../datapage">Day-by-day Data</a></li>
  <li class = "bar"><a href="https://www.iroatuva.org/about">About</a></li>
  <li class = "bar"><a class="active" href="./">Extra Charts and Graphs</a></li>
  <li class = "bar"><a href="../branch">Statistics by Branch</a></li>
</ul>\n'''
	code_text += '<h1 style = "text-align:center;"> Some Extra Graphs </h1>\n'
	code_text += '<h2 style = "text-align:center;"> Last Updated ' + day + '</h2>\n'
	for i in bank_charts:
		code_text += '<img src = "' + i + '" alt = "Another graph of the bank account">\n'
	code_text += '</body>\n</html>'
	with open('charts.html', 'w+', encoding = 'utf-8') as f:
		f.write(code_text)
		code_text = ''
	shutil.move('charts.html','iroatuva.github.io/charts.html')

	shutil.copy('website_designer.py', 'iroatuva.github.io')

write_HTML()