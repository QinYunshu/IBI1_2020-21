import xml.dom.minidom
from xml.dom.minidom import parse
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")

#DNA
dictionary={}#define a dictionary to connect the father node and child node.
for term in terms:
    id_element=term.getElementsByTagName('id')#extract the element <id>GO:XXXXXXX</id>
    id_data=id_element[0].childNodes[0].data#extract the data in the element 'GO:XXXXXX'
    dictionary[id_data]=[]#define the array
for term in terms:
    id_element = term.getElementsByTagName('id')
    id_data = id_element[0].childNodes[0].data
    is_a_element = term.getElementsByTagName('is_a')#there may be more than one 'is_a's in one term
    for i in is_a_element:
        is_a_data = i.childNodes[0].data
        dictionary[is_a_data].append(id_data)#connecting 'is_a'(fathernode) with 'id'(childnode) in the dictionary]

def number_(c):#define a function, where every child node of the selected term in the second funtion will be found out
    for i in range(len(c)):
        if c[i] not in list_:
            list_.append(c[i])#add every target node to the list
            number_(dictionary[c[i]])
    return len(list_)

#DNA
list_=[]
for term in terms:  # take turn to exam the terms
    defstr_element = term.getElementsByTagName('defstr')[0]
    defstr_data = defstr_element.childNodes[0].data
    if 'DNA' in defstr_data:  # extract the terms which have the target word in the 'defstr'
        id_ = term.getElementsByTagName('id')[0].childNodes[0].data  # extract data of 'id's of the selected terms
        if dictionary[id_] != []:  # meaning the corresponding term has child node
            c = dictionary[id_]  # c represents the child node(s) of the term
            n = number_(c)  # the function defined above
print('The childnode number of  DNA  is ' + str(n))
D=n
#8651

#repeat the process on  RNA, protein and carbohydrate
#RNA
list_=[]
for term in terms:
    defstr_element = term.getElementsByTagName('defstr')[0]
    defstr_data = defstr_element.childNodes[0].data
    if 'RNA' in defstr_data:
        id_ = term.getElementsByTagName('id')[0].childNodes[0].data
        if dictionary[id_] != []:
            c = dictionary[id_]
            n = number_(c)
print('The childnode number of  RNA  is ' + str(n))
R=n
#11004

#protein
list_=[]
for term in terms:
    defstr_element = term.getElementsByTagName('defstr')[0]
    defstr_data = defstr_element.childNodes[0].data
    if 'protein' in defstr_data:
        id_ = term.getElementsByTagName('id')[0].childNodes[0].data
        if dictionary[id_] != []:
            c = dictionary[id_]
            n = number_(c)
print('The childnode number of  protein  is ' + str(n))
P=n
#33459

#carbohydrate
list_=[]
for term in terms:
    defstr_element = term.getElementsByTagName('defstr')[0]
    defstr_data = defstr_element.childNodes[0].data
    if 'carbohydrate' in defstr_data:
        id_ = term.getElementsByTagName('id')[0].childNodes[0].data
        if dictionary[id_] != []:
            c = dictionary[id_]
            n = number_(c)
print('The childnode number of  carbohydrate  is ' + str(n))
C=n
#4879

#piechart
import matplotlib.pyplot as plt
frequency={'DNA':str(D),'RNA':str(R),'protein':str(P),'carbohydrate':str(C)}
labels='DNA','RNA','protein','carbohydrate'
sizes=[frequency['DNA'],frequency['RNA'],frequency['protein'],frequency['carbohydrate']]
explode=(0,0,0,0)
plt.title("The number of childNodes associated with each terms")
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()