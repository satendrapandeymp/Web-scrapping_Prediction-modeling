import urllib2, time, sys
from bs4 import BeautifulSoup as Soup

reload(sys)
sys.setdefaultencoding("utf-8")

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]

File_name = "Data.csv"
f = open(File_name, "w+")

arr = ['Processor', 'RAM', 'Operating System', 'Display']
f.write('Name, Processor, RAM, Operating System, Display, Price \n')

for i in range(20):

    seed = "https://www.flipkart.com/search?q=laptops&page="+ str(i+1)
    response = opener.open(seed)
    Page_Html = response.read()
    Parsed_html = Soup(Page_Html, "html.parser")
    
    Containers = Parsed_html.findAll("div", {"class":"col _2-gKeQ"})
    
    for Container in Containers:
        Title = Container.findAll('div', {"class":"_3wU53n"})[0].text
        price_con = Container.findAll("div", {"class":"_1vC4OE _2rQ-NK"})[0]
        price_con = str(price_con)
        test = price_con.split(',')
        if len(test) == 2:
            pre = test[0].split("-->")
            pre = pre[len(pre)-1]
            price = pre + test[1][:3]
        f.write(Title + ',')
        Spec_containers = Container.findAll('li', {"class":"tVe95H"})
        
        # For Specs
        count = 0
        for Specs in Spec_containers:
            sp = Specs.text
            if arr[count] in sp:
                count += 1
                f.write(sp + ',')
            if count == 4:
                break
        f.write(price + ',')
        f.write("\n")
    
    if len(Containers) == 0 :
        break
    print "Results are availabe till page : " + str(i+1)
    
f.close()
