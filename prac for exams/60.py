class ListManager:
    def __init__(self):
        self.my_list=[]
    
    def append_element(self,element):
        self.my_list.append(element)
        print(f"Element {element} appended to the list.")
    
    def delete_element(self,element):
        if element in self.my_list:
            self.my_list.remove(element)
            print("removed")
        else:
            print("element not there")
    
    def display_list(self):
        for element in self.my_list:
            print(element)


newlist= ListManager()
newlist.append_element(1)
newlist.append_element(3)
newlist.delete_element(1)
newlist.display_list()