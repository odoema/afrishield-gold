"""Build specimen licence/compliance PDFs for the AfriShield Gold class-project website.
Every page is watermarked SPECIMEN and states it has no legal effect. No government
crests, seals or signatures are reproduced."""
import os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle, Frame, Spacer
from reportlab.lib.styles import ParagraphStyle

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
NAVY = colors.HexColor('#1b1510'); GOLD = colors.HexColor('#c9a24a'); GOLD_D = colors.HexColor('#8a6a2a')
LOGO = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'afrishield-shield.png')
GREY = colors.HexColor('#f3f1ea'); MUTED = colors.HexColor('#5b6270'); RED = colors.HexColor('#b42318')
W, H = A4

body = ParagraphStyle('b', fontName='Helvetica', fontSize=9.5, leading=13.5, textColor=colors.HexColor('#1d2330'))
small = ParagraphStyle('s', parent=body, fontSize=8, leading=11, textColor=MUTED)
h2 = ParagraphStyle('h2', parent=body, fontName='Helvetica-Bold', fontSize=11, leading=15, spaceBefore=8, spaceAfter=4, textColor=NAVY)
cell = ParagraphStyle('c', parent=body, fontSize=9, leading=12)
cellb = ParagraphStyle('cb', parent=cell, fontName='Helvetica-Bold')

DISCLAIMER = ("SPECIMEN FOR AN ACADEMIC BUSINESS-CLASS PROJECT. AfriShield Gold Ltd is a hypothetical company. "
              "This document is not a licence, permit, certificate or registration, has no legal effect and must not be "
              "relied on for any transaction. Always verify a real licence directly with the issuing authority.")

DOCS = [
  dict(file='afrishield-certificate-of-incorporation-specimen.pdf',
       title='Company Registration Summary', kind='Licence register extract',
       authority='Uganda Registration Services Bureau (URSB)', law='Companies Act, 2012',
       rows=[('Company name','AfriShield Gold Ltd (hypothetical)'),('Registration no.','SPEC-AFG-URSB-0001'),
             ('Company type','Private company limited by shares'),('Registered office','Kampala Business District, Uganda'),
             ('Principal activity','Dealing in, refining arrangements for and export of precious metals'),
             ('Status','Specimen only: not registered')],
       notes=['Real company details can be searched on the URSB online registry.']),
  dict(file='afrishield-mineral-dealers-licence-specimen.pdf',
       title="Mineral Dealer's Licence (Precious Metals)", kind='Licence register extract',
       authority='Ministry of Energy and Mineral Development (MEMD)', law='Mining and Minerals Act, 2022',
       rows=[('Licence holder','AfriShield Gold Ltd (hypothetical)'),('Licence no.','SPEC-AFG-MDL-0002'),
             ('Category','Precious metals (gold)'),('Validity','Calendar year; expires 31 December of the year of issue'),
             ('Conditions','Buy and sell only with holders of a mining, dealer or refining licence; keep records of every transaction'),
             ('Status','Specimen only: not issued')],
       notes=["Requirements for a dealer's licence include proof of financial resources, a URA tax clearance certificate and evidence of technical competence.",
              'Real licences should be checked on the Mining Cadastre and Registry System or with MEMD.']),
  dict(file='afrishield-mining-cadastre-registration-specimen.pdf',
       title='Mining Cadastre Registration', kind='Licence register extract',
       authority='Mining Cadastre and Registry System (MEMD)', law='Mining and Minerals Act, 2022',
       rows=[('Registered party','AfriShield Gold Ltd (hypothetical)'),('Cadastre account','SPEC-AFG-MCR-0003'),
             ('Role','Buyer and seller of precious metals'),('Documents on file','Certificate of incorporation, memorandum and articles, board resolution, TIN'),
             ('Status','Specimen only: not registered')],
       notes=['Buyers and sellers of gold must register on the electronic Mining Cadastre before trading.']),
  dict(file='afrishield-fia-aml-registration-specimen.pdf',
       title='AML / CFT Registration', kind='Licence register extract',
       authority='Financial Intelligence Authority (FIA), Uganda', law='Anti-Money Laundering Act, 2013 (as amended)',
       rows=[('Accountable person','AfriShield Gold Ltd (hypothetical)'),('Reference','SPEC-AFG-FIA-0004'),
             ('Sector','Dealers in precious metals and stones'),('Obligations','Customer due diligence, record keeping, suspicious transaction reporting, compliance officer'),
             ('Status','Specimen only: not registered')],
       notes=['Dealers in precious metals are accountable persons under Uganda\'s anti-money-laundering law.']),
  dict(file='afrishield-export-permit-specimen.pdf',
       title='Export Permit: Sample Consignment Record', kind='Permit register extract',
       authority='Ministry of Energy and Mineral Development (MEMD)', law='Mining and Minerals Regulations, 2023 (Form 52)',
       rows=[('Exporter','AfriShield Gold Ltd (hypothetical)'),('Permit no.','SPEC-AFG-EXP-0005'),
             ('Consignment','Refined gold bars, 99.9% fineness'),('Destination','Supervised refiner / buyer, Dubai, UAE'),
             ('Supporting documents','Valid mineral right or refining licence, certificate of origin, certificate of analysis, royalty receipts'),
             ('Status','Specimen only: not issued')],
       notes=['A separate export permit is needed for every consignment.', 'Gold must be refined to 99.9% purity before export.']),
  dict(file='afrishield-oecd-due-diligence-policy.pdf',
       title='Responsible Gold Supply Chain Policy', kind='Company policy (OECD Annex II aligned)',
       authority='AfriShield Gold Ltd board (hypothetical)', law='OECD Due Diligence Guidance for Responsible Supply Chains of Minerals',
       rows=[('Policy owner','Compliance Officer'),('Reference','SPEC-AFG-POL-0006'),('Review cycle','Annual, or after any red-flag event')],
       notes=[],
       policy=[('1. Commitment','We will not tolerate, profit from, contribute to or facilitate serious human-rights abuses, direct or indirect support to non-state armed groups or public or private security forces acting illegally, bribery, fraudulent misrepresentation of origin, or money laundering.'),
               ('2. Management systems','A named compliance officer, a KYC procedure for every counterparty, and chain-of-custody records kept for at least five years.'),
               ('3. Risk assessment','Every source is mapped and checked for red flags: conflict-affected location, unlicensed sellers, unexplained volumes or cash-only terms.'),
               ('4. Risk mitigation','Red-flag lots are suspended until resolved; supplier relationships are ended where risks cannot be mitigated.'),
               ('5. Audit and reporting','Independent third-party audit of our due diligence and an annual public report on our supply chain.')]),
]

