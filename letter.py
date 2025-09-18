def main():
    invited = ("Mario", "Luigi", "Daisy", "Yoshi", "Toad", "𝒫𝓇𝒾𝓃𝒸𝑒𝓈𝓈 𝒫𝑒𝒶𝒸𝒽", "Bowser")
    for receiver in invited:
        if receiver != "𝒫𝓇𝒾𝓃𝒸𝑒𝓈𝓈 𝒫𝑒𝒶𝒸𝒽":
            print(f"""
                ★~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~★
                    Dear {receiver}, 
                
                    You are cordially invited to a ball at
                    Peache's Castle this evening, 7:00PM.
                                ~~~★~~~
                    Sincerely,
                    {invited[5]}
                ★~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~★""")
main()