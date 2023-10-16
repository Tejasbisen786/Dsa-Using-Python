class Team:
    def __init__(self):
        self.team_members = []

    def input_names(self, names):
        # Input a list of names and add them to the team
        self.team_members.extend(names)

    def display_member_names(self):
        # Display the names of all team members
        for member in self.team_members:
            print(member)

# Example usage:
if __name__ == "__main__":
    team = Team()
    
    # Input names
    names_to_add = ["Alice", "Bob", "Charlie", "David"]
    team.input_names(names_to_add)

    # Display member names
    print("Team Members:")
    team.display_member_names()
