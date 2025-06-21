import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

def send_email_report(desc, tag, image_path, lat, lon):
    # Sender and receiver details
    sender_email = "zaararawat08@gmail.com"
    receiver_email = "eniyasre05@gmail.com"
    app_password = "oksdnfbrpjkwugkf"  # App-specific password from Gmail

    subject = f"🛠️ New Civic Issue Reported: {tag}"

    # Create MIMEMultipart message
    msg = MIMEMultipart("related")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Email content
    text = f"""
New Civic Issue Reported:

Tag: {tag}
Description: {desc}
Location: https://maps.google.com/?q={lat},{lon}
Image is attached below.
"""

    html = f"""
    <html>
        <body>
            <h2>🛠️ New Civic Issue Reported</h2>
            <p><strong>Tag:</strong> {tag}</p>
            <p><strong>Description:</strong> {desc}</p>
            <p><strong>Location:</strong> <a href="https://maps.google.com/?q={lat},{lon}">View on Map</a></p>
            <p><img src="cid:issue_image" style="max-width: 400px; margin-top: 10px;" /></p>
        </body>
    </html>
    """

    # Attach plain text and HTML parts
    alt_part = MIMEMultipart("alternative")
    alt_part.attach(MIMEText(text, "plain"))
    alt_part.attach(MIMEText(html, "html"))
    msg.attach(alt_part)

    # Attach the image (inline display with cid)
    try:
        with open(image_path, 'rb') as img:
            mime_img = MIMEImage(img.read())
            mime_img.add_header('Content-ID', '<issue_image>')
            mime_img.add_header('Content-Disposition', 'inline', filename=os.path.basename(image_path))
            msg.attach(mime_img)
    except FileNotFoundError:
        print("⚠️ Image file not found, sending without image.")

    # Send email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Error sending email: {e}")
