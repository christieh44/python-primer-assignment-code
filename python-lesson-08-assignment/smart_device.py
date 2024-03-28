class SmartDevice:

    def __init__(self, model_number, brand, screen_size, app_list=[]):
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print("\nThis is SmartDevice " + str(self.model_number) + " from " + self.brand + ". It has a screen size of " + str(self.screen_size) + " inches.")


#If not already in app_list, app_name is installed
    def install_app(self, app_name="Demo App"):
        if(app_name not in self.app_list):            
            print(f"\nInstalling {app_name}...")
            self.app_list.append(app_name)
            return self.app_list
        
        else:
            print(f"\n{app_name} is already installed")
        
#deletes app specified
    def delete_app(self, app_name):
        print(f"\nDeleting {app_name}...")
        self.app_list.remove(app_name)
        return self.app_list

device_a = SmartDevice(12341234, 'CLG', 5.7)
device_a.report()

print("\n--Let's install some apps--")

#Install app 'Python Dojo'
device_a.install_app("Python Dojo")
print("The apps installed on this device are: " + str(device_a.app_list) + "\n")


#Install default app
print("\n--Let's install the default app--")

device_a.install_app()
print("The apps installed on this device are: " + str(device_a.app_list) + "\n")


#Install default app again
print("\n--Let's install the default app again--")

device_a.install_app()
print("The apps installed on this device are: " + str(device_a.app_list) + "\n")


#Delete 'Demo App' 
print("\n--Now delete the default app--")

device_a.delete_app("Demo App")
print("The apps installed on this device are: " + str(device_a.app_list) + "\n")

