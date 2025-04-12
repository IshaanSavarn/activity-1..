class Employee:

    # Initializing (Constructor)
    def __init__(self):
        print('Employee created.')

        # deleting (Destructor)
        def __del__(self):
            print('DEstructor called, Employee deleted.')

            obj= Employee()
            del obj
        
                    