#Lucca

class Parachute():
    def parachute(self, check):
        parachute1 = """
     _____    
    /_____\\
    \     /
     \   /
      😅 

        """
        parachute2 = """
      
    /_____\\
    \     /
     \   /
      😨     
        
        """

        parachute3 = """
        
     _____
    \     /
     \   /
      😖        
        

        """

        parachute4 = """
        
    
     \   /
      😵   

        
        """

        parachute5 = """
        
    
      👻   
        
        
        """
        if check == 1:
            return parachute1 
        elif check == 2:
            return parachute2
        elif check == 3:
            return parachute3
        elif check == 4:
            return parachute4
        elif check == 5:
            return parachute5