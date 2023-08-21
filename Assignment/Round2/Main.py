


def allocate_projects(employee, projects):
    assignments = []
    for project in projects:
        for emp in employee:
            if project["required_skills"] == emp["skills"] and emp["current_project"] == None:
                emp["current_project"] = project["name"]
                assignments.append({"project": project["name"], "employee": emp["name"]})
                break
    return assignments

employee = [
    {"name": "Aman", "skills": ["Python", "Database"], "current_project": None},
    {"name": "Rahul", "skills": ["Java", "Testing"], "current_project": None},
    {"name": "Priti", "skills": ["Python", "Java"], "current_project": None},
]

projects = [
    {"name": "Project A", "required_skills": ["Python", "Database"]},
    {"name": "Project B", "required_skills": ["Java", "Testing"]},
    {"name": "Project A", "required_skills": ["Python", "Java"]},
]
    

print(allocate_projects(employee, projects))