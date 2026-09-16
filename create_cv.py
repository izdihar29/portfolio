from fpdf import FPDF
import os

# ============ CV CONTENT - all ASCII, no asterisks ============
cv_lines = [
    "# CV Template",
    "",
    "## Contact Information",
    "- Name: Racksha Vasantharuban",
    "- Phone: +44 7305 175774",
    "- Email: racksha.vasanth@gmail.com",
    "- LinkedIn: https://www.linkedin.com/in/racksha-v-6158a537b/",
    "- Location: London, England",
    "",
    "## Professional Summary",
    "I am a Year 13 student at Tolworth Girls School studying Maths Physics Chemistry with predicted grades AAA. Focused on improving student experience I understand how students learn and communicate in a way that feels clear and supportive. My work with younger students has strengthened my responsibility and confidence grows when someone feels understood.",
    "",
    "## Skills",
    "### Technical Skills",
    "- Word",
    "- PowerPoint",
    "- Sketchup",
    "- Copilot",
    "- Claude",
    "- Deepseek",
    "",
    "### Soft Skills",
    "- Teamwork",
    "- Problem solving",
    "- Creativity",
    "- Communication",
    "- Adaptability",
    "- Time management",
    "",
    "## Professional Experience",
    "",
    "### Wize Foundation - Student Ambassador | Jun 2026-Present",
    "- Representing Wize Foundation supporting outreach disadvantaged students taking part in insight days at major firms helping run newsletter by selecting updates writing concise summaries delivering presentations in school supporting ambassador projects joining workshops panels contributing student-focused viewpoints",
    "",
    "### LEAF Pathways - Intern | Sep 2026-Present",
    "- Representing LEAF Pathways outreach tasks reviewing school-facing materials improving clarity helping organise project workflows keeping track of deadlines contributing ideas improve student engagement based observed needs assisting research tasks informing programme development building confidence working professional environment communicating progress reliably",
    "",
    "### Springpod Advisory Board - Student Advisor | Jan-Jun 2026",
    "- Representing student perspectives accessibility career education evaluating platform features highlighting areas where students struggled contributing discussions with Springpod staff partners using direct student insight collaborating with other board members shape more inclusive relevant solutions communicating student needs precise structured way influencing platform decisions",
    "",
    "### Higherin - Student Ambassador | Jul 2026-Present",
    "- Representing employers including Deloitte PwC and University of Law to students helping students identify apprenticeship routes they havent considered sharing opportunities with interested students guiding next steps supporting short employer campaigns reviewing improving outreach materials talking to students about apprenticeships career paths clear grounded way",
    "",
    "## Education",
    "",
    "A-Levels | Tolworth Girls School and Sixth Form | London - predicted AAA in Maths Physics Chemistry. GCSEs | Tolworth Girls School | London - 11 grades 9-7 (A-A) with 9/A* in English Language and 8/A* in Maths.",
    "",
    "## Languages",
    "",
    "English: Native/Bilingual | Tamil: Native/Bilingual | Spanish: Limited working proficiency",
]

# Join into a single string - all ASCII, no special chars
cv_content = "\n".join(cv_lines)


class PDF(FPDF):
    def __init__(self):
        super().__init__()
        # Small margins to fit everything on one page
        self.set_auto_page_break(auto=False)
        self.set_margins(15, 15, 15)
    
    def header(self):
        # Thin line on subsequent pages
        if self.page_no() > 1:
            self.set_draw_color(0, 0, 0)
            self.set_line_width(0.3)
            self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
            self.ln(3)


pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=False, margin=20)

w = pdf.w - pdf.l_margin - pdf.r_margin  # usable width

# ============ NAME SECTION - prominent at top ============
pdf.set_font("Helvetica", 'B', 22)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 12, "Racksha Vasantharuban", 0, 1, 'C')

# Thin separator line under name
pdf.set_draw_color(0, 0, 0)
pdf.set_line_width(0.4)
pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
pdf.ln(3)

# ============ Contact info - compact ============
pdf.set_font("Helvetica", '', 9)
pdf.set_text_color(60, 60, 60)
contact_text = "+44 7305 175774 | racksha.vasanth@gmail.com | London, England"
pdf.cell(0, 5, contact_text, 0, 1, 'C')
pdf.set_text_color(0, 0, 0)
pdf.ln(3)

# ============ PROFESSIONAL SUMMARY - 2 lines condensed ============
pdf.set_font("Helvetica", '', 9.5)
pdf.set_text_color(0, 0, 0)

# Summary text - already 2-line ready from the content lines
# Split the summary into two lines
summary_full = "I am a Year 13 student at Tolworth Girls School studying Maths Physics Chemistry with predicted grades AAA. Focused on improving student experience I understand how students learn and communicate in a way that feels clear and supportive. My work with younger students has strengthened my responsibility and confidence grows when someone feels understood."

# Split into two roughly equal parts
words = summary_full.split()
mid = len(words) // 2
first_line = ' '.join(words[:mid])
second_line = ' '.join(words[mid:])

# Available width
avail_w = w - 20

# Write first line
pdf.set_font("Helvetica", '', 8.5)
first_width = pdf.get_string_width(first_line)
if first_width > avail_w - 20:
    # Condense further
    first_line = "I am a Year 13 student focusing on improving student experience understanding how students learn and communicating clearly. My work has strengthened my responsibility and confidence grows when someone feels understood."

pdf.cell(avail_w, 5, first_line, 0, 1, 'L')

# Second line
pdf.set_font("Helvetica", '', 8.5)
second_width = pdf.get_string_width(second_line)
if second_width > avail_w - 20:
    second_line = second_line[:50] + "..."

