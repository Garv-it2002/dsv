from bokeh.plotting import figure, show
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure()
p.line(x, y)
p.circle(x, y)

for i,j in zip(x,y):
    p.text(i,j,text = ["Point"])

show(p)
