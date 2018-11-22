from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# buzzwords from cvcompiler.com
buzzwords = ['Deployment', 'Security', 'API', 'Scalability', 'OOP', 'Continuous Integration (CI)', 'Availability', 'Docker', 'SOLID', 'NoSQL', 'Configuration Management (CM)', 'Robust Tuning Algorithm', 'Web services', 'Networking', 'Design Patterns', 'Unit testing', 'Open Source', 'AWS', 'Hadoop', 'Continuous Deployment (CD)', 'REST', 'Big Data', 'Agile', 'TDD', 'Machine Learning', 'Microservices', 'Artificial Intelligence', 'GitHub', 'Linux', 'Stanford']

# randomly pick 12 buzzwords
sample = random.sample(buzzwords, 12)
added_text = " ".join(sample)

# build a new PDF with stuffed keywords
packet = StringIO.StringIO()
can = canvas.Canvas(packet, pagesize=A4)
can.setFont('Helvetica', 6) # font and size
can.setFillColorRGB(1, 1, 1) # white text color
can.drawString(0, 66, added_text) # add the buzzwords
can.save()
packet.seek(0)
new_pdf = PdfFileReader(packet)

# merge our newly created PDF with the existing input.pdf
existing_pdf = PdfFileReader(file("input.pdf", "rb"))
output = PdfFileWriter()
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
outputStream = file("output.pdf", "wb")
output.write(outputStream)
outputStream.close()
