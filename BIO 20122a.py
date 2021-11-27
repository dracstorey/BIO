
railway = []

class junction():

    def __init__(self,letter, CL, CR, S, pt_type):
        self.pt_letter = letter
        self.pt_CL = CL
        self.pt_CR = CR
        self.pt_S = S
        self.pt_type = pt_type
    # end of constructor function

straights = ["D","C","B","A","A","A","B","B","C","C","D","D","U","U","V","V","W","W","X","X","V","U","X","W"]

left_curves = ["E","G","I","K","M","N","O","P","Q","R","S","T","L","E","F","G","H","I","J","K","M","O","Q","X"]

right_curves = ["F","H","J","L","N","O","P","Q","R","S","T","M","E","F","G","H","I","J","K","L","N","P","R","T"]

for count in range (0, 23):
    r = junction(chr(count+64),left_curves[count],right_curves[count],straights[count],"left")
    railway.append(r)
    
print (railway[0].pt_S)