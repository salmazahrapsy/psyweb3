"""Build the PsyWeb3 static site into ./site (pure Python, no dependencies).

Edit SIGNUP_URL and CONTACT_EMAIL below, then run:  python3 build.py
GitHub Actions runs this automatically on every push and deploys ./site to GitHub Pages.
All links are relative, so the site works at https://salmazahrapsy.github.io/psyweb3/
or on a custom domain without changes.
"""
import html, os, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "site")
BASE = "https://salmazahrapsy.github.io/psyweb3/"

# ---- Settings Salma fills in -------------------------------------------------
SIGNUP_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdHkWdobLz43sIWRbDkrBCIzHyt1PH5h_hD041nnxcrDIYb2Q/viewform"  # Google Form. Empty = signup button hidden.
CONTACT_EMAIL = "psyweb3@zohomail.com"   # a PsyWeb3 email you are happy to publish. Empty = GitHub only.
UPDATED = datetime.date.today().isoformat()
# -----------------------------------------------------------------------------

PAGES = [("index.html", "Home"), ("reading-list.html", "Starter reading list"),
         ("research.html", "Research"), ("about.html", "About"), ("privacy.html", "Privacy")]


OG = (f'<meta property="og:image" content="{BASE}assets/og.png">\n<meta name="twitter:card" content="summary_large_image">\n'
      if os.path.exists(os.path.join(OUT, "assets", "og.png")) else "")


def page(fname, title, desc, body):
    nav = "".join(f'<a href="{f}"{" aria-current=\"page\"" if f == fname else ""}>{t}</a>'
                  for f, t in PAGES[:4])
    canon = BASE + ("" if fname == "index.html" else fname)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="PsyWeb3">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}">
{OG}<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <a class="brand" href="index.html">PsyWeb3</a>
  <nav aria-label="Main">{nav}</nav>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <p><strong>PsyWeb3</strong> is operated by PT Psyweb Tiga Indonesia. Founder: Salma Zahra.</p>
  <p><a href="privacy.html">Privacy</a> · <a href="https://github.com/salmazahrapsy">GitHub</a>{(' · ' + html.escape(CONTACT_EMAIL)) if CONTACT_EMAIL else ''} · Updated {UPDATED}</p>
  <p class="small">Educational and research content only. Not clinical, therapeutic or financial advice.</p>
</footer>
</body>
</html>
"""
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(doc)


signup = (f'<p>Join the PsyWeb3 list for new research notes and reading lists. Psychology students and young researchers can also volunteer for a 20–30 minute online interview about their research needs.</p>'
          f'<p><a class="button" href="{html.escape(SIGNUP_URL)}">Sign up / Daftar</a></p>'
          '<p class="small">The form (Google Forms) asks for your email, name, role, affiliation, country and research interests. See <a href="privacy.html">Privacy</a>.</p>'
          if SIGNUP_URL else
          '<p class="notice">Email updates open soon. Meanwhile, start with the <a href="reading-list.html">free starter reading list</a>.</p>')

ORG_LD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","name":"PsyWeb3",
 "legalName":"PT Psyweb Tiga Indonesia","url":"https://salmazahrapsy.github.io/psyweb3/",
 "founder":{"@type":"Person","name":"Salma Zahra","url":"https://salmazahrapsy.github.io/"},
 "description":"Research and education studio on human behaviour in decentralised and online communities."}
</script>"""

