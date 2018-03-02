#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os
class transformer():
    def __init__(self):
        self.config()
        self.head=""
        self.cssStyle=""
        self.head+='<meta http-equiv="content-type" content="text/html; charset=UTF-8">'
        self.head+='<meta name="viewport" content="width=device-width">'
        if self.config['outCss']==True:
            self.head+='<link rel="stylesheet" type="text/css" media="all" href="../css/article_styles.css">'
        else:
            self.cssStyle='''<style>body{
  background-color: rgba(200,200,200,0.8);
}
div.codeBlock{
  border-radius: 10px;
  padding: 4px;
  background-color: rgba(127, 127, 127, 0.5);
}

div.citation{
  border-radius: 10px;
  padding: 4px;
  background: rgba(50,50,50,0.7);
  color: white;
}
table{
  margin: 10px;
}
td,tr {
   border-collapse:collapse;
   cellspacing:0;
}
table td{
  border: 1px solid grey;
  border-collapse:collapse;
  border-radius: 10px;
}
table th{
  background: rgba(100, 137, 209,0.8);
  margin: 1px;
  border-radius: 10px;
  padding: 1px;
  text-align: center;
  text-decoration: none;
  color: inherit;
}
table a{
  display: block;
  background: pink;
  margin: 1px;
  border-radius: 10px;
  padding: 1px;
  text-align: center;
  text-decoration: none;
  color: inherit;
}
a{
  margin: 3px;
  display: inline-block;
  text-decoration: none;
  color: rgba(194, 64, 24,0.8);
}</style>'''
        self.text=None
    def config(self):
        self.config=dict()
        self.config['outCss']=True
    def loadMarkdown(self, fileName):
        if(os.path.exists(fileName)):
            f=file(fileName,"rt")
            self.text=f.read()
        else:
            print "No such file"
    def loadCss(self,fileName):
        if (os.path.exists(fileName)):
            f = file(fileName, "rt")
            self.cssStyle = f.read()
        else:
            print "No such file"
    def transformCodeBlocks(self):
        print 'transform CodeBlocks...'
        if(self.text is None):
            return
        result=re.findall("(\n```[^`]*?\n([^`]+\n)```)",self.text)
        for index,each in enumerate(result):
            repl = each[1].replace('&', '&amp;')
            repl = repl.replace('<','&lt;')
            repl = repl.replace('>','&gt;')
            repl = repl.replace('\"','&quot;')
            repl = repl.replace('\'','&apos;')
            self.text=self.text.replace(each[0],"\n<div class='codeBlock'><pre class='codeBlockPre'><blockquote>"+repl+"</blockquote></pre></div>",1)
    def transformHeaders(self):
        print 'transform Headers...'
        if (self.text is None):
            return
        result = re.findall("((#+)\s+?([^#]+?\n))", self.text)
        for index, each in enumerate(result):
            repl = each[2].replace('&', '&amp;')
            repl = repl.replace('<', '&lt;')
            repl = repl.replace('>', '&gt;')
            repl = repl.replace('\"', '&quot;')
            repl = repl.replace('\'', '&apos;')
            if repl.endswith('\n'):
                repl = repl.strip('\n')
            self.text=self.text.replace(each[0],'<h'+str(len(each[1]))+' id="'+repl+'">'+str(repl)+'</h'+str(len(each[1]))+'>\n',1)
    def transformTables(self):
        print 'transform Tables...'
        if (self.text is None):
            return
        patternTable = re.compile("((?:\|(?:[^\|\n]+\|)+\n)+)")
        patternRow=re.compile("(?:\|(?:[^\|\n]+\|)+\n)")
        result = patternTable.findall(self.text)
        for index, eachTable in enumerate(result):
            rowList=patternRow.findall(eachTable)
            newTable="<table cellspacing='0'>"
            for rowIndex,eachRow in enumerate(rowList):
                if rowIndex==0:
                    eachRow=re.sub("\|","</th><th>",eachRow)
                    eachRow=re.sub("^</th><th>","<tr><th>",eachRow)
                    eachRow=re.sub("</th><th>\n$","</th></tr>",eachRow)
                    newTable+=eachRow
                elif rowIndex>1:
                    eachRow = re.sub("\|", "</td><td>", eachRow)
                    eachRow = re.sub("^</td><td>", "<tr><td>", eachRow)
                    eachRow = re.sub("</td><td>\n$", "</td></tr>", eachRow)
                    newTable+=eachRow
            newTable+="</table><br>"
            self.text=patternTable.sub(newTable,self.text,1)
        pass
    def transformLatex(self):
        self.head+= "<script type='text/x-mathjax-config'>"\
                    "  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$']]}});"\
                    "</script>"\
                    "<script type='text/javascript' "\
                    "src='http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'>"\
                    "</script>"
        pass
    def transformURLs(self):
        print 'transform URLs...'
        if (self.text is None):
            return
        pattern=re.compile("([^!])\[(.*?)\]\((.+?)\)")
        result = pattern.findall(self.text)
        for index, each in enumerate(result):
            self.text = re.sub("[^!]\[(.*?)\]\((.+?)\)",each[0]+'<a class="url" href="' + str(each[2]) + '">' + str(each[1]) + '</a>',self.text, 1)
            pass
        pass
    def transformImages(self):
        print 'transform Images...'
        if (self.text is None):
            return
        pattern = re.compile("!\[(.*?)\]\((.+?)\)")
        result = pattern.findall(self.text)
        for index, each in enumerate(result):
            self.text = re.sub("!\[(.*?)\]\((.+?)\)",
                               '<div class="image"><image src="' + str(each[1]) + '" title="'+str(each[0])+'"></image></div>', self.text, 1)
            pass
        pass
    def transformCitations(self):
        print 'transform Citations...'
        if (self.text is None):
            return
        pattern=re.compile("(\n(?:>.*?\n)+)")
        result = pattern.findall(self.text)
        for index, eachPara in enumerate(result):
            newPara=re.sub('\n>','<br>',eachPara)
            newPara="<div class='citation'><p class='citationP'>"+newPara+"</p></div>"
            self.text=pattern.sub(newPara, self.text,1)
            pass
        pass
    def transformListItems(self):
        print 'transform ListItems...'
        if (self.text is None):
            return
        # * 号类
        pattern = re.compile("\n((?:&emsp;)*)(?:\*\s+([^\n]+))")
        result = pattern.findall(self.text)
        for index, each in enumerate(result):
            self.text=pattern.sub(each[0]+'<div class="liRank'+str(len(each[0])/6)+'"><li class="liRank'+str(len(each[0])/6)+'">'+each[1]+"</li></div>",self.text,1)
        # 1. 类
        pattern = re.compile("\n((?:&emsp;)*)(?:(\d+\.\s+[^\n]+))")
        result = pattern.findall(self.text)
        for index, each in enumerate(result):
            self.text=pattern.sub(each[0]+'<div class="ulRank'+str(len(each[0])/6)+'"><ul class="ulRank'+str(len(each[0])/6)+'">'+each[1]+"</ul></div>",self.text, 1)
        pass
    def transformStrength(self):
        print 'transform Strength...'
        if (self.text is None):
            return
        pattern = re.compile("\*\*((?:.|\n)+?)\*\*")
        result = pattern.findall(self.text)
        for index, each in enumerate(result):
            self.text = pattern.sub('<strong>'+each + "</strong>", self.text, 1)
        pass
    def transformAll(self):
        self.transformCodeBlocks()
        self.transformHeaders()
        self.transformTables()
        self.transformLatex()
        self.transformURLs()
        self.transformImages()
        self.transformCitations()
        self.transformListItems()
        self.transformStrength()
        # print self.text
    def saveAsHtml(self,desFileName):
        f=file(desFileName,"w")
        f.write("<!DOCTYPE html>\n<html>\n<head>")
        f.write(self.head)
        if self.config['outCss']==False:
            f.write(self.cssStyle)
        f.write("</head>\n<body>")
        f.write("<div class='content'>")
        if(self.text):
            f.write(self.text)
        else:
            print 'no'
        f.write("</div></body>\n</html>\n")
        f.close()
def single():
    tran=transformer()
    tran.loadMarkdown("./ARTICLE/2017-10-16.md")
    tran.loadCss("./css/article_styles.css")
    tran.transformAll()
    tran.saveAsHtml("./ARTICLE/2017-10-16_TEST.html")
def transformAllArticles():
    fileNameList=os.listdir('ARTICLE')
    for each in fileNameList:
        if each.endswith(".md"):
            newFileName = each.strip('.md')+"__.html"
            tran=transformer()
            tran.loadMarkdown("ARTICLE/" + each)
            tran.transformAll()
            tran.saveAsHtml("ARTICLE/"+newFileName)
transformAllArticles()
    
