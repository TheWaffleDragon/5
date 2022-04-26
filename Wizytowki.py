from faker import Faker


# class Card :
    
#     def __init__(self, first_name, last_name, company, job, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.company = company
#         self.job = job
#         self.email = email
    
#     def __repr__(self):
#         return f"First Name: {self.first_name}, Last Name: {self.last_name}, email: {self.email}"
#     def __str__(self):
#         return f"First Name: {self.first_name}, Last Name: {self.last_name}, email: {self.email}"
#     def contact(self):
#         return print(f"Kontaktuje sie z {self.first_name} {self.last_name}, {self.job} {self.email}")
#     @property
#     def label_lenght(self):
#         return len(self.first_name)+ len(self.last_name)+1
    
   
class BaseCard:
    def __init__(self, first_name, last_name,p_phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.p_phone = p_phone
        self.email = email
    def contact(self):
        return print(f"Wybieram numer {self.p_phone}  i dzwonię do {self.first_name} {self.last_name}")
    @property
    def label_lenght(self):
        return len(self.first_name)+ len(self.last_name)+1

class BusinessCard(BaseCard):
    def __init__(self, b_phone, company, job, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.b_phone = b_phone
        self.company = company
        self.job = job
    def contact(self):
        return print(f"Wybieram numer {self.b_phone}  i dzwonię do {self.first_name} {self.last_name}")
    @property
    def label_lenght(self):
        return len(self.first_name)+ len(self.last_name)+1

        
# def new_card():       
#     return Card(first_name =fake.first_name(), last_name =fake.last_name(), company =fake.company(), job =fake.job(), email =fake.email())

fake = Faker() 

def create_contacts(card_type,num):
    cards = []
    if card_type == 'BaseCard':
        for i in range(num):
            card = BaseCard(first_name = fake.first_name(), last_name = fake.last_name(), p_phone = fake.phone_number(), email = fake.email())
            cards.append(card)
    if card_type == 'BusinessCard':
        for i in range(num):
            card = BusinessCard(first_name = fake.first_name(), last_name = fake.last_name(), p_phone = fake.phone_number(), email = fake.email(), b_phone = fake.phone_number(), company = fake.company(), job = fake.job())
            #BusinessCard(first_name = fake.first_name(), last_name = fake.last_name(), p_phone = fake.phone_number(), email = fake.email())
            cards.append(card)
    return cards
        
    
x = create_contacts("BaseCard", 5)
y = create_contacts("BusinessCard", 7)
#%%      
x[0].contact()
print(x[0].label_lenght)
y[3].contact()
print(y[3].label_lenght)


# for i in range(10):
#     cards.append(new_card())
    
    
# by_first_name = sorted(cards, key = lambda card: card.first_name)           
# by_last_name = sorted(cards, key = lambda card: card.last_name)           
# by_email = sorted(cards, key = lambda card: card.email)

# n_card = new_card()
# n_card.contact()

# x=n_card.label_lenght

           
        
        
        
        