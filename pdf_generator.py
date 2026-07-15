from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import re


def clean_text(text):

    # Remove emojis
    text = text.encode("ascii", "ignore").decode()

    # Remove markdown headers
    text = re.sub(r"#", "", text)

    # Convert bullet points
    text = text.replace("•", "-")

    return text


def create_pdf(itinerary, destination):

    filename = "Travel_Plan.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Travel Planner Agent</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Destination:</b> {destination}", styles["Heading2"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    itinerary = clean_text(itinerary)

    for line in itinerary.split("\n"):

        if line.strip() != "":

            story.append(
                Paragraph(line, styles["BodyText"])
            )

    doc.build(story)

    return filename