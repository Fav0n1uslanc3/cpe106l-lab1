class Logger:
    _instance = None
    
    def __new___(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            
        return cls._instance