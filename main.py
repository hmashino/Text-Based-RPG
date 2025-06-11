# Option
def get_choice(options):
    while True:
        choice = input("Choice: ").strip().lower()
        if choice in options:
            return choice
        else:
            print(f"Invalid choice. Please select one of {', '.join(options)}.")
# Start the game
print("You are a Sky Engineer.  You are traveling around with a mysterious device and diary left behind by your father who once went missing. Your goal is to activate the ‘sealed gate’ that is your father's legacy and stop the collapse of the world.")
print("You called from the kingdom. Reports that his father's device has begun to reactivate.")
print("1) Go to investigate the device")
print("2) Examine my father's records first")

ans1 = get_choice(["1", "2"])

if ans1 == "1":
    print("Gather information in a neutral zone city")
    print("The inventor's daughter and the informant offer to provide information.")
    print("1) Trust the inventor's daughter and accompany her to investigate")
    print("2) Investigate on my own")
    
    ans2 = get_choice(["1", "2"])
    
    if ans2 == "1":
        print("Captured by rebel leader on Dark Island ")
        print("Rebel leader convinces you that you can end the oppression of the kingdom if you use the gate to gain power.")
        print("1) Turn and become the rebel leader's collaborator")
        print("2) Escape and inform the inventor's daughter")
        
        ans3 = get_choice(["1", "2"])
        
        if ans3 == "1":
            print("Reach the sealing device at the gate")
            print("1) Let it go out of control with the rebel leader")
            print("2) Trust the opinion of the inventor's daughter and stop it")
            
            ans4 = get_choice(["1", "2"])
            
            if ans4 == "1":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Rebel leader")
                print("2) Player")
                
                ans5 = get_choice(["1", "2"])
                
                if ans5 == "1":
                    print("They destroyed inequality through revolution by force.")
                elif ans5 == "2":
                    print("You live as “guardian of the sealed gate”.")
                    
            elif ans4 == "2":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Player")
                
                ans5 = get_choice(["1"])
                
                if ans5 == "1":
                    print("You live as “guardian of the sealed gate”.")
        
        elif ans3 == "2":
            print("Reach the sealing device at the gate")
            print("1) Trust the opinion of the inventor's daughter and stop it")
            print("2) Activate as my father planned")
            
            ans4 = get_choice(["1", "2"])
            
            if ans4 == "1":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Inventor's Daughter")
                print("2) Player")
                
                ans5 = get_choice(["1", "2"])
                
                if ans5 == "1":
                    print("Technology and reason for a stable future.")
                elif ans5 == "2":
                    print("You live as “guardian of the sealed gate”.")
            
            elif ans4 == "2":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Player")
                
                ans5 = get_choice(["1"])
                
                if ans5 == "1":
                    print("You live as “guardian of the sealed gate”.")
    
    elif ans2 == "2":
        print("Captured by rebel leader on Dark Island ")
        print("Rebel leader convinces you that you can end the oppression of the kingdom if you use the gate to gain power.")
        print("1) Turn and become the rebel leader's collaborator")
        print("2) Escape and inform the inventor's daughter")
        
        ans3 = get_choice(["1", "2"])
        if ans3 == "1":
            print("Reach the sealing device at the gate")
            print("1) Let it go out of control with the rebel leader")
            print("2) Shutting down the equipment")
            
            ans4 = get_choice(["1", "2"])
            
            if ans4 == "1":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Rebel leader")
                print("2) Player")
                
                ans5 = get_choice(["1", "2"])
                
                if ans5 == "1":
                    print("They destroyed inequality through revolution by force.")
                elif ans5 == "2":
                    print("You live as “guardian of the sealed gate”.")
                    
            elif ans4 == "2":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Player")
                
                ans5 = get_choice(["1"])
                
                if ans5 == "1":
                    print("You live as “guardian of the sealed gate”.")
        
        elif ans3 == "2":
            print("Reach the sealing device at the gate")
            print("1) Trust the opinion of the inventor's daughter and stop it")
            print("2) Activate as my father planned")
            
            ans4 = get_choice(["1", "2"])
            
            if ans4 == "1":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Inventor's Daughter")
                print("2) Player")
                
                ans5 = get_choice(["1", "2"])
                
                if ans5 == "1":
                    print("Technology and reason for a stable future.")
                elif ans5 == "2":
                    print("You live as “guardian of the sealed gate”.")
            
            elif ans4 == "2":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Player")
                
                ans5 = get_choice(["1", "2"])
                
                if ans5 == "1":
                    print("You live as “guardian of the sealed gate”.")
    


