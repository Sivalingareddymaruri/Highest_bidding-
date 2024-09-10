def bidding():
    while(True):
        dictionary={}
        #print("welcome to the secret auction program")
        name=input("what is your name ?")
        bid=int(input("what's your bid"))
        #print(name)
        #print(bid)
        dictionary.update({name:bid})
        x=input("Are there any other bidders ? if there type yes or else no ").lower()
        if(x=="no"):
            break
        max_key = None
        max_value = float('-inf')  
        for key, value in dictionary.items():
            if value > max_value:
                max_value = value
                max_key = key    
    print(f"the winer is {max_key} with a bid of {max_value}")
bidding()
        
        
    
    