def main():
    invited = ("Mario", "Luigi", "Daisy", "Yoshi", "Toad", "Princess Peach", "Bowser")
    for receiver in invited:
        if receiver != "Princess Peach":
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