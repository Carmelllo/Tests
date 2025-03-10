def generate_project_section(project_folder):
    project_path = f"Tests.github.io/{project_folder}"
    project_name = re.sub(r'^\d+-', '', project_folder).replace("-", " ").title()
    
    html = f"""
    <section id="{project_folder}">
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
    
    # Verbali subsections (FIXED FOLDER NAMES)
    html += '<div class="verbali-container">'
    for tipo in ["interni", "esterni"]:  # Changed to match folder names
        verbali = sorted(glob.glob(f"{project_path}/verbali/{tipo}/*.pdf"), 
                       key=lambda x: os.path.basename(x), reverse=True)
        if verbali:
            html += f"""
            <div>
                <h2>Verbale {tipo[:-1].title()}</h2>  # "interni" → "interno"
                <ul>
            """
            for pdf in verbali:
                date_str = os.path.basename(pdf).split('_')[1][:8]
                date = datetime.strptime(date_str, "%Y%m%d").strftime("%d/%m/%Y")
                html += f'<li><a href="{project_folder}/verbali/{tipo}/{os.path.basename(pdf)}">{date}</a></li>'
            html += '</ul></div>'
    html += '</div></section>'
    
    return html
