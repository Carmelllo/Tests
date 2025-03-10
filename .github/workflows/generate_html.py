import os
import glob
import re
from datetime import datetime

def get_project_folders():
    """Find all folders matching the pattern 'number-name' (e.g., 1-candidatura)"""
    return sorted([f for f in os.listdir('site-repo') if re.match(r'^\d+-', f)])

def extract_date(filename):
    match = re.search(r'\d{8}', filename)
    return datetime.strptime(match.group(), "%Y%m%d") if match else datetime.min

def generate_project_section(project_folder):
    base_path = f"site-repo/{project_folder}"
    section_name = re.sub(r'^\d+-', '', project_folder).replace("-", " ").title()
    
    html = f"""
    <section class="project-section">
        <h1>{section_name}</h1>
    """
    
    # Non-verbali documents
    non_verbali = []
    for doc in glob.glob(f"{base_path}/*.pdf"):
        if "verbali" not in doc:
            name = os.path.basename(doc).replace(".pdf", "").replace("-", " ").title()
            non_verbali.append(f'<li><a href="{project_folder}/{os.path.basename(doc)}">{name}</a></li>')
    
    if non_verbali:
        html += '<ul class="document-list">\n' + '\n'.join(non_verbali) + '</ul>'
    
    # Verbali subsections
    html += '<div class="verbali-container">'
    for tipo in ["interno", "esterno"]:
        verbali = sorted(glob.glob(f"{base_path}/verbali/{tipo}/*.pdf"), 
                       key=extract_date, reverse=True)
        if verbali:
            html += f"""
            <div>
                <h2>Verbale {tipo.title()}</h2>
                <ul>
            """
            for pdf in verbali:
                date = extract_date(os.path.basename(pdf)).strftime("%d/%m/%Y")
                html += f'<li><a href="{project_folder}/verbali/{tipo}/{os.path.basename(pdf)}">{date}</a></li>'
            html += '</ul></div>'
    html += '</div></section>'
    
    return html

def update_index():
    with open("index.html", "r") as f:
        content = f.read()
    
    sections = []
    for project in get_project_folders():
        sections.append(generate_project_section(project))
    
    new_content = content.replace(
        '<!-- AUTO-GENERATED SECTIONS -->',
        '\n'.join(sections)
    )
    
    with open("index.html", "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_index()