page("index.html", "PsyWeb3 — Understanding human behaviour in decentralised communities",
     "PsyWeb3 turns psychology research into practical guides for students and researchers studying online and Web3 communities.",
f"""{ORG_LD}
<section class="hero">
  <p class="eyebrow">Psychology × Web3 · Research &amp; education</p>
  <h1>Understanding human behaviour in decentralised communities.</h1>
  <p class="lede">PsyWeb3 turns psychology research into clear, sourced guides for students and researchers who study online and Web3 communities: trust, identity, participation and wellbeing.</p>
  <p class="cta"><a class="button" href="reading-list.html">Free starter reading list</a> <a class="button ghost" href="research.html">Research in progress</a></p>
</section>

<section aria-labelledby="who">
  <h2 id="who">Who it is for</h2>
  <div class="cards">
    <div class="card"><h3>Psychology students</h3><p>Especially final-year students planning a thesis on digital or online behaviour.</p></div>
    <div class="card"><h3>Early-career researchers</h3><p>Social scientists who need a reliable starting point on Web3 communities.</p></div>
    <div class="card"><h3>Community builders</h3><p>People who run online communities and want evidence, not hype, about how members behave.</p></div>
  </div>
</section>

<section aria-labelledby="how">
  <h2 id="how">How we work</h2>
  <ul class="ticks">
    <li><strong>Every source verified.</strong> Each citation is checked against its DOI or original page before we use it.</li>
    <li><strong>Claims labelled.</strong> We mark what is established research, what is Web3-specific evidence, and what is still a hypothesis.</li>
    <li><strong>Ethics first.</strong> Informed consent and data minimisation for anything involving people, under Indonesia's Personal Data Protection Law (UU 27/2022). No identifiable psychological data.</li>
    <li><strong>Non-clinical.</strong> We do not diagnose, treat or give individual psychological or financial advice.</li>
  </ul>
</section>

<section aria-labelledby="join">
  <h2 id="join">Stay in touch</h2>
  {signup}
</section>

<section aria-labelledby="id-summary" lang="id">
  <h2 id="id-summary">Dalam Bahasa Indonesia</h2>
  <p>PsyWeb3 adalah studio riset dan edukasi tentang perilaku manusia di komunitas online dan Web3. Kami menyusun panduan berbasis riset psikologi untuk mahasiswa dan peneliti, terutama mahasiswa psikologi yang sedang menyiapkan skripsi tentang perilaku digital. Semua sumber diverifikasi, dan konten kami bersifat edukatif, bukan layanan klinis.</p>
</section>
""")

REFS = [
 ("Trust", "Mayer, R. C., Davis, J. H., &amp; Schoorman, F. D. (1995). An integrative model of organizational trust. <em>Academy of Management Review, 20</em>(3), 709–734.", "10.5465/amr.1995.9508080335",
  "The ability–benevolence–integrity model of trustworthiness. The backbone for thinking about whom people trust in a community.", "Established"),
 ("Trust", "Gaggioli, A., Eskandari, S., Cipresso, P., &amp; Lozza, E. (2019). The middleman is dead, long live the middleman: The “trust factor” and the psycho-social implications of blockchain. <em>Frontiers in Blockchain, 2</em>, 20.", "10.3389/fbloc.2019.00020",
  "A perspective piece that sets out a psychology research agenda for blockchain. Cite it as an argument, not as evidence.", "Perspective"),
 ("Trust", "Prados-Castillo, J. F., Martín, J. M. M., Alexeeva-Alexeev, I., &amp; Guaita-Martínez, J. M. (2025). Understanding blockchain by digital natives: Innovation, trust and psychological factors. <em>Journal of Innovation &amp; Knowledge, 10</em>(6), 100806.", "10.1016/j.jik.2025.100806",
  "Survey of young adults in Spain: trust, perceived usefulness and perceived risk drive blockchain adoption; experienced users are more critical.", "Web3 evidence"),
 ("Governance", "Feichtinger, R., Fritsch, R., Vonlanthen, Y., &amp; Wattenhofer, R. (2023). The hidden shortcomings of (D)AOs – An empirical study of on-chain governance. In <em>Financial Cryptography and Data Security. FC 2023 International Workshops</em> (pp. 165–185). Springer.", "10.1007/978-3-031-48806-1_11",
  "Data from 21 DAOs: voting power is highly concentrated, governance has hidden costs, and much voting activity is pointless.", "Web3 evidence"),
 ("Identity", "Tajfel, H., &amp; Turner, J. C. (1979). An integrative theory of intergroup conflict. In W. G. Austin &amp; S. Worchel (Eds.), <em>The social psychology of intergroup relations</em>. Brooks/Cole.", "",
  "Social identity theory: why belonging to a group shapes how people treat insiders and outsiders.", "Established"),
 ("Identity", "Postmes, T., Spears, R., &amp; Lea, M. (1998). Breaching or building social boundaries? SIDE-effects of computer-mediated communication. <em>Communication Research, 25</em>(6), 689–715.", "10.1177/009365098025006006",
  "How anonymity online can strengthen, not weaken, group identity.", "Established"),
 ("Participation", "Ren, Y., Kraut, R., &amp; Kiesler, S. (2007). Applying common identity and bond theory to design of online communities. <em>Organization Studies, 28</em>(3), 377–408.", "10.1177/0170840607076007",
  "Two routes to commitment: attachment to the group versus attachment to individual members.", "Established"),
 ("Participation", "Kraut, R. E., &amp; Resnick, P. (with Kiesler, S., et al.) (2012). <em>Building successful online communities: Evidence-based social design</em>. MIT Press.", "10.7551/mitpress/8472.001.0001",
  "Evidence-based design claims for starting, growing and governing online communities.", "Established"),
 ("Wellbeing", "Suler, J. (2004). The online disinhibition effect. <em>CyberPsychology &amp; Behavior, 7</em>(3), 321–326.", "10.1089/1094931041291295",
  "Why people say and do things online they would not do face to face.", "Established"),
 ("Wellbeing", "Ellison, N. B., Steinfield, C., &amp; Lampe, C. (2007). The benefits of Facebook “friends”: Social capital and college students' use of online social network sites. <em>Journal of Computer-Mediated Communication, 12</em>(4), 1143–1168.", "10.1111/j.1083-6101.2007.00367.x",
  "Online networks and social capital among students.", "Established"),
]
items = ""
for theme, cite, doi, note, label in REFS:
    link = f' <a href="https://doi.org/{doi}">doi:{doi}</a>' if doi else ""
    items += f'<li><span class="label">{theme}</span> <span class="label">{label}</span><br>{cite}{link}<br><span class="small">{note}</span></li>\n'

