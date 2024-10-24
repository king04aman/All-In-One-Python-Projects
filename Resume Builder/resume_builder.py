from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import button_dialog
from fpdf import FPDF
import os

# To clear the terminal after selecting a section
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Resume data storage
resume_data = {
    "contact_info": {},
    "experience": [],
    "education": [],
    "skills": [],
    "projects": [],
    "certifications": [],
    "achievements": []
}

# Function to navigate back to the main menu
def back_to_menu():
    print("\nReturning to main menu...")

# Add contact information
def add_contact_info():
    clear_screen()
    print("Enter Contact Information")
    resume_data["contact_info"]["name"] = prompt("Name: ")
    resume_data["contact_info"]["email"] = prompt("Email: ")
    resume_data["contact_info"]["phone"] = prompt("Phone: ")
    resume_data["contact_info"]["address"] = prompt("Address: ")
    resume_data["contact_info"]["linkedin"] = prompt("LinkedIn URL: ")
    resume_data["contact_info"]["github"] = prompt("GitHub URL: ")
    back_to_menu()

# Add work experience
def add_experience():
    while True:
        clear_screen()
        print("Enter Work Experience")
        experience = {
            "title": prompt("Job Title: "),
            "company": prompt("Company: "),
            "start_date": prompt("Start Date (e.g., June 2024): "),
            "end_date": prompt("End Date (or type 'Present' if still working): "),
            "details": prompt("Details (comma-separated): ").split(',')
        }
        resume_data["experience"].append(experience)

        # Ask user if they want to add more experience entries
        more = prompt("Do you want to add more work experience? (yes/no): ").strip().lower()
        if more == "no":
            break
    back_to_menu()

# Add education details
def add_education():
    while True:
        clear_screen()
        print("Enter Education Information")
        education = {
            "degree": prompt("Degree (e.g., B.Tech in CSE): "),
            "institution": prompt("Institution: "),
            "start_year": prompt("Start Year: "),
            "end_year": prompt("End Year: ")
        }
        resume_data["education"].append(education)

        # Ask user if they want to add more education entries
        more = prompt("Do you want to add more education? (yes/no): ").strip().lower()
        if more == "no":
            break
    back_to_menu()

# Add skills
def add_skills():
    clear_screen()
    print("Enter Skills (comma-separated): ")
    resume_data["skills"] = prompt("Skills: ").split(',')
    back_to_menu()

# Add projects
def add_projects():
    while True:
        clear_screen()
        print("Enter Projects Information")
        project = {
            "name": prompt("Project Name: "),
            "description": prompt("Description: "),
            "technologies": prompt("Technologies Used: ")
        }
        resume_data["projects"].append(project)

        # Ask if they want to add more projects
        more = prompt("Do you want to add more projects? (yes/no): ").strip().lower()
        if more == "no":
            break
    back_to_menu()

# Add certifications
def add_certifications():
    while True:
        clear_screen()
        print("Enter Certifications")
        certification = {
            "name": prompt("Certification Name: "),
            "provider": prompt("Provider: "),
            "year": prompt("Year: ")
        }
        resume_data["certifications"].append(certification)

        more = prompt("Do you want to add more certifications? (yes/no): ").strip().lower()
        if more == "no":
            break
    back_to_menu()

# Add achievements
def add_achievements():
    while True:
        clear_screen()
        print("Enter Achievements")
        achievement = prompt("Achievement: ")
        resume_data["achievements"].append(achievement)

        more = prompt("Do you want to add more achievements? (yes/no): ").strip().lower()
        if more == "no":
            break
    back_to_menu()

# PDF Generation class
class ResumePDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, resume_data["contact_info"]["name"], 0, 1, 'C')
        self.set_font('Arial', 'I', 12)
        self.cell(0, 10, resume_data["contact_info"]["email"], 0, 1, 'C')
        self.cell(0, 10, resume_data["contact_info"]["phone"], 0, 1, 'C')
        self.cell(0, 10, resume_data["contact_info"]["address"], 0, 1, 'C')

    def add_section(self, title, content):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1)
        self.set_font('Arial', '', 11)
        for line in content:
            self.cell(0, 10, line, 0, 1)

# PDF Generation
def generate_pdf():
    pdf = ResumePDF()
    pdf.add_page()

    # Contact Information
    contact = resume_data["contact_info"]
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f"{contact['name']} - {contact['email']}", 0, 1)
    pdf.cell(0, 10, f"Phone: {contact['phone']} - Address: {contact['address']}", 0, 1)
    pdf.cell(0, 10, f"LinkedIn: {contact.get('linkedin', 'N/A')} - GitHub: {contact.get('github', 'N/A')}", 0, 1)

    # Work Experience
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "Experience", 0, 1)
    pdf.set_font('Arial', '', 11)
    for exp in resume_data["experience"]:
        details = ', '.join(exp["details"])
        pdf.cell(0, 10, f"{exp['title']} at {exp['company']} ({exp['start_date']} - {exp['end_date']})", 0, 1)
        pdf.multi_cell(0, 10, f"Responsibilities: {details}")

    # Education
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "Education", 0, 1)
    pdf.set_font('Arial', '', 11)
    for edu in resume_data["education"]:
        pdf.cell(0, 10, f"{edu['degree']} from {edu['institution']} ({edu['start_year']} - {edu['end_year']})", 0, 1)

    # Skills
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "Skills", 0, 1)
    pdf.multi_cell(0, 10, ', '.join(resume_data["skills"]))

    # Projects
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "Projects", 0, 1)
    pdf.set_font('Arial', '', 11)
    for proj in resume_data["projects"]:
        pdf.cell(0, 10, proj["name"], 0, 1)
        pdf.multi_cell(0, 10, proj["description"])
        pdf.cell(0, 10, f"Technologies Used: {proj['technologies']}", 0, 1)

    # Certifications
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "Certifications", 0, 1)
    pdf.set_font('Arial', '', 11)
    for cert in resume_data["certifications"]:
        pdf.cell(0, 10, f"{cert['name']} by {cert['provider']} ({cert['year']})", 0, 1)

    # Achievements
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "Achievements", 0, 1)
    pdf.set_font('Arial', '', 11)
    for ach in resume_data["achievements"]:
        pdf.cell(0, 10, ach, 0, 1)

    # Save PDF
    pdf_output_path = "generated_resume.pdf"
    pdf.output(pdf_output_path)

    # Auto-open PDF after generation
    os.system(f"start {pdf_output_path}" if os.name == "nt" else f"open {pdf_output_path}")
    print(f"Resume generated: {pdf_output_path}")

# Main Menu using button_dialog from prompt_toolkit
def interactive_menu():
    while True:
        clear_screen()
        choice = button_dialog(
            title="Interactive Resume Builder",
            text="Please choose a section to modify:",
            buttons=[
                ("Contact Info", 1),
                ("Work Experience", 2),
                ("Education", 3),
                ("Skills", 4),
                ("Projects", 5),
                ("Certifications", 6),
                ("Achievements", 7),
                ("Generate PDF", 8),
                ("Exit", 9)
            ]
        ).run()

        if choice == 1:
            add_contact_info()
        elif choice == 2:
            add_experience()
        elif choice == 3:
            add_education()
        elif choice == 4:
            add_skills()
        elif choice == 5:
            add_projects()
        elif choice == 6:
            add_certifications()
        elif choice == 7:
            add_achievements()
        elif choice == 8:
            generate_pdf()
        elif choice == 9:
            break

# Start the program
if __name__ == "__main__":
    interactive_menu()