elif ans1 == "2":
    print("Gather information in a neutral zone city")
    print("The inventor's daughter and the informant offer to provide information.")
    print("1) Trust the inventor's daughter and accompany her to investigate")
    print("2) Investigate on my own")
    
    ans2 = get_choice(["1", "2"])
    
    if ans2 == "1":
        print("Captured by rebel leader on Dark Island ")
        print("Rebel leader convinces you that you can end the oppression of the kingdom if you use the gate to gain power.")
        print("1) Turn and become the rebel leader's collaborator")
        print("2) Escape and inform the inventor's daughter")
        
        ans3 = get_choice(["1", "2"])
        
        if ans3 == "1":
            print("Reach the sealing device at the gate")
            print("1) Let it go out of control with the rebel leader")
            print("2) Trust the opinion of the inventor's daughter and stop it")
            
            ans4 = get_choice(["1", "2"])
            
            if ans4 == "1":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Rebel leader")
                print("2) Player")
                
                ans5 = get_choice(["1", "2"])
                
                if ans5 == "1":
                    print("They destroyed inequality through revolution by force.")
                elif ans5 == "2":
                    print("You live as “guardian of the sealed gate”.")
                    
            elif ans4 == "2":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Player")
                
                ans5 = get_choice(["1"])
                
                if ans5 == "1":
                    print("You live as “guardian of the sealed gate”.")
        
        elif ans3 == "2":
            print("Reach the sealing device at the gate")
            print("1) Trust the opinion of the inventor's daughter and stop it")
            print("2) Activate as my father planned")
            
            ans4 = get_choice(["1", "2"])
            
            if ans4 == "1":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Inventor's Daughter")
                print("2) Player")
                
                ans5 = get_choice(["1", "2"])
                
                if ans5 == "1":
                    print("Technology and reason for a stable future.")
                elif ans5 == "2":
                    print("You live as “guardian of the sealed gate”.")
            
            elif ans4 == "2":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Player")
                
                ans5 = get_choice(["1"])
                
                if ans5 == "1":
                    print("You live as “guardian of the sealed gate”.")
    elif ans2 == "2":
        print("Captured by rebel leader on Dark Island ")
        print("Rebel leader convinces you that you can end the oppression of the kingdom if you use the gate to gain power.")
        print("1) Turn and become the rebel leader's collaborator")
        print("2) Escape and inform the inventor's daughter")
        print("3) Stay neutral")
        
        ans3 = get_choice(["1", "2", "3"])
        if ans3 == "1":
            print("Reach the sealing device at the gate")
            print("1) Let it go out of control with the rebel leader")
            print("2) Shutting down the equipment")
            
            ans4 = get_choice(["1", "2"])
            
            if ans4 == "1":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Rebel leader")
                print("2) Player")
                print("3) Informant")
                
                ans5 = get_choice(["1", "2", "3"])
                
                if ans5 == "1":
                    print("They destroyed inequality through revolution by force.")
                elif ans5 == "2":
                    print("You live as “guardian of the sealed gate”.")
                elif ans5 == "3":
                    print("Future where neutrality and chaos intersect")    
            elif ans4 == "2":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Player")
                print("2) Inventor's Daughter")
                print("3) Informant")
                
                ans5 = get_choice(["1", "2", "3"])
                
                if ans5 == "1":
                    print("You live as “guardian of the sealed gate”.")
                elif ans5 == "2":
                    print("Technology and reason for a stable future.")
                elif ans5 == "3":
                    print("Future where neutrality and chaos intersect")
        elif ans3 == "2":
            print("Reach the sealing device at the gate")
            print("1) Trust the opinion of the inventor's daughter and stop it")
            print("2) Activate as my father planned")
            
            ans4 = get_choice(["1", "2"])
            
            if ans4 == "1":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Inventor's Daughter")
                print("2) Player")
                print("3) Informant")
                
                ans5 = get_choice(["1", "2", "3"])
                
                if ans5 == "1":
                    print("Technology and reason for a stable future.")
                elif ans5 == "2":
                    print("You live as “guardian of the sealed gate”.")
                elif ans5 == "3":
                    print("Future where neutrality and chaos intersect")
            elif ans4 == "2":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Player")
                print("2) Informant")
                ans5 = get_choice(["1", "2"])
                
                if ans5 == "1":
                    print("You live as “guardian of the sealed gate”.")
                elif ans5 == "2":
                    print("Future where neutrality and chaos intersect")
        elif ans3 == "3":
            print("Reach the sealing device at the gate")
            print("1) Activate as my father planned")
            print("2) Shutting down the equipment")
            
            ans4 = get_choice(["1", "2"])
            if ans4 == "1":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Player")
                print("2) Informant")
                ans5 = get_choice(["1", "2"])
                
                if ans5 == "1":
                    print("You live as “guardian of the sealed gate”.")
                elif ans5 == "2":
                    print("Future where neutrality and chaos intersect")
            
            elif ans4 =="2":
                print("Who will be entrusted with the power of the gate in the future?")
                print("1) Player")
                print("2) Inventor's Daughter")
                print("3) Informant")
                
                ans5 = get_choice(["1", "2", "3"])
                
                if ans5 == "1":
                    print("You live as “guardian of the sealed gate”.")
                elif ans5 == "2":
                    print("Technology and reason for a stable future.")
                elif ans5 == "3":
                    print("Future where neutrality and chaos intersect")
                
            
            
print("Thanks for playing the game!")