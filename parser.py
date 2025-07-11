import re

print("Welcome to Resume Parser")

 
with open("resume_parser.txt", "r") as file:
    text = file.read()
    
epattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
ephone = r'(?:\+91[\-\s]?)?[6-9]\d{9}'

skillset = ["python", "java", "c++", "c", "javascript", "typescript", "kotlin", "swift", "go", "ruby", "rust", "html", "css", "javascript", "react", "node", "express", "bootstrap", "tailwind", "next.js"
, "sql", "mysql", "postgresql", "sqlite", "mongodb", "redis", "firebase", "machine learning", "deep learning", "computer vision", "nlp", "scikit-learn", "tensorflow", "keras", "pytorch"
, "pandas", "numpy", "matplotlib", "seaborn", "data analysis", "data visualization", "power bi", "excel", "git", "github", "linux", "docker", "kubernetes", "ci/cd", "bash", "terminal", "vscode"
, "flask", "django", "fastapi", "api", "rest", "graphql", "oop", "dsa", "problem solving", "debugging", "testing", "unit testing", "agile", "scrum"
]

education_keywords = ["b.tech", "m.tech", "be", "pu", "class 10", "10th", "12th", "class 12",
                      "engineering", "college", "university", "rvce", "iit", "school", "cbse", "puc"]
                      
experience_keywords = [
    "intern", "internship", "worked", "developed", "built",
    "created", "designed", "led", "managed", "contributed",
    "collaborated", "project", "experience", "volunteer", "freelance",
    "research", "engineer", "software", "trainee", "job"
]



def extract_name(text):
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue  # Skip empty lines
        if line.lower().startswith("name:"):
            return line.split(":", 1)[1].strip()
        elif "resume of" in line.lower():
            return line.lower().split("resume of", 1)[1].strip().title()
        elif idx == 0:
            return line.strip()
    return "Unknown"

    
def extract_email(text):
    matches = re.findall(epattern, text)
    return matches
    
def extract_phone(text):
    match = re.findall(ephone , text)
    return match

def extract_skills(text):
    matched_skills = []
    text = text.lower()
    for skill in skillset:
    
        if skill in text:
            matched_skills.append(skill.title().strip())
        
    return list(set(matched_skills))
    
def extract_education(text):
    matched_education = []
    text = text.lower().splitlines()
    for line in text:
        for edu in education_keywords:
            if edu in line:
                matched_education.append(line.title().strip())
        
    return list(set(matched_education))

def extract_experience(text):
    matched_experience = []
    text = text.lower().splitlines()
    for line in text:
        for exp in experience_keywords:
            if exp in line:
                matched_experience.append(line.title().strip())
    return list(set(matched_experience))

        
# Create the resume dictionary
resume = {
    "Name": extract_name(text),
    "Email": extract_email(text),
    "Phone" : extract_phone(text),
    "Matched Skills" : extract_skills(text),
    "Education" : extract_education(text),
    "Experience": extract_experience(text) 
}

for key in resume:
    print(f"{key} : {resume[key]}")

