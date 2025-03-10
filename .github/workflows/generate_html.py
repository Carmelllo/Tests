import os
import glob
import re
from datetime import datetime

def get_projects():
    """Find all numbered project folders (1-candidatura, 2-rtb, etc.)"""
    return sorted([f for f in os.listdir('Tests.github.io') 
                  if re.match(r'^\d+-', f)])

def generate_project_section(project_folder):
    project_path = f"Tests.github.io/{project_folder}"
    project_name = re.sub(r'^\d+-', '', project_folder).replace("-", " ").title()
    
    html = f"""
    <section id="{project_folder}">
        <h1>{project_name}</h1>
    """
    
    # Non-verbali documents (include all PDFs not in verbali subfolders)
    non_verbali = []
    for doc in glob.glob(f"{project_path}/**/*.pdf", recursive=True):
        if "verbali" not in os.path.dirname(doc):
            rel_path = os.path.relpath(doc, project_path)
            doc_name = os.path.basename(doc).replace(".pdf", "").replace("-", " ").title()
            non_verbali.append(f'<li><a href="{project_folder}/{rel_path}">{doc_name}</a></li>')
    
    # Verbali subsections
    html += '<div class="verbali-container">'
    for tipo in ["interni", "esterni"]:
        verbali = sorted(glob.glob(f"{project_path}/verbali/{tipo}/*.pdf"), 
                       key=lambda x: os.path.basename(x), reverse=True)
        if verbali:
            html += f"""
            <div>
                <h2>Verbali {tipo.title()}</h2>
                <ul>
            """
            for pdf in verbali:
                date_str = os.path.basename(pdf).split('_')[1][:8]
                date = datetime.strptime(date_str, "%Y%m%d").strftime("%d/%m/%Y")
                html += f'<li><a href="{project_folder}/verbali/{tipo}/{os.path.basename(pdf)}">{date}</a></li>'
            html += '</ul></div>'
    html += '</div></section>'
    
    return html

def update_index():
    with open("Tests.github.io/index.html", "r") as f:
        content = f.read()
    
    # Generate aside links
    projects = get_projects()
    aside_links = "\n".join([f'<li><a href="#{p}">{re.sub(r"^\\d+-", "", p).replace("-", " ").title()}</a></li>' for p in projects])
    content = content.replace("<!-- ASIDE LINKS PLACEHOLDER -->", aside_links)
    
    # Generate main content
    projects_html = "\n".join([generate_project_section(p) for p in projects])
    start_marker = "<!-- AUTO-GENERATED CONTENT START -->"
    end_marker = "<!-- AUTO-GENERATED CONTENT END -->"
    pattern = re.compile(f"{re.escape(start_marker)}.*?{re.escape(end_marker)}", re.DOTALL)
    content = re.sub(pattern, f"{start_marker}\n{projects_html}\n{end_marker}", content)
    
    # Save changes
    with open("Tests.github.io/index.html", "w") as f:
        f.write(content)

if __name__ == "__main__":
    update_index()
