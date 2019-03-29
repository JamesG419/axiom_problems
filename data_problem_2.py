#Write a generic function to compute various scenarios for the following optimization problem: A farmer owns X acres of land. 
# She profits P1 dollars per acre of corn and P2 dollars per acre of oats. Her team has Y hours of labor available. 
# The corn takes H1 hours of labor per acre and oats require H2 hours of labor per acre. 
# How many acres of each can be planted to maximize profits?
#Test the function for the following cases:
#a) X = 240, Y = 320, P1 = $40, P2 = $30, H1 = 2, H2 = 1
#b) X = 300, Y = 380, P1 = $70, P2 = $45, H1 = 3, H2 = 1
#c) X = 180, Y = 420, P1 = $65, P2 = $55, H1 = 3, H2 = 2

from scipy.optimize import linprog

def createMatrix(X,Y,p1,p2,h1,h2):
    c = [-p1,-p2]
    A = [[1,1],[h1,h2]]
    b = [X,Y]
    
    return [c,A,b]

def optimizeProblem(c,A,b):

    result = linprog(c,A,b)
    acres = result.get('x')

    print(str(acres[0]) + ' acres of corn')
    print(str(acres[1]) + ' acres of oats')
    print('')

x = [240.,300.,180.]
y = [320.,380.,420.]
p1 = [40.,70.,650.]
p2 = [30.,45.,55.]
h1 = [2.,3.,3.]
h2 = [1.,1.,2.]

for i in range(len(x)):
    setup = createMatrix(x[i],y[i],p1[i],p2[i],h1[i],h2[i])
    optimizeProblem(setup[0],setup[1],setup[2])