import pygal

piechart = pygal.Pie()
piechart.title='Favourite Technologies'
piechart.add('Wordpress',6)
piechart.add('Drupal',3)
piechart.add('python',1)
piechart.add('php',9)
#piechart.add('java',7)
piechart.render()

barchart=pygal.Bar()
barchart.title='Favourite pets'
barchart.add('Dog',5)
barchart.add('Cat',8)
barchart.add('Hamster',3)
barchart.add('Fish',2)
barchart.add('tiger',3)
barchart.render()

barchart2=pygal.Bar()
barchart2.title='barchat Data Taken From The txt File'
file=open('pets.txt','r')
for line in file.read().splitlines():
  if line:
    label, value=line.split(' ')
    barchart2.add(label,int(value))
file.close()
barchart2.render()

piechart2=pygal.Pie()
piechart2.title='pic chart data taken from the txt' 
file=open('chart.txt','r')
for line in file.read().splitlines():
  if line:
    label,value=line.split(' ')
    piechart2.add(label,int(value))
file.close()
piechart2.render()