def draw_page(c, d):
    # header band
    c.setFillColor(NAVY); c.rect(0, H-3.2*cm, W, 3.2*cm, fill=1, stroke=0)
    c.drawImage(LOGO, 1.6*cm, H-2.75*cm, width=1.6*cm*253/304, height=1.6*cm, mask='auto')
    c.setFillColor(colors.white); c.setFont('Helvetica-Bold', 15); c.drawString(3.4*cm, H-1.65*cm, 'AFRISHIELD GOLD LTD')
    c.setFillColor(colors.HexColor('#c9ccd3')); c.setFont('Helvetica', 8.5)
    c.drawString(3.4*cm, H-2.15*cm, 'Secure. Ethical. African Gold.  ·  Hypothetical company, business class project')
    c.setFillColor(GOLD); c.setFont('Helvetica-Bold', 9); c.drawRightString(W-1.6*cm, H-1.65*cm, d['kind'].upper())
    c.setFillColor(GOLD); c.rect(0, H-3.3*cm, W, 0.1*cm, fill=1, stroke=0)
    # red specimen banner
    c.setFillColor(RED); c.rect(1.6*cm, H-4.35*cm, W-3.2*cm, 0.75*cm, fill=1, stroke=0)
    c.setFillColor(colors.white); c.setFont('Helvetica-Bold', 9.5)
    c.drawCentredString(W/2, H-4.08*cm, 'SPECIMEN · ACADEMIC PROJECT · NOT A VALID LICENCE OR PERMIT')
    # watermark
    c.saveState(); c.translate(W/2, H/2-1*cm); c.rotate(35)
    c.setFillColor(colors.Color(0.71, 0.14, 0.09, alpha=0.10)); c.setFont('Helvetica-Bold', 64)
    c.drawCentredString(0, 30, 'SPECIMEN'); c.setFont('Helvetica-Bold', 26); c.drawCentredString(0, -20, 'NO LEGAL EFFECT')
    c.restoreState()
    # footer
    c.setStrokeColor(GOLD); c.setLineWidth(1); c.line(1.6*cm, 2.9*cm, W-1.6*cm, 2.9*cm)
    f = Frame(1.6*cm, 0.9*cm, W-3.2*cm, 1.9*cm, showBoundary=0, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    f.addFromList([Paragraph('<b>Disclaimer.</b> ' + DISCLAIMER, small)], c)

def build(d):
    path = os.path.join(OUT, d['file'])
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle(d['title'] + ' (Specimen) | AfriShield Gold Ltd'); c.setAuthor('AfriShield Gold class project')
    c.setSubject('Specimen document for an academic project. No legal effect.')
    draw_page(c, d)
    story = [Paragraph(d['title'], ParagraphStyle('t', parent=body, fontName='Times-Bold', fontSize=20, leading=24, textColor=NAVY)),
             Spacer(1, 4),
             Paragraph(f"Relevant authority: <b>{d['authority']}</b><br/>Legal basis: {d['law']}", body), Spacer(1, 10)]
    t = Table([[Paragraph(k, cellb), Paragraph(v, cell)] for k, v in d['rows']], colWidths=[4.6*cm, W-3.2*cm-4.6*cm])
    t.setStyle(TableStyle([('BACKGROUND', (0,0), (0,-1), GREY), ('BOX', (0,0), (-1,-1), 0.6, GOLD_D),
                           ('INNERGRID', (0,0), (-1,-1), 0.4, colors.HexColor('#d9d4c4')), ('VALIGN', (0,0), (-1,-1), 'TOP'),
                           ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6), ('LEFTPADDING', (0,0), (-1,-1), 7)]))
    story.append(t)
    for head, text in d.get('policy', []):
        story += [Paragraph(head, h2), Paragraph(text, body)]
    if d['notes']:
        story += [Spacer(1, 6), Paragraph('Notes for the reader', h2)]
        story += [Paragraph('• ' + n, body) for n in d['notes']]
    story += [Spacer(1, 10), Paragraph('Issued for: classroom demonstration of the documents a legitimate gold trader would hold. '
                                       'No crest, seal or signature of any authority is reproduced.', small)]
    Frame(1.6*cm, 3.2*cm, W-3.2*cm, H-4.8*cm-3.2*cm, showBoundary=0, leftPadding=0, rightPadding=0).addFromList(story, c)
    c.showPage(); c.save()
    return path

for d in DOCS:
    print(build(d))