pdf.set_xy(pdf.get_x(), pdf.get_y() + 1)
pdf.cell(avail_w, 5, second_line, 0, 1, 'L')

pdf.ln(3)

# ============ SEPARATOR ============
pdf.set_draw_color(0, 0, 0)
pdf.set_line_width(0.3)
pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
pdf.ln(3)

# ============ SKILLS SECTION - compact ============
pdf.set_font("Helvetica", 'B', 10)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 6, "Skills", 0, 1, 'L')
pdf.ln(1)

# Technical Skills - as a compact horizontal list
pdf.set_font("Helvetica", '', 8.5)
pdf.set_text_color(40, 40, 40)
tech_skills = ["Word", "PowerPoint", "Sketchup", "Copilot", "Claude", "Deepseek"]
x_pos = pdf.l_margin
pdf.set_xy(x_pos, pdf.get_y())
for i, skill in enumerate(tech_skills):
    pdf.cell(28, 4, skill, 0, 0, 'L')
    if (i + 1) % 3 == 0 or i == len(tech_skills) - 1:
        pdf.ln(4)
    else:
        pdf.cell(3, 4, "", 0, 0, 'L')

pdf.set_text_color(0, 0, 0)
pdf.ln(2)

# Soft Skills
pdf.set_font("Helvetica", 'B', 8.5)
pdf.cell(0, 5, "Soft Skills", 0, 1, 'L')
pdf.set_font("Helvetica", '', 8.5)
soft_skills = ["Teamwork", "Problem solving", "Creativity", "Communication", "Adaptability", "Time management"]
x_pos = pdf.l_margin
pdf.set_xy(x_pos, pdf.get_y())
for i, skill in enumerate(soft_skills):
    pdf.cell(35, 4, skill, 0, 0, 'L')
    if (i + 1) == len(soft_skills):
        pdf.ln(4)
    else:
        pdf.cell(3, 4, "", 0, 0, 'L')

pdf.ln(3)

# ============ PROFESSIONAL EXPERIENCE - compact ============
pdf.set_font("Helvetica", 'B', 10)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 6, "Professional Experience", 0, 1, 'L')
pdf.ln(1)

experiences = [
    ("Wize Foundation - Student Ambassador | Jun 2026-Present",
     "Representing Wize Foundation supporting outreach disadvantaged students taking part in insight days at major firms helping run newsletter by selecting updates writing concise summaries delivering presentations in school supporting ambassador projects joining workshops panels contributing student-focused viewpoints"),
    ("LEAF Pathways - Intern | Sep 2026-Present",
     "Representing LEAF Pathways outreach tasks reviewing school-facing materials improving clarity helping organise project workflows keeping track of deadlines contributing ideas improve student engagement based observed needs assisting research tasks informing programme development building confidence working professional environment communicating progress reliably"),
    ("Springpod Advisory Board - Student Advisor | Jan-Jun 2026",
     "Representing student perspectives accessibility career education evaluating platform features highlighting areas where students struggled contributing discussions with Springpod staff partners using direct student insight collaborating with other board members shape more inclusive relevant solutions communicating student needs precise structured way influencing platform decisions"),
    ("Higherin - Student Ambassador | Jul 2026-Present",
     "Representing employers including Deloitte PwC and University of Law to students helping students identify apprenticeship routes they havent considered sharing opportunities with interested students guiding next steps supporting short employer campaigns reviewing improving outreach materials talking to students about apprenticeships career paths clear grounded way"),
]

for title, bullets in experiences:
    pdf.set_font("Helvetica", 'B', 8.5)
    pdf.cell(0, 5, title, 0, 1, 'L')
    pdf.ln(0.5)
    pdf.set_font("Helvetica", '', 7.5)
    pdf.set_text_color(50, 50, 50)
    # Truncate bullet if too long for one line
    if len(bullets) > 85:
        bullets = bullets[:80] + "..."
    pdf.cell(0, 4, "- " + bullets, 0, 1, 'L')
    pdf.set_text_color(0, 0, 0)
    pdf.ln(1.5)

pdf.ln(3)

# ============ EDUCATION ============
pdf.set_font("Helvetica", 'B', 10)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 6, "Education", 0, 1, 'L')
pdf.ln(1)

# Education text from the content lines
edu_text = "A-Levels | Tolworth Girls School and Sixth Form | London - predicted AAA in Maths Physics Chemistry. GCSEs | Tolworth Girls School | London - 11 grades 9-7 (A-A) with 9/A* in English Language and 8/A* in Maths."
pdf.set_font("Helvetica", '', 8.5)
pdf.set_text_color(50, 50, 50)
pdf.cell(0, 4, edu_text, 0, 1, 'L')
pdf.set_text_color(0, 0, 0)
pdf.ln(3)

# ============ LANGUAGES ============
pdf.set_font("Helvetica", 'B', 10)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 6, "Languages", 0, 1, 'L')
pdf.ln(1)

pdf.set_font("Helvetica", '', 8.5)
pdf.set_text_color(40, 40, 40)
lang_text = "English: Native/Bilingual | Tamil: Native/Bilingual | Spanish: Limited working proficiency"
pdf.cell(0, 5, lang_text, 0, 1, 'L')
pdf.set_text_color(0, 0, 0)
pdf.ln(5)

# ============ Output ============
output_path = r"C:\Users\rackv\Documents\cv_design.pdf"
pdf.output(output_path)
print(f"PDF created: {output_path}")
print(f"Pages: {pdf.page_no()}")