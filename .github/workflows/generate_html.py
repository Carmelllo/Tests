import os
import glob
import re
from datetime import datetime

def get_projects():
    """Find all numbered project folders (1-candidatura, 2-rtb, etc.)"""
    return sorted([f for f in os.listdir('Tests.github.io') 
                  if re.match(r'^\d+-', f)])

def generate_project_section(project_folder):
    """Generate HTML for a project section"""
    project_path = f"Tests.github.io/{project_folder}"
    project_name = re.sub(r'^\d+-', '', project_folder).replace("-", " ").title()
    
    html = f"""
    <section class="project-section">
        <h1>{project_name}</h1>
    """
    
    # Non-verbali documents
    non_verbali = []
    for doc in glob.glob(f"{project_path}/*.pdf"):
        if "verbali" not in doc:
            doc_name = os.path.basename(doc).replace(".pdf", "").replace("-", " ").title()
            non_verbali.append(f'<li><a href="{project_folder}/{os.path.basename(doc)}">{doc_name}</a></li>')
    
    if non_verbali:
        html += '<ul class="document-list">\n' + '\n'.join(non_verbali) + '</ul>'
    
    # Verbali subsections
    html += '<div class="verbali-container">'
    for tipo in ["interno", "esterno"]:
        verbali = sorted(glob.glob(f"{project_path}/verbali/{tipo}/*.pdf"), 
                       key=lambda x: os.path.basename(x), reverse=True)
        if verbali:
            html += f"""
            <div>
                <h2>Verbale {tipo.title()}</h2>
                <ul>
            """
            for pdf in verbali:
                date_str = os.path.basename(pdf).split('_')[1][:8]  # Extract YYYYMMDD
                date = datetime.strptime(date_str, "%Y%m%d").strftime("%d/%m/%Y")
                html += f'<li><a href="{project_folder}/verbali/{tipo}/{os.path.basename(pdf)}">{date}</a></li>'
            html += '</ul></div>'
    html += '</div></section>'
    
    return html

def update_index():
    # Read the existing index.html
    with open("Tests.github.io/index.html", "r") as f:
        content = f.read()
    
    # Generate project sections
    projects_html = "\n".join([generate_project_section(p) for p in get_projects()])
    
    # Replace the placeholder in index.html
    new_content = content.replace(
        '<!-- AUTO-GENERATED SECTIONS -->',
        projects_html
    )
    
    # Save the updated index.html
    with open("Tests.github.io/index.html", "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_index()
