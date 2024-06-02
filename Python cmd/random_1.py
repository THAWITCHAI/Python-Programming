import random as rd


def ran(name:str, team:int):
    # print(name, team)
    if team == 1:
        if len(team_1) == 3:
            if len(team_2) != 3:
                team=2
                team_2.append({
                'name':name,
                'team':team
            })
        else:
            team_1.append({
                'name':name,
                'team':team
            })
            # user.remove(name)
    elif team == 2:
        if len(team_2) == 3:
            if len(team_1) != 3:
                team=1
                team_1.append({
                'name':name,
                'team':team
            })
        else:
            team_2.append({
                'name':name,
                'team':team
            })
            # user.remove(name)


if __name__ == '__main__':
    user = [
    {
        'name':'Pae',
        'team':''
    },
    {
        'name':'jame',
        'team':''
    },
    {
        'name':'Jack',
        'team':''
    },
    {
        'name':'Pond',
        'team':''
    },
    {
        'name':'Ole',
        'team':''
    },
    {
        'name':'Tong',
        'team':''
    },
    ]
    team_1 = []
    team_2 = []    

    for i in user:
        num = rd.randint(1, 2)
        name = i['name']
        ran(name, num)
        
    print('------------------------------------------------Team 1------------------------------------------------')
    for i in team_1:
        print(i['name'])
    print('------------------------------------------------------------------------------------------------------')
    print('------------------------------------------------Team 2------------------------------------------------')
    for i in team_2:
        print(i['name'])
    print('------------------------------------------------------------------------------------------------------')

