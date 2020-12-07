import csv
import pickle
import copy
import os

class Table:
    table_name = "TODO"
    table = {}
    types = {}

    def __init__(self, *filepath,name = None, table=None, type_check=False, delimiter_csv=';'):
        if name:
            self.table_name = name
        if table:
            self.table = table
            return

        for filename in filepath:
            if not os.path.exists(filename):
                raise FileNotFoundError
            if '.csv' or '.txt' in filename:
                with open(filename) as f_obj:
                    reader = csv.DictReader(f_obj, delimiter=delimiter_csv)
                    for line in reader:
                        for name in line:
                            try:
                                bool(self.table[name])
                            except:
                                self.table[name] = []
                            self.table[name].append(line[name])
            elif '.pickle' in filename:
                with open(filename, 'rb') as f_obj:
                    unpickler = pickle.Unpickler(f_obj)
                    self.table = unpickler.load()
            else:
                raise Exception('Unknown file extension')
        self.__complete_table()
        print('Imported table:\n', self.table)
        if type_check:
            self.type_research()
            self.set_types()
            print("Imported tables types: ", self.types)

    def __str__(self):
        return str(self.table)
    
    def __get_key_by_index(self,index):
        i=0
        for k in self.table.keys():
            if index == i:
                return k
            i+=1
        raise Exception(f"Not accesable index {index}")

    def __complete_table(self):
        maximum = max([len(self.table[n]) for n in self.table.keys()])
        for key in self.table.keys():
            if len(self.table[key]) < maximum:
                for _ in range(maximum - len(self.table[key])):
                    self.table[key].append("nill")
        for key in self.table.keys():
            for index,item in enumerate(self.table[key]):
                if item == "" or item == None:
                    self.table[key][index] = "nill"

    
    def set_types(self, types=None):
        if types:
            self.types = types
        for key in self.table.keys():
            pack = []
            for i in self.table[key]:
                
                if self.types[key] == "int":
                    try:
                        if i == "nill":
                            pack.append("nill")
                        else:
                            if i == "True":
                                pack.append(1)
                            elif i == "False":
                                pack.append(0)
                            else:
                                pack.append(int(i))
                    except:
                        print(f"Неудачная конвертация значения {i} в тип {self.types[key]}, записываем в виде строки...")
                        pack.append(str(i))

                elif self.types[key] == "float":
                    try:
                        if i == "nill":
                            pack.append("nill")
                        else:
                            pack.append(float(i))
                    except:
                        print(f"Неудачная конвертация значения {i} в тип {self.types[key]}, записываем в виде строки...")
                        pack.append(str(i))
                
                elif self.types[key] == "bool":
                    try:
                        if i == "nill":
                            pack.append("nill")
                        else:
                            pack.append('True' if i == "True" or i==1 else 'False')
                    except:
                        print(f"Неудачная конвертация значения {i} в тип {self.types[key]}, записываем в виде строки...")
                        pack.append(str(i))
                else:
                    if i == "nill":
                            pack.append("nill")
                    else:
                        pack.append(str(i))    
            self.table[key] = pack
   
    def type_research(self):
        for key in self.table.keys():
            try:
                buf = int(self.table.get(key)[0])
            except:
                try:
                    buf = float(self.table.get(key)[0])
                except:
                    if self.table[key][0] == "True" or self.table[key][0] == "False":
                        buf = True
                    else:
                        buf = str(self.table.get(key)[0])
            self.types[key] = "bool" if (type(buf)) == bool else "str" if (type(buf)) == str else "int" if (type(buf)) == int else "float"
        return self.types
    
    def print_table(self):
        print(f"Таблица по имени: {self.table_name}")
        print("━"*20,"\n┌─", end = "")
        for key in self.table.keys():
            print("{0:^10}".format(key),end = "─")
        print("┐")

        for item in range(min([len(self.table[n]) for n in self.table.keys()])):
            print("├", end = "─")
            for k in self.table.keys():
                print("{0:^10}".format(self.table[k][item] if self.table[k][item] != "nill" else ""),end = "─")
            print("┤")
        print(f"└{'─'*(10*len(self.table.keys()))}{'─'*(len(self.table.keys())+1)}┘")
            
    def get_value(self,index=0,column=None):
        if column:
            return self.table[column][index] if self.table[column][index] != "nill" else None
        return [self.table[key][index] if self.table[key][index] != "nill" else None for key in self.table.keys()]

    def Table_to_List (self, column = None):
        keys = self.table.keys()
        self.__complete_table()
        minimum = min([len(self.table[n]) for n in keys])
        pack = []
        for i in range(minimum):
            pack.append([self.table[k][i] if self.table[k][i] != "nill" else None for k in keys])
        return pack

    def get_rows_by_number(self, start, stop = None, copy_table=False):
        allrows = self.Table_to_List()
        pack = []
        for i in range(start-1, stop) if stop else range(start-1,len(allrows)):
            pack.append(allrows[i])
        pack = list_to_Table(self.table.keys(),pack)
        if copy_table:
            pack = copy.deepcopy(pack)
        return Table(table = pack)
    
    def get_rows_by_index(self,*index, copy_table=False):
        allrows = self.Table_to_List()
        pack = []
        for i in index:
            pack.append(allrows[i])
        pack = list_to_Table(self.table.keys(),pack)
        if copy_table:
            pack = copy.deepcopy(pack) 
        return Table(table = pack)
    
    def save_table(self, *name, max_Lines = None, newline=''):
        List = self.Table_to_List()
        i=0
        if max_Lines:
            for n in name:
                lines = max_Lines
                with open(n, "w") as f_obj:
                    writer = csv.writer(f_obj, delimiter = ";")
                    writer.writerow(self.table.keys())
                    for line in List[i*max_Lines:]:
                        writer.writerow(line)
                        lines -=1
                        if lines <= 0:
                            break
                i+=1
            while True:
                if i+(max_Lines*i) > len(List):
                    return 0 
                lines = max_Lines
                fname = name[0].replace(".csv",f"{i}.csv")
                with open(fname, "w") as f_obj:
                    writer = csv.writer(f_obj, delimiter = ";")
                    writer.writerow(self.table.keys())
                    for line in List[i*max_Lines:]:
                        if i+(max_Lines*i) < len(List):
                            writer.writerow(line)
                            lines -=1
                            if lines <= 0:
                                break
                        else:
                            return 0
                i+=1
        else:
            with open (name[0], "w") as f_obj:
                writer = csv.writer(f_obj, delimiter=';')
                writer.writerow(self.table.keys())
                for line in self.Table_to_List():
                    writer.writerow(line)

    
    def set_values(self,*value,row = 0, column = 0):
        if len(value) == 1:
            if isinteger(column):
                self.table[self.__get_key_by_index(column)][row] = list(value)[0]
            else:
                self.table[column][row] = list(value)[0]
        else:
            if isinteger(column):
                self.table[self.__get_key_by_index(column)] = list(value)
            else:
                self.table[column] = list(value)
            self.__complete_table()
        self.set_types()
    
    def get_column_types(self):
        return str(self.types)
    
    def set_column_types(self, types_dict, by_number=True):
        if by_number:
            for key in types_dict.keys():
                self.types[self.__get_key_by_index(key)] = types_dict[key]
        else:
            self.types = types_dict
        self.set_types()
    
    def concat(self,table):
        pack = {}
        for key in table.table.keys():
            pack[key] = []
        for key in self.table.keys():
            pack[key] = []
        for key in self.table.keys():
            for item in self.table[key]:
                pack[key].append(item)
        for key in table.table.keys():
            for item in table.table[key]:
                pack[key].append(item)
        self.table = pack

    def split (self,row_number):
        pack1,pack2 = {},{}
        for key in self.table.keys():
            pack1[key] = []
            pack2[key] = []
            for i in range(len(self.table[key])):
                if i <row_number:
                    pack1[key].append(self.table[key][i])
                else:
                    pack2[key].append(self.table[key][i])
        return Table(table=pack1),Table(table=pack2)
        

def list_to_Table(keys, List):
    pack = {}
    i = 0
    for key in keys: 
        pack[key] = []
        for l in List:
            pack[key].append(l[i])
        i+=1
    return pack

def isinteger(key):
    try:
        int(key)
        return True
    except:
        return False

def test():
    t = Table('C:/Users/ankluz/Desktop/Prakt/3KR/rollOut.csv', 'C:/Users/ankluz/Desktop/Prakt/3KR/rollOut1.csv',type_check = True)
    print(t.get_value(3))
    print(t.get_value(3,"time"))
    print(t.Table_to_List())
    print(t.get_rows_by_number(5,6,True))
    print(t.get_rows_by_index(2,4,1,3))
    t.print_table()
    t.set_values(23,4,21,61,32,55, row = 0,column = 0)
    print(t)
    t.print_table()
    print(t.get_column_types())
    t.set_column_types({0:"int",1:"str",2:"float",3:"bool"})
    print(t.get_column_types())
    print(t)
    t.save_table("C:/Users/ankluz/Desktop/Prakt/3KR/roller.csv")
    g,a = t.split(2)
    g.print_table()
    a.print_table()
    g.concat(a)
    g.print_table()

if __name__ == '__main__':
    test()