page("reading-list.html", "Starter Reading List: Psychology of Web3 Communities | PsyWeb3",
     "Ten verified sources to start research on trust, identity, participation and wellbeing in online and Web3 communities.",
f"""<article class="prose">
<h1>Starter reading list</h1>
<p class="lede">Ten sources to start a psychology project on online and Web3 communities. Each citation was checked against its DOI or publisher record.</p>
<p class="small">Labels: <strong>Established</strong> = classic psychology or online-community research · <strong>Web3 evidence</strong> = empirical work on blockchain or DAOs · <strong>Perspective</strong> = argument or agenda, not data.</p>
<ol class="refs">
{items}</ol>
<h2>How to use it</h2>
<ol>
  <li>Start with Mayer et al. (1995) and Tajfel &amp; Turner (1979): trust and identity are the two lenses most Web3 questions need.</li>
  <li>Read one Web3 evidence paper and ask which psychological construct it actually measures.</li>
  <li>Look for a gap: most Web3 evidence comes from Europe and the United States, so Indonesian samples are rare.</li>
</ol>
</article>
""")

page("research.html", "Research in Progress | PsyWeb3",
     "PsyWeb3 research notes in progress: the psychology of trust in Web3 communities, and a framework for studying online communities.",
"""<article class="prose">
<h1>Research in progress</h1>
<table>
 <thead><tr><th scope="col">Note</th><th scope="col">Question</th><th scope="col">Status</th></tr></thead>
 <tbody>
  <tr><td>#1 The Psychology of Trust in Web3 Communities</td><td>How do people decide whom to trust when members are pseudonymous and rules are written in code?</td><td>Drafting</td></tr>
  <tr><td>#2 Digital Behaviour and Online Communities: A Psychology-Based Research Framework</td><td>Which psychological theories give students a sound starting point for studying online communities?</td><td>Sources being collected</td></tr>
  <tr><td>#3 Human Behaviour, AI and Digital Wellbeing</td><td>What does evidence say about wellbeing in AI-mediated online spaces?</td><td>Planned</td></tr>
 </tbody>
</table>
<p>Notes are published here once each source is verified and the text has been reviewed by the founder.</p>
<h2>Thesis ideas for students</h2>
<ul>
  <li>Replicate a trust and blockchain adoption model with Indonesian university students, adding perceived risk as its own construct. Check national databases (Garuda, SINTA) for prior work first.</li>
  <li>Compare commitment to the group versus commitment to individual members (common identity versus common bond) in an Indonesian online community.</li>
</ul>
<p class="small">These are hypotheses to test, not findings.</p>
</article>
""")

