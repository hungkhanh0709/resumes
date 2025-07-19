#!/usr/bin/env python3
"""
English CV PDF Generator - Professional Resume PDF Creation with Avatar
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

def create_styles():
    """Create custom styles for the PDF"""
    styles = getSampleStyleSheet()
    
    styles.add(ParagraphStyle(
        name='CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=6,
        textColor=HexColor('#2C3E50'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    ))
    
    styles.add(ParagraphStyle(
        name='CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        textColor=HexColor('#34495E'),
        alignment=TA_CENTER,
        fontName='Helvetica'
    ))
    
    styles.add(ParagraphStyle(
        name='SectionHeader',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=8,
        spaceBefore=16,
        textColor=HexColor('#2C3E50'),
        fontName='Helvetica-Bold'
    ))
    
    styles.add(ParagraphStyle(
        name='JobTitle',
        parent=styles['Heading3'],
        fontSize=12,
        spaceAfter=4,
        textColor=HexColor('#2980B9'),
        fontName='Helvetica-Bold'
    ))
    
    styles.add(ParagraphStyle(
        name='Company',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=4,
        textColor=HexColor('#7F8C8D'),
        fontName='Helvetica-Oblique'
    ))
    
    styles.add(ParagraphStyle(
        name='Duration',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=8,
        textColor=HexColor('#95A5A6'),
        fontName='Helvetica'
    ))
    
    styles.add(ParagraphStyle(
        name='BulletPoint',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=4,
        leftIndent=20,
        fontName='Helvetica'
    ))
    
    styles.add(ParagraphStyle(
        name='ContactInfo',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=4,
        alignment=TA_CENTER,
        fontName='Helvetica'
    ))
    
    return styles

def main():
    """Main function to generate the CV PDF with avatar"""
    print("🚀 Starting English PDF generation with avatar...")
    
    # Setup
    filename = "khanh-to-resume-english.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, rightMargin=0.5*inch, leftMargin=0.5*inch, topMargin=0.5*inch, bottomMargin=0.5*inch)
    story = []
    styles = create_styles()
    
    print("📝 Adding header section...")
    
    # Check if avatar image exists
    avatar_path = "./img/IMG_3832.JPG"
    photo_content = None
    
    if os.path.exists(avatar_path):
        try:
            # Create image with exact square dimensions
            photo_content = Image(avatar_path, width=2.08*inch, height=2.08*inch)
            print(f"✅ Avatar image loaded: {avatar_path}")
        except Exception as e:
            print(f"⚠️  Could not load image: {e}")
            photo_content = Paragraph("<br/><br/><b>PHOTO</b><br/><br/><br/>", styles['ContactInfo'])
    else:
        print(f"⚠️  Avatar image not found: {avatar_path}")
        photo_content = Paragraph("<br/><br/><b>PHOTO</b><br/><br/><br/>", styles['ContactInfo'])
    
    # Header with name and profile picture
    header_data = [
        [
            [
                Paragraph("To Hung Khanh", styles['CustomTitle']),
                Paragraph("Senior Backend Engineer", styles['CustomSubtitle'])
            ],
            photo_content
        ]
    ]
    
    header_table = Table(header_data, colWidths=[4.2*inch, 2.08*inch], rowHeights=[2.08*inch])
    header_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('ALIGN', (1, 0), (1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),
        ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
        ('BOX', (1, 0), (1, 0), 2, HexColor('#2C3E50')),
        ('BACKGROUND', (1, 0), (1, 0), HexColor('#F8F9FA')),
    ]))
    
    story.append(header_table)
    story.append(Spacer(1, 12))
    
    # Contact Information with adjusted widths
    contact_data = [
        ["📧 Email", "hungkhanh0709@gmail.com", "📱 Phone", "+84 946 686 872"],
        ["🌍 Location", "Ho Chi Minh City, Vietnam", "👤 Gender", "Male"],
        ["🔗 GitHub", "github.com/hungkhanh0709/resumes", "🎂 DOB", "September 7, 1990"],
        ["", "", "💒 Marital Status", "Married"]
    ]
    
    contact_table = Table(contact_data, colWidths=[0.8*inch, 2.5*inch, 1.3*inch, 2.2*inch])
    contact_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),
        ('FONTNAME', (3, 0), (3, -1), 'Helvetica'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#E8E8E8')),
    ]))
    
    story.append(contact_table)
    story.append(Spacer(1, 16))
    
    print("📝 Adding professional summary...")
    
    # Professional Summary
    story.append(Paragraph("💡 Career Summary", styles['SectionHeader']))
    summary_text = """
    With <b>10+ years</b> of experience in backend development and enterprise-scale applications. 
    Currently working at <b>Techbase Vietnam (LY Corporation subsidiary)</b> with proven track record 
    delivering high-traffic backend systems for millions of users. Strong background in 
    <b>Java, Spring Boot, Node.js</b>, and modern cloud technologies with solid understanding of 
    frontend development. Passionate about AI technologies, team collaboration, and continuous 
    learning with <b>JLPT N3 certification</b> and active involvement in internal tech teams. 
    <b>Aspiring to technical leadership roles</b> with demonstrated mentoring and project coordination experience.
    """
    story.append(Paragraph(summary_text.strip(), styles['Normal']))
    story.append(Spacer(1, 12))
    
    print("📝 Adding work experience...")
    
    # Work Experience
    story.append(Paragraph("💼 Work Experience", styles['SectionHeader']))
    
    # Current Position
    story.append(Paragraph("Senior Backend Engineer & TechTeam Member", styles['JobTitle']))
    story.append(Paragraph("Techbase Vietnam (TBV) - LY Corporation Subsidiary, Ho Chi Minh City, Vietnam", styles['Company']))
    story.append(Paragraph("April 2017 - Present (8+ years)", styles['Duration']))
    
    current_achievements = [
        "Currently contributing to Yahoo! Kids portal development within a 12-member team using Java Spring Boot, Docker, CI/CD",
        "Developed AI Game Creator platform (Apr to Jul 2025) - an AI-powered game development tool for children",
        "Contributed to Japan's largest donation portal (Jun 2020 - Feb 2022) serving millions of users",
        "Engineered Yahoo! Kids portal (Feb 2019 - May 2020) - a high-traffic children's website",
        "Developed myThings IoT application (Apr 2017 - Jan 2019) using PHP, Java, and Go Language",
        "Active TechTeam member (May 2023 - Present) - Internal team supporting 100+ developers",
        "AI Technology Pioneer - Working with OpenAI APIs and LLMs, training team members"
    ]
    
    for achievement in current_achievements:
        story.append(Paragraph(f"• {achievement}", styles['BulletPoint']))
    
    story.append(Spacer(1, 8))
    
    # Previous Positions
    story.append(Paragraph("Team Leader & Backend Developer", styles['JobTitle']))
    story.append(Paragraph("Gumi Vietnam, Ho Chi Minh City, Vietnam", styles['Company']))
    story.append(Paragraph("January 2015 - March 2017 (2+ years)", styles['Duration']))
    
    gumi_achievements = [
        "Promoted to Team Leader (July 2015) managing 3 developers",
        "Led CliSSS medical system backend development using Ruby on Rails and Deep Learning",
        "Built MnS reporting system backend - comprehensive business intelligence platform",
        "Developed CampusCareer recruitment platform backend serving Japanese job market"
    ]
    
    for achievement in gumi_achievements:
        story.append(Paragraph(f"• {achievement}", styles['BulletPoint']))
    
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("Software Developer & Team Leader", styles['JobTitle']))
    story.append(Paragraph("LIT Solution Company, Ho Chi Minh City, Vietnam", styles['Company']))
    story.append(Paragraph("February 2012 - February 2015 (3 years)", styles['Duration']))
    
    lit_achievements = [
        "Promoted to Team Leader (March 2014) managing 5 developers",
        "Developed iLaTour - comprehensive tour management system",
        "Maintained KeyMan HRM system managing 2000+ employees"
    ]
    
    for achievement in lit_achievements:
        story.append(Paragraph(f"• {achievement}", styles['BulletPoint']))
    
    story.append(Spacer(1, 12))
    
    print("📝 Adding technical skills...")
    
    # Technical Skills
    story.append(Paragraph("📝 Technical Skills", styles['SectionHeader']))
    
    skills_data = [
        ["Programming Languages", "Java, JavaScript/TypeScript, PHP, Python, Golang"],
        ["Backend Technologies", "Spring Boot, Node.js, Laravel, MySQL, Redis, MongoDB"],
        ["Frontend Technologies", "React, Vue.js, Next.js, Nuxt.js, Bootstrap, CSS3"],
        ["DevOps & Cloud", "Docker, Kubernetes, AWS, CI/CD, Git"],
        ["AI & Emerging Tech", "OpenAI APIs, LLMs, Deep Learning, IoT Development"],
        ["Enterprise Systems", "Large-scale applications, Performance optimization"]
    ]
    
    skills_table = Table(skills_data, colWidths=[2*inch, 4*inch])
    skills_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#BDC3C7')),
    ]))
    skills_table.hAlign = 'LEFT'  # Align table to left
    
    story.append(skills_table)
    story.append(Spacer(1, 12))
    
    print("📝 Adding education...")
    
    # Education
    story.append(Paragraph("🎓 Education & Certifications", styles['SectionHeader']))
    
    story.append(Paragraph("<b>Programming Diploma (Information Technology)</b>", styles['JobTitle']))
    story.append(Paragraph("Vietnam-America College (VATC), Ho Chi Minh City, Vietnam", styles['Company']))
    story.append(Paragraph("August 2008 - February 2012", styles['Duration']))
    
    story.append(Paragraph("<b>Software Engineering Studies</b>", styles['JobTitle']))
    story.append(Paragraph("Ho Chi Minh University of Industry, Ho Chi Minh City, Vietnam", styles['Company']))
    story.append(Paragraph("August 2014 - July 2017", styles['Duration']))
    
    story.append(Paragraph("<b>JLPT N3 (Japanese Language Proficiency Test)</b>", styles['JobTitle']))
    story.append(Paragraph("Japan Foundation - July 2025", styles['Company']))
    
    story.append(Spacer(1, 12))
    
    # Languages
    story.append(Paragraph("🌟 Languages & Personal Attributes", styles['SectionHeader']))
    
    story.append(Paragraph("<b>Languages:</b>", styles['JobTitle']))
    lang_data = [
        ["Vietnamese", "Native speaker"],
        ["Japanese", "Intermediate (JLPT N3)"],
        ["English", "Intermediate (TOEIC 405)"]
    ]
    
    lang_table = Table(lang_data, colWidths=[1.5*inch, 4.5*inch])
    lang_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#E8E8E8')),
    ]))
    
    story.append(lang_table)
    story.append(Spacer(1, 8))
    
    interests = [
        "Reading enthusiast - Enjoy exploring diverse topics and continuous learning",
        "Technology exploration - Special interest in emerging tech and AI developments",
        "Team collaboration and mentoring junior developers",
        "Cross-cultural communication and international team experience"
    ]
    
    for interest in interests:
        story.append(Paragraph(f"• {interest}", styles['BulletPoint']))
    
    # Footer
    story.append(Spacer(1, 16))
    story.append(Paragraph("<i>Resume last updated: July 2025</i>", styles['ContactInfo']))
    story.append(Paragraph("<i>Available for new opportunities and career advancement</i>", styles['ContactInfo']))
    
    print("🔨 Building PDF...")
    
    # Build PDF
    doc.build(story)
    
    print(f"✅ PDF generated successfully: {filename}")
    print(f"🎉 Your English CV PDF with avatar has been created: {filename}")
    print("📧 You can now send this PDF file to HR departments via email!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error generating PDF: {str(e)}")
        import traceback
        traceback.print_exc()
        print("💡 Make sure you have the reportlab library installed:")
        print("   pip install reportlab")
