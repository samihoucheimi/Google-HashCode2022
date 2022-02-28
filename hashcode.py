from collections import defaultdict
import numbers
import pandas as pd
import numpy as np

class Contributor():

    def __init__(self, name : str):
        self.name = name
        self.skills = defaultdict(lambda x: 0)
        self.availability = True
    
    def add_skill(self, skill, level):
        self.skills[skill] = level
    
    def level_up(self, skill):
        self.skills[skill] += 1

    def can_work_independently(self, desired_skill, required_level):
        return self.skills[desired_skill] >= required_level

    def can_be_mentored(self, desired_skill, required_level):
        return self.skills[desired_skill] == required_level - 1

    def is_available(self):
        return self.availability


class Project():

    def __init__(self, name : str, minimum_duration : int, score : int, best_before : int):
        self.name = name
        self.minimum_duration = minimum_duration
        self.score = score
        self.best_before = best_before
        self.roles = {}
    
    def add_role(self, skill, level):
        self.roles[skill] = level

    def decrement_score(self):
        self.score -= 1

    def get_number_of_roles(self):
        return len(self.roles)

    def rank_projects(self, t):
        working_days = self.minimum_duration * len(self.roles)
        adj_score = self.score - max(0, self.minimum_duration + t - self.best_before)

# -----------------------------------------------------------------------------------------------   

contributors = {}
projects = {}
skills_contributors = {}
completed_projects = {}
completed_projects_contributors = {}

# projects['project_1'] = Project('project_1', 1, 1, 1)
# projects['project_2'] =Project('project_2', 1, 1, 1)
# completed_projects = ['project_1', 'project_2']
# completed_projects_contributors = {'project_2' : ['sami', 'farid', 'not sami'] , 'project_1' : ['sami']}

current_file = 'd_dense_schedule'
with open("Desktop/ghc/{}.in.txt".format(current_file), "r") as input:
    line = input.readline()
    
    number_of_contributors = int(line.split(' ')[0])
    number_of_projects = int(line.split(' ')[1])
    
    # Create a Contributor object for each Contirbutor and add it to the contributors dictionary
    for _ in range(number_of_contributors):
        line = input.readline()
        name = line.split(' ')[0]
        num_of_skills = int(line.split(' ')[1])
        contributor = Contributor(name)
        
        for x in range(num_of_skills):
            line = input.readline()
            skill = line.split(' ')[0]
            level = int(line.split(' ')[1])
            contributor.add_skill(skill,level)
            try:  
                skills_contributors[skill].append(contributor)
            except:
                skills_contributors[skill] = [contributor]

        contributors[name] = contributor

    # Print name and skills for every contributor
    # for contributor in contributors.values():
        # print('Contributor name: {}'.format(contributor.name))
        # print('Contributor skills: {}'.format(contributor.skills))
    
    # Create a Project object for each project and add it to the projects dictionaries
    for _ in range(number_of_projects):
        line = input.readline()
        split_line = line.split(' ')
        name = split_line[0]
        minimum_duration = int(split_line[1])
        score = int(split_line[2])
        best_before = int(split_line[3])
        num_of_roles = int(split_line[4])


        project = Project(name, minimum_duration, score, best_before)
        
        for _ in range(num_of_roles):
            line = input.readline()
            role = line.split(' ')[0]
            level = int(line.split(' ')[1])
            project.add_role(role,level)

        projects[name] = project

    # for project in projects.values():
    #     print('--------------------')
    #     print('Project name: {}'.format(project.name))
    #     print('Project skills: {}'.format(project.roles))
    #     print('Project minimum duration: {}'.format(project.minimum_duration))
    #     print('Project best before: {}'.format(project.best_before))

    for project_name in projects:
        for contributor_name in contributors:
            project_object = projects[project_name]
            contributor_object = contributors[contributor_name]
            
            if (contributor_object.skills.keys() & project_object.roles.keys()):
                common = contributor_object.skills.keys() & project_object.roles.keys()
                # print('{} has the skills {} for project: {}'.format(contributor_name, common, project_name))


def complete_project(project_object, dictionary_of_contributor_name_to_skill_used ,list_of_contributor_objects):

    for contributor in list_of_contributor_objects:
        contributor.level_up(dictionary_of_contributor_name_to_skill_used[contributor.name])

    # print('completing project: {}'.format(project_object.name))
    for contributor in list_of_contributor_objects:
        # print('project is completed by: {}'.format(contributor.name))
        pass
    projects.pop(project_object.name)

with open('solution_{}.txt'.format(current_file), 'w') as f:
    f.write(str(len(completed_projects)))
    f.write('\n')

    for project in completed_projects:
        f.write(projects[project].name)
        f.write('\n')

        for i in range(len(completed_projects_contributors[projects[project].name])):
            if i != 0:
                f.write(' ')
            f.write(completed_projects_contributors[projects[project].name][i])
        f.write('\n')
        
def find_skilled_contributors(project):
    
    list_of_contributors = {}
    list_of_required_skills = project.roles

    for contributor in contributors:
        if contributor.skills

    return list_of_contributors


def rank_projects(time, projects):
    working_hours = []
    adj_score = []
    difficulty = []
    for project in projects:
        working_hours.append(project.get_working_hours())
        adj_score.append(project.get_adjusted_score(time))
        difficulty.append(project.get_difficulty)
    rank_working_hours = np.array([sorted(working_hours).index(x) for x in working_hours])
    rank_adj_score = np.array([sorted(adj_score).index(x) for x in adj_score])
    rank_difficulty = np.array([sorted(difficulty).index(x) for x in difficulty])
    final_score = rank_working_hours + rank_difficulty - rank_adj_score
    ranking = [project_name for _, project_name in sorted(zip(final_score, projects.keys()), key=lambda pair: pair[0])]
    return ranking



#--------------------------------- Backtest -----------------------
t = 0
score = 0


while True:

    ranking = rank_project(t, projects)
    for project_name in ranking:
        team = [] #list of contributors
        
        
        

    t += 1
