## Question 1.
# class StringUtility:
#     def forrmat_title(self, raw_test):
#         self.raw_test = raw_test
#         return raw_test.title()
        
# text1=StringUtility()
# print(text1.forrmat_title("python programming"))


    
# ##Question 2.
# class SmartDevice:
#     def __init__(self,device_name , batter_level):
#         self.device_name=device_name
#         self.batter_level=batter_level
#         print( f'Device {self.device_name} is boosted up' )
    
# D1=SmartDevice("motorola", 90)

# del D1
# print(D1)


##Question 3

# class Notification:
#     def send(self):
#         pass


# class SMSNotification(Notification):
#     def send(self):
#         super().send()
#         print("its hot out side try to stay in home ")

# msg=SMSNotification()
# msg.send()

##Question 4
class profile:
    def set_bio(self, text , links=None):
        self.text=text
        self.links=links

        print(f'Bio Text: {self.text}')

        if links is not None:
            print(f'links provided {self.links}')



    
# e1=profile()
# e1.set_bio("jay shree ram")

e2=profile()
e2.set_bio("jay shree ram ", ["http://google.com"])