page("about.html", "About PsyWeb3 | PT Psyweb Tiga Indonesia",
     "About PsyWeb3, a research and education studio founded by Salma Zahra and operated by PT Psyweb Tiga Indonesia.",
f"""<article class="prose">
<h1>About</h1>
<p class="lede">PsyWeb3 is a research and education studio on human behaviour in decentralised and online communities, founded by <a href="https://salmazahrapsy.github.io/">Salma Zahra</a>, a Psychology undergraduate in Indonesia.</p>
<dl class="facts">
  <dt>Legal entity</dt><dd>PT Psyweb Tiga Indonesia</dd>
  <dt>Founder</dt><dd>Salma Zahra (authorised signatory)</dd>
  <dt>Focus</dt><dd>Trust, identity, participation and wellbeing in online and Web3 communities</dd>
  <dt>Languages</dt><dd>English; Bahasa Indonesia</dd>
</dl>
<h2>Roadmap</h2>
<ol>
  <li><strong>Research-led education</strong>: sourced notes and reading lists.</li>
  <li><strong>Digital knowledge products</strong>: research starter kits for students.</li>
  <li><strong>An AI-enabled research platform</strong>, only after demand is proven.</li>
</ol>
<h2>Contact</h2>
<p>{('Email: ' + html.escape(CONTACT_EMAIL) + ' · ') if CONTACT_EMAIL else ''}GitHub: <a href="https://github.com/salmazahrapsy">salmazahrapsy</a></p>
</article>
""")

page("privacy.html", "Privacy | PsyWeb3",
     "How PsyWeb3 handles personal data under Indonesia's Personal Data Protection Law (UU 27/2022).",
f"""<article class="prose">
<h1>Privacy</h1>
<p class="lede">This website itself sets no cookies, runs no analytics and collects no personal data. Personal data is collected only if you fill in the signup form.</p>
<h2>If you use the signup form</h2>
<ul>
  <li><strong>What we collect:</strong> email address, name or preferred name, current role, university or affiliation (optional), country and time zone, research interests, familiarity with Web3, an optional open question, interview preference, preferred language, and your consent.</li>
  <li><strong>Why:</strong> to send PsyWeb3 updates and reading lists, and, only if you say yes, to arrange a research interview.</li>
  <li><strong>Where it is stored:</strong> the form runs on Google Forms and answers are kept in a Google Sheet controlled by PT Psyweb Tiga Indonesia. Google processes the data as the service provider.</li>
  <li><strong>How long:</strong> only as long as needed for these purposes. We delete your answers when you ask.</li>
  <li><strong>Your rights:</strong> you can ask to see, correct or delete your data, or withdraw consent, at any time by emailing {html.escape(CONTACT_EMAIL) if CONTACT_EMAIL else 'us'}, in line with Indonesia's Personal Data Protection Law (UU No. 27 Tahun 2022). Every email includes a way to unsubscribe.</li>
  <li>We never sell your data or share it outside PsyWeb3.</li>
</ul>
<h2>Research participation</h2>
<p>Interviews and surveys use informed consent, keep notes anonymous, and never record without your agreement. You can stop at any time.</p>
<p class="small">Hosted on GitHub Pages; GitHub may log technical data such as IP addresses for security. See GitHub's privacy statement. Updated {UPDATED}.</p>
</article>
""")

with open(os.path.join(OUT, "404.html"), "w") as f:
    f.write("""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Page not found | PsyWeb3</title><meta name="robots" content="noindex"><link rel="stylesheet" href="/psyweb3/assets/site.css"></head><body><main class="prose"><h1>Page not found</h1><p><a href="/psyweb3/">Back to PsyWeb3</a></p></main></body></html>""")
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for fn, _ in PAGES:
        f.write(f"  <url><loc>{BASE}{'' if fn == 'index.html' else fn}</loc><lastmod>{UPDATED}</lastmod></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
print("Built", len(PAGES), "pages into", OUT)
