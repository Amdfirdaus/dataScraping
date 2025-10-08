from bs4 import BeautifulSoup
import os

html = """
<div> this is a  div </div>
<p> ini adalah matkul data scraping</p>
<div class='bold'> cihuuyy </div>

<div><ini adalah paragraf ke 1>
<div><ini adalah paragraf ke 2>
<div><ini adalah paragraf ke 3>

# <div id="d1" class = "wide">
#     <p id = 'p1'> ini addalah sintag paragra ke 1f</p>
#     <div><p>OK</p></div>
#     <img src = ""/>
#     <a id = "a1"></a>
# </div>

# <div id = "d1" class = "small">
#     <p id = 'p1'> ini addalah sintag paragraf ke 2</p>
#     <div><p>KO</p></div>
#     <img src = ""/>
#     <a id = "a1"></a>
# </div>
# """

html ="""
<div>jos1</div>
<div>jos2</div>
<div>jos3</div>
<div>jos4</div>
<div>jos5</div>
<div>jos6</div>
<div>jos7</div>
<div>jos8</div>
<div>jos9</div>
<div>jos10</div>
"""
soup = BeautifulSoup(html,"html.parser")

# print (soup.p.text)
# print(soup.div)
# print(soup.findAll("div"))
# print(soup.findAll("div")[1])

# print (soup.findAll("div",{'class':'bold'}))
# print (soup.findAll("p",{'id':'para'}))

# print(soup.find("div", {"class": "wide"}).findAll("p")[1])

print(soup.findAll("div")[1::2]) #cara 1

for d in soup.findAll("div")[1::2]: #cara 2
    print(d.text)
    

for index, div in enumerate (soup.findAll("div")): #cara 3
    if (index + 1 ) % 2 == 0:
        print(div.text)