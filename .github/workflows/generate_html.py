import os
import glob
import re
from datetime import datetime

def get_projects():
    """Get sorted list of project folders (1-candidatura, 2-rtb, etc.)"""
    return sorted([f for f in os.listdir('site-repo') 
                 if re.match(r'^\d+-', f)])

def generate_anchor_id(project_folder):
    """Convert '1-candidatura' to 'candidatura' for anchor links"""
    return re.sub(r'^\d+-', '', project_folder)

def generate_aside_links(projects):
    """Create navigation links for the aside"""
    links = []
    for project in projects:
        name = re.sub(r'^\d+-', '', project).replace("-", " ").title()
        anchor = generate_anchor_id(project)
        links.append(f'<li><a href="#{anchor}">{name}</a></li>')
    return '\n'.join(links)

def generate_project_section(project_folder):
    """Create section with anchor ID for deep linking"""
    anchor_id = generate_anchor_id(project_folder)
    # ... rest of your existing project section generation code ...
    return f'<section id="{anchor_id}">\n{content}\n</section>'

def update_index():
    with open("index.html", "r") as f:
        content = f.read()
    
    projects = get_projects()
    
    # Update aside navigation
    new_content = content.replace(
        '<!-- ASIDE LINKS PLACEHOLDER -->',
        generate_aside_links(projects)
    )
    
    # Update main content
    projects_html = "\n".join([generate_project_section(p) for p in projects])
    new_content = new_content.replace(
        '<!-- PROJECT SECTIONS PLACEHOLDER -->',
        projects_html
    )
    
    with open("index.html", "w") as f:
        f.write(new_content)
