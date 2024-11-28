from smartphone import Smartphone
catalog = [
    Smartphone ("Nokia", 3110, 855544433),
    Smartphone ("Philips", "Xenium E2301", 844455522),
    Smartphone ("Samsung", "Galaxy S10", 833322211), 
    Smartphone ("Honor", "20i", 899966622),
    Smartphone ("LG", "KG376", 877711155)
]

for smartphone in catalog:
    print(f"{smartphone.phone_brand}-{smartphone.phone_model}-{smartphone.subscriber_number}")
