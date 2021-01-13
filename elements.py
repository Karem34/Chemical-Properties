class Element():

    def __init__(self, iden: int):
        self.elements_symbol = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
        self.elements_full = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"]
        self.iden = iden

        if isinstance(iden, int):
            atn = iden
        elif isinstance(iden, str):
            self.iden = iden.capitalize()
            atn = self.__get_electron()
        self.atomic_number = atn
        self.number_of_electrons = atn
        self.number_of_protons = atn
        self.number_of_neutrons = atn
        self.name = self.__get_element()
        self.symbol = self.__get_symbol()
        self.electron_configuration = self.__electronConfig()
        
    def __electronConfig(self):
        elec = self.number_of_electrons
        elec_config = []
        sub_shells = [('s', 1), ('s', 2), ('p', 2), ('s', 3), ('p', 3), ('s', 4), ('d', 3), ('p', 4), ('s', 5), ('d', 4), ('p', 5), ('s', 6), ('f', 4), ('d', 5), ('p', 6), ('s', 7), ('f', 5), ('d', 6), ('p', 7)]
        orbitals = {'s': 1, 'p': 3, 'd': 5, 'f': 7}

        for i, n in sub_shells:
            m = orbitals.get(i)*2

            if elec >= m:
                
                elec_config.append(str(n) + i + str(m))
                elec -= m
            elif elec != 0:
                elec_config.append(str(n) + i + str(elec))
                break
            else:
                break
        return elec_config

    def __get_element(self):
        elec = self.number_of_electrons
        
        if elec <= 118 and elec > 0:            
            return self.elements_full[elec-1]

    def __get_symbol(self):
        elec = self.number_of_electrons
        if elec <= 118:  
            return self.elements_symbol[elec-1]

    def __get_electron(self):
        symbols = self.elements_symbol
        names = self.elements_full
        if self.iden in symbols:
            elec = self.elements_symbol.index(self.iden)
        elif self.iden in names:
            elec = self.elements_full.index(self.iden)
        else:
            
            return 
        return elec+1
