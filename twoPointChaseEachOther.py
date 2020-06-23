import matplotlib.pyplot as plt
for x in range(1,6):
	print(x)
	plt.clf()
	plt.plot([0,5-x],[3+x,x],'k:',marker='o')
	plt.axis([-2,10,0,10]) # make the axis constant
	plt.pause(1)
	
