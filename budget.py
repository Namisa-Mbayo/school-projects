import re


class Budget:
    def __init__(self):
        self.ledger = {'Personal':200.0,'Clothes':161.0, 'Food':412.0, 'Entertainment':290.0}
        self.itemList = []


    def choose_category(self):
        instantiate_category = input("Choose the category you wish to add your objects into:\n(P)ersonal, (C)lothes, (F)ood, or (E)ntertainment: ")
        if instantiate_category.islower == True:
            raise ValueError("Input is not uppercase.")
        elif instantiate_category.upper == 'P'.upper:
            category_name = 'Personal'
            return category_name
        elif instantiate_category.upper == 'C'.upper:
            category_name = 'Clothes'
            return category_name
        elif instantiate_category.upper == 'F'.upper:
            category_name = 'Food'
            return category_name
        elif instantiate_category.upper == 'E'.upper:
            category_name = 'Entertainment'
            return category_name
        else:
            raise ValueError("Not acceptable input.")


    def choose_objects(self):
        self.itemList = []
        instantiate_objects = ''
        while instantiate_objects.upper != 'S'.upper:
            instantiate_objects = input("What object are you adding?\nType (S)top when done: ")
            self.itemList.append(instantiate_objects)
            print(f'What you have so far: {self.itemList}')
            continue
        
        self.itemList.pop(-1)
        return self.itemList

    def choose_action(self, cat_name):
        key_list = []
        for key in self.ledger.keys():
            key_list.append(key)

        for cat in key_list:
            if cat == cat_name:
                activity = input("Would you like (D)eposit or (W)ithdraw the items from your account?: ")
                if activity.upper == 'D'.upper:
                    self.deposit(self.itemList, cat_name, self.ledger[cat_name])
                elif activity.upper == 'W'.upper:
                    self.withdraw(self.itemList, cat_name, self.ledger[cat_name])
                elif activity.islower == True:
                    raise ValueError("Input is not uppercase.")
                else:
                    raise ValueError("Not acceptable input.")

    def deposit(self, item_list, key, value):
        #get cost of items
        for item in item_list:
            quanity = input(f'How much does {item} cost?: ')
            if re.search('\d+', quanity):
                total = lambda a, b : a + b
                total = total(value, float(quanity))
                value = round(total, 2)
                print(f'You have ${value} left in account')
                self.ledger.update({key:value})
            else: 
                raise ValueError(f"Input was not a number.") 

    def withdraw(self, item_list, key, value):
        #get cost of items
        for item in item_list:
            quanity = input(f'How much does {item} cost?: ')
            if re.search('\d+', quanity):
                total = lambda a, b : a - b
                total = total(value, float(quanity))
                if total < 0:
                    raise ValueError(f'Insufficient funds ${value} left in account.')
                else:
                    value = round(total, 2)
                    print(f'You have ${value} left in account')
                    self.ledger.update({key:value})
            else: 
                raise ValueError(f"Input was not a number.") 
   
    def repeatAction(self):
            go_again = input("Do you wish to add objects in a different category? [Y/N]: ")
            if go_again.upper == 'Y'.upper: 
                print(self.ledger)
            elif go_again.upper == 'N'.upper: 
                print(self.ledger)
                quit()
            else:
                raise ValueError("Not acceptable input.")