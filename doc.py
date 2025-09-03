from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem

# File path
file_path = "Nextjs_Navigation_Report.pdf"

# Create PDF document
doc = SimpleDocTemplate(file_path, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Custom styles
title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Heading1"],
    fontSize=16,
    spaceAfter=12,
    alignment=1,
)
section_style = ParagraphStyle(
    "SectionStyle",
    parent=styles["Heading2"],
    fontSize=13,
    spaceAfter=6,
)
body_style = styles["Normal"]
body_style.spaceAfter = 10

# Title
story.append(Paragraph("📘 Next.js Learning Journal", title_style))
story.append(Paragraph("Date: July 1, 2025", body_style))
story.append(Paragraph("Topic: Navigation in Next.js", section_style))
story.append(Spacer(1, 12))

# Content
content = [
    "🔗 <b>&lt;Link&gt; Component (Client-Side Navigation)</b><br/>"
    "Next.js uses the <b>&lt;Link&gt;</b> component from <b>next/link</b> for smooth client-side navigation (no full page reload).",

    "<b>Basic Example:</b><br/><br/>"
    "<font face='Courier'>"
    "import Link from 'next/link';<br/><br/>"
    "export default function Home() {<br/>"
    "&nbsp;&nbsp;return (<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;&lt;div&gt;<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;h1&gt;Home&lt;/h1&gt;<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;Link href='/about'&gt;Go to About&lt;/Link&gt;<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;&lt;/div&gt;<br/>"
    "&nbsp;&nbsp;);<br/>"
    "}<br/>"
    "</font>",

    "✅ <b>Link</b> is fast and works just like a single-page app (SPA) navigation.",

    "🧭 <b>useRouter Hook (Programmatic Navigation & Route Info)</b><br/>"
    "From <b>next/navigation</b> (for App Router), <b>useRouter</b> lets us:",
]

story.append(Paragraph(content[0], body_style))
story.append(Spacer(1, 6))
story.append(Paragraph(content[1], body_style))
story.append(Spacer(1, 6))
story.append(Paragraph(content[2], body_style))
story.append(Spacer(1, 12))
story.append(Paragraph(content[3], body_style))
story.append(Spacer(1, 6))

# Bullet points for useRouter features
points = [
    "Navigate programmatically",
    "Get current path",
    "Replace history, etc.",
]
story.append(ListFlowable([ListItem(Paragraph(p, body_style)) for p in points], bulletType="bullet"))
story.append(Spacer(1, 12))

# Example for useRouter
use_router_example = (
    "<b>Example:</b><br/><br/>"
    "<font face='Courier'>"
    "\"use client\";<br/>"
    "import { useRouter } from 'next/navigation';<br/><br/>"
    "export default function Contact() {<br/>"
    "&nbsp;&nbsp;const router = useRouter();<br/><br/>"
    "&nbsp;&nbsp;const handleClick = () => {<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;router.push('/thank-you');<br/>"
    "&nbsp;&nbsp;};<br/><br/>"
    "&nbsp;&nbsp;return &lt;button onClick={handleClick}&gt;Submit & Go&lt;/button&gt;;<br/>"
    "}<br/>"
    "</font>"
)
story.append(Paragraph(use_router_example, body_style))
story.append(Spacer(1, 12))

# Notes
story.append(Paragraph("📝 <b>Notes:</b>", section_style))
story.append(Paragraph("- useRouter() is only available in Client Components (requires <b>\"use client\"</b> at the top).", body_style))
story.append(Paragraph("- In the App Router, useRouter comes from <b>next/navigation</b>, not <b>next/router</b>.", body_style))

# Build PDF
doc.build(story)
file_path
