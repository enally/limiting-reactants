import re

molecular_dictionary ={
  "He":	4.002602,
  "Li":	6.941,
  "Be":	9.012182,
  "Ne":	20.1797,
  "Na":	22.989768,
  "Mg":	24.3050,
  "Al":	26.981539,
  "Si":	28.0855,
  "Cl":	35.4527,
  "Ar":	39.948,
  "K":	39.0983,
  "Ca":	40.078,
  "Sc":	44.955910,
  "Ti":	47.88,
  "V":	50.9415,
  "Cr":	51.9961,
  "Mn":	54.93805,
  "Fe":	55.847,
  "Co":	58.93320,
  "Ni":	58.6934,
  "Cu":	63.546,
  "Zn":	65.39,
  "Ga":	69.723,
  "Ge":	72.61,
  "As":	74.92159,
  "Se":	78.96,
  "Br":	79.904,
  "Kr":	83.80,
  "Rb":	85.4678,
  "Sr":	87.62,
  "Y":	88.90585,
  "Zr":	91.224,
  "Nb":	92.90638,
  "Mo":	95.94,
  "Tc":	98,
  "Ru":	101.07,
  "Rh":	102.90550,
  "Pd":	106.42,
  "Ag":	107.8682,
  "Cd":	112.411,
  "In":	114.82,
  "Sn":	118.710,
  "Sb":	121.757,
  "Te":	127.60,
  "Xe":	131.29,
  "Cs":	132.90543,
  "Ba":	137.327,
  "La":	138.9055,
  "Ce":	140.115,
  "Pr":	140.90765,
  "Nd":	144.24,
  "Pm":	145,
  "Sm":	150.36,
  "Eu":	151.965,
  "Gd":	157.25,
  "Tb":	158.92534,
  "Dy":	162.50,
  "Ho":	164.93032,
  "Er":	167.26,
  "Tm":	168.93421,
  "Yb":	173.04,
  "Lu":	174.967,
  "Hf":	178.49,
  "Ta":	180.9479,
  "W":	183.85,
  "Re":	186.207,
  "Os":	190.2,
  "Ir":	192.22,
  "Pt":	195.08,
  "Au":	196.96654,
  "Hg":	200.59,
  "Tl":	204.3833,
  "Pb":	207.2,
  "Bi":	208.98037,
  "Po":	209,
  "At":	210,
  "Rn":	222,
  "Fr":	223,
  "Ra":	226.0254,
  "Ac":	227,
  "Th":	232.0381,
  "Pa":	213.0359,
  "U":	238.0289,
  "Np":	237.0482,
  "Pu":	244,
  "Am":	243,
  "Cm":	247,
  "Bk":	247,
  "Cf":	251,
  "Es":	252,
  "Fm":	257,
  "Md":	258,
  "No":	259,
  "Lr":	260,
  "Rf":	261,
  "Db":	262,
  "Sg":	263,
  "Bh":	262,
  "Hs":	265,
  "Mt":	266,
  "N": 14.00674,
  "B": 10.811,
  "C": 12.011,
  "O": 15.9994,
  "F": 18.9984032,
  "I": 126.90447,
  "S": 32.066,
  "P": 30.973762,
  "H":	1.00794,
}


print '\nPlease Print Molecular Formulas with correct cases e.g CH3, NaCl\n'


class Compound:
    def __init__(self):
        self.molecular_weight= 0
        self.formula = raw_input('Enter compound iupac name: ')
        self.stociometric = input('Enter stociometric value of compound in equation: ')
        self.mw_calc()
    def mw_calc(self):
        alterable_formula = self.formula
        
        #### Seperate all bracketed groups from formula
        RegExValue = re.compile(r"(\()(\w*)(\))(\d*)",re.I)
        myMatches = RegExValue.findall(self.formula)

        #### Add bracketed groups into formula again, removing original entries
        for i in myMatches:
            for j in range(int(i[3])):
                alterable_formula = alterable_formula + i[1]
            alterable_formula = alterable_formula.replace(i[0] + i[1] + i[2] + i[3], '')
        formula_list = list(alterable_formula)

        #### Match letters to corresponding dictionary values
        #### loop through each letter and add value to answer variable
        for i,j in enumerate(formula_list):
            if j.isdigit() == True:
                for m in range(int(j)):
                    self.molecular_weight+= molecular_dictionary[formula_list[i-1]]
                
            else:
                if j in molecular_dictionary:
                    self.molecular_weight+= molecular_dictionary[j]


class Reactant(Compound):
    def __init__(self):
        Compound.__init__(self)
        self.weight = input('Enter amount of compound used in grams: ')
        self.moles = self.weight / self.molecular_weight

        
class Product(Compound):
    def __init__(self):
        Compound.__init__(self)
    def calculation(self, name1, name2):
        self.outcome1 = (name1.weight * (1/name1.molecular_weight) * (name1.stociometric / self.stociometric) * (self.molecular_weight))
        self.outcome2 = (name2.weight * (1/name2.molecular_weight) * (name2.stociometric / self.stociometric) * (self.molecular_weight))
        if self.outcome1 < self.outcome2:
            print name1.formula + ' is the limiting reagent'
            self.theoretical_yield = (name1.weight * (1/name1.molecular_weight) * (self.stociometric/name1.stociometric) * (self.molecular_weight))
            print 'Theoretical Yield = ' + str(self.theoretical_yield) + 'g ' + self.formula
        elif self.outcome1 > self.outcome2:
            print name2.formula + ' is the limiting reagent'
            self.theoretical_yield = (name2.weight * (1/name2.molecular_weight) * (self.stociometric/name2.stociometric) * (self.molecular_weight))
            print 'Theoretical Yield = ' + str(self.theoretical_yield) + 'g ' + self.formula

        else:
            print 'Reactants imbalanced'

        
def main():
    print 'Input Data for Reactant 1\n'
    compound1 = Reactant()
    print '\nInput Data for Reactant 2\n'
    compound2 = Reactant()
    print '\nInput Data for Product\n'
    product = Product()
    product.calculation(compound1, compound2)

if __name__ == "__main__":
    main()


