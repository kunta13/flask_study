#!/usr/bin/env python
#coding:utf-8
import csv

with open('/Users/huangkun/flask_study/list.csv') as csvFile:
		reader = [each for each in csv.DictReader(csvFile)]



html_file = '/Users/huangkun/flask_study/templates/result.html'		
fp = open(html_file, 'w+')
fp.write('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>Starter Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="starter-template.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="/static/js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="http://cdn.bootcss.com/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="http://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">HK‘s Quant</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
        
        </div><!--/.nav-collapse -->
      </div>
    </nav>

   <div class="container-fluid">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
          <ul class="nav nav-sidebar">
            <li class="active"><a href="#">股票</a></li>
            <li><a href="#">选股策略</a></li>
            <li><a href="#">股票回测</a></li>
            <li><a href="#">股票实盘</a></li>
          </ul>
          
        </div>
        <div class="col-sm-9 col-sm-offset-2 col-md-8 col-md-offset-0 main">
          

          <h2 class="sub-header">结果显示</h2>
          <div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>日期</th>
                  <th>股票代码</th>
                  <th>买入价</th>
                  <th>目前价格</th>
                  <th>盈亏比例</th>
                </tr>
              </thead>
              <tbody>
''')

fp.write("\n")
for line in reader:
    #print line['date'],line['change']
	fp.write("<tr>")
	fp.write("\n")
	fp.write("<td>%s</td>" % line['date'])
	fp.write("\n")
	fp.write("<td>%s</td>" % line['code'])
	fp.write("\n")
	fp.write("<td>%s</td>" % line['buy_price'])
	fp.write("\n")
	fp.write("<td>%s</td>" % line['real_price'])
	fp.write("\n")
	fp.write("<td>%s</td>" % line['change'])
	fp.write("\n")
	fp.write("</tr>")
	fp.write("\n")
	fp.write("\n")   
    
fp.write('''
</tbody>
            </table>
          </div>
        </div>
      </div>
    </div>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://cdn.bootcss.com/jquery/1.11.1/jquery.min.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="/static/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
''')
fp.close()