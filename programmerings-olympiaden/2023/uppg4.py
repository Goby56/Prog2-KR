strengths = (int(input("Antal ettor ? ")), int(input("Antal tvåor ? ")), int(input("Antal treor ? ")), int(input("Antal fyror ? ")))

team_strength = lambda team: map(lambda x, y: x*y, team, [1,2,3,4])

soot = team_strength(strengths) # Strength of one team

def solve(current_team: list, strengths_left: list):
    if team_strength(current_team) == sum(strengths)//2:
        print(current_team)
        return
    






