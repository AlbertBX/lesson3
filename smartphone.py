class Smartphone:
    def __init__(self, phone_brand, phone_model, subscriber_number):
        self.phone_brand = phone_brand
        self.phone_model = phone_model
        self.subscriber_number= subscriber_number

    def get_phone_brand(self):
        return self.phone_brand
    
    def get_phone_model(self):
        return self.phone_model
    
    def get_subscriber_number(self):
        return self.subscriber_number
    
    def get_smartphone_info(self):
        return f"{self.phone_brand}, {self.phone_model}, {self.subscriber_number}"