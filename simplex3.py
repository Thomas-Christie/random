import math
from prettytable import PrettyTable

decision_variables = {1 : "X", 2 : "Y", 3 : "Z"}

class Simplex:

    def __init__(self, objective = 0, constraint_1 = 0, constraint_2 = 0):

        self.tableau = [objective, constraint_1, constraint_2]
        self.piv = 0
        self.negative = 0

    def pivot(self):
        most_neg = 0
        for key in decision_variables.keys():
            if self.tableau[-3][key] < most_neg:
                most_neg = self.tableau[-3][key]
                index = key
        self.piv = index
        #print(self.piv)

    def gen_tableau(self):
        rows = [1,2,3]
        ratios = []
        new_tableau = [[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0]]
        for constraint in range(1,3): #Check ratios to find pivot row
            ratio = 0
            if self.tableau[-constraint][self.piv] != 0:
                ratio = self.tableau[-constraint][-1]/self.tableau[-constraint][self.piv]
            if ratio > 0:
                ratios.append(ratio)
            else:
                ratios.append(math.inf)
        one_row = (ratios.index(min(ratios))) + 1
        rows.remove(one_row)
        new_row = []
        for num in self.tableau[-one_row]:
            #print("One row {}".format(one_row))
            new_num = num/self.tableau[-one_row][self.piv]
            new_row.append(new_num)
        new_tableau[-one_row] = new_row
        for row in rows:
            edited_row = []
            div = self.tableau[-row][self.piv]/self.tableau[-one_row][self.piv]
            for num in range(7):
                edited_row.append(self.tableau[-row][num]-(div*self.tableau[-one_row][num]))
            new_tableau[-row] = edited_row
        for row in new_tableau:
            self.tableau.append(row)

    def run(self):
        run = True
        while run:
            self.pivot()
            self.gen_tableau()
            run = False
            for key in decision_variables.keys(): #Checks to see if x or y in objective function is negative to see if another iteration is necessary
                if self.tableau[-3][key] < 0 and (self.tableau[-2][key] > 0 or self.tableau[-1][key] > 0):
                    run = True

def main():
    #Arrays take the form: [P, x, y, z, s1, s2, V]
    print("Please input the coefficients for the Objective Function: ")
    ox = float(input("X: "))
    oy = float(input("Y: "))
    oz = float(input("Z: "))
    objective = [1, -ox, -oy, -oz, 0, 0, 0]
    print("Please input the coefficients for the First Constraint: ")
    c1x = float(input("X: "))
    c1y = float(input("Y: "))
    c1z = float(input("Z: "))
    c1 = float(input("Constraint value: "))
    constraint_1 = [0, c1x, c1y, c1z, 1, 0, c1]
    print("Please input the coefficients for the Second Constraint: ")
    c2x = float(input("X: "))
    c2y = float(input("Y: "))
    c2z = float(input("Z: "))
    c2 = float(input("Constraint value: "))
    constraint_2 = [0, c2x, c2y, c2z, 0, 1, c2]
    simplex = Simplex(objective, constraint_1, constraint_2)
    simplex.run()
    x = PrettyTable()
    x.field_names = ["P", "x", "y", "z", "s1", "s2", "V"]
    for each in simplex.tableau:
        #print(each)
        x.add_row(each)
    print(x)

if __name__ == "__main__":
    main()
