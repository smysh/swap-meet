class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []
        
        if not isinstance(self.inventory, list):
            raise TypeError("Inventory should be a list type object")
            
    def add(self, item):
        if not item:
            return None
        self.inventory.append(item) 
        return item

    def remove(self, item):
        if item not in self.inventory:
            return None
        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        if not id or not self.inventory:
            return None
        return next((item for item in self.inventory if item.id == id), None)

    def swap_items(self, other_vendor, my_item, their_item):
        if not my_item or not their_item:
            return False
        if not self.inventory or not other_vendor.inventory:
            return False
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.add(other_vendor.remove(their_item))
        other_vendor.add(self.remove(my_item))
        return True

    def swap_first_item(self, other_vendor):
        if not self or not other_vendor:
            return False
        if not self.inventory or not other_vendor.inventory:
            return False
        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True
    
    def get_by_category(self, category):
        if not category or not self.inventory:
            return None
        return [item for item in self.inventory if item.get_category() == category]

    def get_best_by_category(self, category):
        if not category:
            return None
        category_items = self.get_by_category(category)
        if not category_items:
            return None
        return max(category_items, key=lambda item: item.condition)

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not self.inventory or not other_vendor.inventory:
            return False
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        if not my_best_item or not their_best_item:
            return False
        return self.swap_items(other_vendor, my_best_item, their_best_item)
    
    def display_inventory(self, category=None):
        if not self.inventory:
            print("No inventory to display.")
            return 
        items = self.get_by_category(category) if category else self.inventory
        if items:
            for index, item in enumerate(items):
                print(f"{index+1}. {str(item)}")
        else:
            print("No inventory to display.")
    
    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        if not self.inventory or not other_vendor.inventory:
            return False
        if (not self.get_by_id(my_item_id)) or (not other_vendor.get_by_id(their_item_id)):
            return False
        return self.swap_items(other_vendor, self.get_by_id(my_item_id), other_vendor.get_by_id(their_item_id))

    def choose_and_swap_items(self, other_vendor, category=None):
        if not self.inventory or not other_vendor.inventory:
            print("No inventory to display.")
            return False
        print("Inventory 1:\n")
        self.display_inventory(category)
        print("Inventory 2:\n")
        other_vendor.display_inventory(category)
        my_item_id = int(input(f"Enter the item id from first inventory to swap: "))
        their_item_id = int(input(f"Enter the item id from second inventory to swap: "))
        return self.swap_by_id(other_vendor, my_item_id, their_item_id)

