class Category:
    category_name=""
    positive_balance=0
    negative_balance=0
    ledger=[]
    
    def __init__(self,name):
        self.category_name=name
        self.positive_balance=0
        self.negative_balance=0
        self.ledger=[]
    def get_balance(self):
        return self.positive_balance-self.negative_balance
    def check_funds(self,amount):
        total=self.get_balance()
        if total>=amount:
            return True
        else:
            return False
    def deposit(self,amount,description=""):
        self.positive_balance+=amount
        detail={"amount": amount, "description": description}
        self.ledger.append(detail)
    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.negative_balance+=amount
            detail={"amount": -amount, "description": description}
            self.ledger.append(detail)
            return True
        else:
            return False
    def transfer(self,amount,other_category):
        if self.check_funds(amount):
            self.negative_balance+=amount
            detail={"amount": -amount, "description": "Transfer to "+other_category.category_name}
            self.ledger.append(detail)
            other_category.deposit(amount,"Transfer from "+self.category_name)
            return True
        else:
            return False
    def __str__(self):
        string_obj=""
        string_obj+=self.category_name.center(30,'*')+"\n"
        for value in self.ledger:
            desc_23=value["description"]
            string_obj+=desc_23[:23].ljust(23)
            string_obj+='{:.02f}'.format(value["amount"]).rjust(7)+"\n"
        
        string_obj+="Total: "+'{:.02f}'.format(self.get_balance())
        return string_obj
        
def create_spend_chart(categories):
    negative_total=0
    max_category_len=0
    for categorie in categories:
        negative_total+=categorie.negative_balance
    category_percent=[]
    for categorie in categories:
        first_degit=str(categorie.negative_balance/negative_total*10)[:1]
        category_percent_dict={"category":categorie.category_name,"percent":int(first_degit)*10}
        category_percent.append(category_percent_dict)
        if max_category_len<len(categorie.category_name):
            max_category_len=len(categorie.category_name)
    
    answer="Percentage spent by category\n"
    max_list_index=len(category_percent)
    for i in range(100,-10,-10):
        answer+=str(i).rjust(3)+"|"
        count=0
        while count<max_list_index:
            category_dict=category_percent[count]
            if category_dict["percent"]>=i:
                answer+=" "+"o"
            else:
                answer+="  "
            answer+=" "
            count+=1
        answer+=" "+"\n"
    
    answer+="    "
    for i in range(0,max_list_index,1):
        answer+="-"*3
    answer+="-\n"
    
    row_count=0
    while row_count<max_category_len:
        answer+="    "
        column_count=0
        while column_count<max_list_index:
            dict=category_percent[column_count]
            if row_count<len(dict["category"]):
                answer+=" "+dict["category"][row_count]+" "
            else:
                answer+="   "
            column_count+=1
        if row_count==(max_category_len-1):
            answer+=" "
        else:
            answer+=" \n"
        row_count+=1
    return answer