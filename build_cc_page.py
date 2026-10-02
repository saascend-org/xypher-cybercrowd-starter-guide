import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_cc_css, build_cc_js, build_cc_data
IMGS = json.load(open(os.path.join(HERE, 'imgs.json')))   # [DEMO]-record screenshots from the DXR guide
S = build_cc_data.STAGES
for _s in S: _s['what'] = _s['what'] + ' (In HubSpot: ' + _s['hs'] + '.)'

def path(*bits):
    out=[]
    for b in bits:
        if b == '>': out.append('<i>&rsaquo;</i>')
        elif b.startswith('!'): out.append(f'<span class="btn">{b[1:]}</span>')
        else: out.append(f'<span>{b}</span>')
    return '<div class="path">' + ''.join(out) + '</div>'

def fig(i, cap):
    return (f'<figure><img loading="lazy" alt="{cap}" src="{IMGS[i]}">'
            f'<figcaption>{cap}</figcaption></figure>')

def step(n, sid, title, sub, body):
    return (f'<li data-step="{sid}"><div class="head"><span class="num"><span>{n}</span></span>'
            f'<span class="ttl"><b>{title}</b><em>{sub}</em></span>'
            f'<span class="tick">Mark done</span>'
            f'<span class="chev" aria-hidden="true">&rsaquo;</span></div>'
            f'<div class="body">{body}</div></li>')

def table(head, rows):
    h = ''.join(f'<th>{c}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<div class="tblwrap"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

LOGIN = [
 step(1,'l1','Go to the Xypher login page','xypher.my.salesforce.com',
   '<p>Open <strong>https://xypher.my.salesforce.com</strong> and bookmark it. This is the only address you need.</p>'),
 step(2,'l2','Click Log in with AzureSSO','The Microsoft button, not the username box',
   '<p>Below the username and password boxes is a button for <strong>AzureSSO</strong>. Click it.</p>'
   '<div class="note warn"><span class="tag">Do not use the username and password boxes</span>'
   '<p>You do not have a Salesforce password &mdash; your login is your Microsoft account. '
   'Typing your email into the username box will not work.</p></div>'),
 step(3,'l3','Sign in with your DXR Cyber Microsoft account','firstname.lastname@dxrcyber.com',
   '<p>Microsoft asks for your account. Use your <strong>@dxrcyber.com</strong> address &mdash; '
   '<code>firstname.lastname@dxrcyber.com</code> &mdash; and approve the sign-in as you normally would. '
   'Salesforce opens on its own.</p>'
   '<div class="note"><span class="tag">If it fails</span>'
   '<p>Do not keep retrying or try other accounts. Screenshot the message and send it to Kristian, '
   'who will pass it to SaaScend &mdash; we can see exactly why it failed.</p></div>'),
 step(4,'l4','Open the Sales app','Top left, the nine dots',
   '<p>Click the nine-dot <strong>App Launcher</strong> and choose <strong>Sales</strong>. That is '
   'where the tabs below live.</p>' + path('!App Launcher','>','!Sales')),
]

ORDER = [
 step(1,'o1','Get the deal ready','Products on, amount right',
   '<p>The form is built from the deal. It needs <strong>products</strong> on the deal, and the products '
   'must add up to the deal <strong>Amount</strong>. Add them from the <strong>Products</strong> panel.</p>'),
 step(2,'o2','Click Create CyberCrowd Order Form','Top right of an open deal',
   '<p>On any open CyberCrowd deal, the button sits in the row at the top right, next to '
   '<strong>Edit</strong>. If you cannot see it, click the <strong>&#9662;</strong> at the end of that row.</p>'
   + path('Opportunity','>','!Create CyberCrowd Order Form')),
 step(3,'o3','Check and adjust','Bill-to, contact, expiry, wording',
   '<p>The screen shows everything pulled from the deal. Change the bill-to company, contact, expiry '
   'date, comments or the wording of any line if you need to, then create it.</p>'),
 step(4,'o4','Download and send it yourself','It is saved to Files',
   '<p>The PDF is in the CyberCrowd quote design and is saved to the deal&rsquo;s <strong>Files</strong>. '
   '<strong>Salesforce does not email it</strong> &mdash; download it and send it to the customer as you do now. '
   'Each new version gets its own reference (<code>DXR-21654-v1</code>, <code>-v2</code>&hellip;).</p>'),
]

CLOSE = [
 step(1,'c1','Close from the path, not the Stage field','Closed, then Closed Won',
   '<p>On the stage path at the top of the deal, choose <strong>Closed</strong>, then <strong>Closed Won</strong>. '
   'That opens the <strong>work package form</strong>. Editing the Stage field directly will be refused.</p>'),
 step(2,'c2','Fill in the work package','What Projects and Finance need',
   '<p>The form asks for the contract details and a short outline of the work. The '
   '<strong>Order Form No.</strong> is filled in from your latest order form.</p>'),
 step(3,'c3','Submit','Salesforce does the hand-over',
   '<p>On submit the deal closes and Salesforce emails the <strong>work order</strong> to the projects team '
   'and the <strong>invoice request</strong> to finance, copying Kristian. Nothing else to send.</p>'
   '<p>If something was wrong, use <strong>Resend Work Package</strong> on the closed deal.</p>'),
]

TIDY = [
 step(1,'t1','Open My Opportunities','Every open CyberCrowd deal you own',
   '<p>Click <strong>Opportunities</strong>, then switch the list to <strong>My Opportunities</strong>. '
   'Click the <strong>Close Date</strong> column to sort oldest first.</p>'
   + path('Sales app','>','!Opportunities','>','list: My Opportunities','>','sort by Close Date')
   + fig(0,'The Opportunities list view (demo records). The dropdown by the title switches lists.')),
 step(2,'t2','Close what is dead','Old HubSpot deals nobody is working',
   '<p>Your HubSpot pipeline came across as it was &mdash; including deals that stopped moving '
   'years ago. <strong>474 open CyberCrowd deals have a close date before 2026.</strong> If it is dead, '
   'move it to <strong>Closed Lost</strong> with a Loss Reason and a line of Loss Detail. '
   'Losing a deal needs no MEDDPICC evidence.</p>'),
 step(3,'t3','Fix the close date on what is alive','Your honest date',
   '<p>If the deal is real, give it the date you actually expect a decision. A past date on an open '
   'deal shows as overdue on your manager&rsquo;s report.</p>'),
 step(4,'t4','Check Service Line, set Funding Route','Two fields HubSpot never had',
   '<p>You cannot leave Qualify without either. HubSpot never had a service line, so we filled it in '
   'from the deal name &mdash; check it is right (56 deals with no clue in the name say <strong>Other</strong>). '
   'Funding Route is yours to set. Open the deal, go to <strong>Details</strong>, click the pencil, save.</p>'
   '<p>The deal name updates itself when you change the service line, type or close date.</p>'
   '<p>A Cyber Essentials or Pen Testing deal under &pound;5k needs nothing more &mdash; it skips the '
   'MEDDPICC grades.</p>'),
 step(5,'t5','Give it a Next Step with a future date','The rule every stage move checks',
   '<p>Write the next action in <strong>Next Step</strong> and a date of today or later in '
   '<strong>Next Step Date</strong>. Without it, no stage will move.</p>'),
 step(6,'t6','Move the stage when you can evidence it','Read "To Advance, Still Needed"',
   '<p>The field <strong>To Advance, Still Needed</strong> on every deal lists exactly what is missing '
   'for the next stage. Fill those, then move the stage on the path at the top.</p>'
   + fig(1,'The Sales Path with the guidance for the current stage (demo record).')),
]

DICT = table(['In HubSpot', 'In Salesforce', 'Notes'], [
 ['Company', '<strong>Account</strong>', 'Some of your companies already existed in Salesforce for DXR or Business Central. They were joined, not duplicated &mdash; you are on the <strong>Account Team</strong>.'],
 ['Contact (customer / opportunity lifecycle)', '<strong>Contact</strong>', 'People at companies you are already selling to.'],
 ['Contact (lead / subscriber / MQL / SQL)', '<strong>Lead</strong>', 'HubSpot has no Lead object; the lifecycle stage decided. Convert a Lead when it becomes a deal.'],
 ['Deal', '<strong>Opportunity</strong>', 'Same owner, amount, close date and stage (mapped below). Every deal now has a <strong>DXR- reference</strong>. Open deals are renamed the DXR way &mdash; <code>DXR-24532 - Account - Service Line - Type - Quarter</code> &mdash; and the HubSpot name is kept at the top of <strong>Legacy Details</strong>. Closed deals keep their name.'],
 ['Deal &rarr; reseller field', '<strong>Partner</strong> on the deal', 'Softcat, Bytes and the rest sit in the Partners panel, not in the deal name.'],
 ['Emails, tasks, meetings, notes', '<strong>Activity</strong> timeline', 'On the record they belonged to in HubSpot.'],
 ['Original owner, created date, stage, tags', '<strong>Legacy</strong> fields', 'Legacy Owner, Legacy Created Date, Legacy Stage, Legacy Tags &mdash; kept for reference, never edited.'],
 ['The HubSpot record itself', '<strong>Legacy Record Link</strong>', '&ldquo;Open original record&rdquo; opens it in HubSpot while HubSpot is still available.'],
])

STAGEMAP = table(['HubSpot deal stage', 'Salesforce stage', 'Forecast', 'Deals'], [
 ['10% - lead', 'Qualify (10%)', 'Pipeline', '792'],
 ['30% - Appointment Scheduled', 'Solution Validation (30%)', 'Pipeline', '127'],
 ['50% - Proposal Sent', 'Proposal / Bid Submitted (70%)', 'Best Case', '208'],
 ['80% - Waiting on Order', 'Negotiation / Commercial Agreement (90%)', 'Commit', '12'],
 ['Closed won', 'Closed Won', 'Closed', '2,109'],
 ['Closed lost', 'Closed Lost', 'Omitted', '1,557'],
])

LEADMAP = table(['HubSpot lead status', 'Salesforce Lead Status'], [
 ['New &middot; Open &middot; In progress &middot; Attempted to contact', 'Working'],
 ['Connected &middot; Open deal', 'Engaged'],
 ['Bad timing', 'Nurturing'],
 ['Unqualified', 'Disqualified (needs a Disqualify Reason)'],
])

ERRS = ''.join(f'<div class="err"><div class="msg">{m}</div><p>{w}</p></div>'
               for m,w in build_cc_data.ERRORS)
PICK = ''.join(f'<button data-stage="{s["id"]}" aria-pressed="false">{s["pos"]}. {s["name"]}</button>' for s in S)

EXTRA_CSS = '''
.tblwrap{overflow-x:auto;margin:14px 0 6px;border:1px solid var(--line);border-radius:12px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:.93rem}
th{font-family:var(--f-disp);font-size:.74rem;letter-spacing:.06em;text-transform:uppercase;text-align:left;
   color:var(--ink-soft);background:var(--tint);padding:10px 14px}
td{padding:10px 14px;border-top:1px solid var(--line);vertical-align:top;color:var(--ink)}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin:16px 0}
.stat{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.stat b{display:block;font-family:var(--f-disp);font-size:1.5rem;color:var(--accent-ink)}
.stat span{font-size:.85rem;color:var(--muted)}
.brand{display:flex;align-items:center;gap:10px;margin-bottom:14px}
.brand img{height:34px;width:auto}
'''

LOGO = ''
lp = os.path.expanduser('~/Work/SaaScend/Xypher/enablement-slides/assets/logo_white.png')
if os.path.exists(lp):
    import base64
    LOGO = 'data:image/png;base64,' + base64.b64encode(open(lp,'rb').read()).decode()

HTML = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<!-- Internal enablement for the CyberCrowd sales team (Xypher group). Every field name, dropdown
     option and pass/fail mark was read from the Xypher production org on 30 Sep 2026. -->
<meta name="robots" content="noindex, nofollow, noarchive">
<title>CyberCrowd Salesforce Guide</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Open+Sans:ital,wght@0,400;0,600;0,700;1,400&display=swap">
<style>{build_cc_css.CSS}{EXTRA_CSS}</style>
</head>
<body>

<header class="hero">
  <div class="wrap">
    {'<div class="brand"><img alt="SaaScend" src="'+LOGO+'"></div>' if LOGO else ''}
    <p class="eyebrow">SaaScend &times; Xypher &middot; CyberCrowd sales team</p>
    <h1>Your HubSpot pipeline is now in Salesforce</h1>
    <p class="stand">Your companies, contacts, deals and history came across from HubSpot. This guide gets you logged in, shows you where everything went, and walks you
      through tidying your deals so they move.</p>
    <div class="prog">
      <div class="top">
        <span class="lbl">Deals tidied</span>
        <span class="count" id="count">0</span>
      </div>
      <div class="bar"><i id="bar"></i></div>
      <p class="row" id="progsub">List the deals you want to tidy below and tick them off as you go.</p>
      <div class="row">
        <span>How many open deals are you tidying?</span>
        <input type="number" id="target" min="0" max="999" placeholder="—" aria-label="Number of deals to tidy">
        <button class="ghost" id="resetall" type="button">Start over</button>
      </div>
    </div>
  </div>
</header>

<nav class="jump">
  <div class="wrap">
    <a href="#login">Logging in</a>
    <a href="#orderform">Order forms</a>
    <a href="#closing">Closing a deal</a>
    <a href="#moved">What came across</a>
    <a href="#basics">Finding your way</a>
    <a href="#tidy">Tidy your deals</a>
    <a href="#stages">What each stage needs</a>
    <a href="#tracker">Your list</a>
    <a href="#errors">When it will not save</a>
    <a href="#help">Help</a>
  </div>
</nav>

<div class="wrap">
<main>

<section id="login">
  <h2>Logging in</h2>
  <p class="dek">You sign in with your DXR Cyber Microsoft account &mdash; no Salesforce password.</p>
  <ul class="steps">{''.join(LOGIN)}</ul>
</section>

<section id="moved">
  <h2>What came across from HubSpot</h2>
  <p class="dek">Everything you were working is here, under the same owner. Counts are from the
    Xypher production org on 30 September.</p>
  <div class="stats">
    <div class="stat"><b>9,013</b><span>companies &rarr; Accounts</span></div>
    <div class="stat"><b>1,386</b><span>Contacts</span></div>
    <div class="stat"><b>9,855</b><span>Leads</span></div>
    <div class="stat"><b>4,805</b><span>deals &rarr; Opportunities</span></div>
    <div class="stat"><b>1,139</b><span>of them still open</span></div>
  </div>
  <h3>Where each thing went</h3>
  {DICT}
  <h3>Your deal stages</h3>
  <p>Stages map one-to-one. The percentage is what the forecast assumes, and it follows the stage
    automatically &mdash; note Proposal moves from 50% to 70% and Waiting on Order from 80% to 90%.</p>
  {STAGEMAP}
  <h3>Your lead statuses</h3>
  {LEADMAP}
  <div class="note"><span class="tag">What did not come across, on purpose</span>
    <p><strong>Call recordings</strong> stayed in HubSpot. <strong>A 2021 import of Cyber Essentials
    register prospects</strong> with no contact details was left out &mdash; there was no one to
    email. A few hundred <strong>contacts that matched existing Xypher records</strong> are being
    checked and enriched after go-live, so you may see them appear in the first weeks.</p></div>
</section>

<section id="basics">
  <h2>Finding your way around</h2>
  <p class="dek">Four things to recognise. Once these make sense the rest is just typing.</p>
  <ul class="steps">
    <li data-step="b1"><div class="head"><span class="num"><span>A</span></span>
      <span class="ttl"><b>Tabs across the top</b><em>Home, Leads, Accounts, Contacts, Opportunities&hellip;</em></span>
      <span class="tick">Mark done</span><span class="chev" aria-hidden="true">&rsaquo;</span></div>
      <div class="body"><p>Each tab is a type of record: <strong>Accounts</strong> are companies,
      <strong>Contacts</strong> are people, <strong>Opportunities</strong> are deals,
      <strong>Leads</strong> are people you have not qualified yet. Click a tab for a list; click a row
      to open the record.</p></div></li>
    <li data-step="b2"><div class="head"><span class="num"><span>B</span></span>
      <span class="ttl"><b>List views</b><em>Your filtered tables</em></span>
      <span class="tick">Mark done</span><span class="chev" aria-hidden="true">&rsaquo;</span></div>
      <div class="body"><p>The dropdown next to a list&rsquo;s name switches between saved filters
      &mdash; <strong>My Opportunities</strong>, <strong>Closing This Month</strong>,
      <strong>Recently Viewed</strong>. Changing the view never changes data.</p></div></li>
    <li data-step="b3"><div class="head"><span class="num"><span>C</span></span>
      <span class="ttl"><b>Shared accounts</b><em>Some of your customers are also DXR customers</em></span>
      <span class="tick">Mark done</span><span class="chev" aria-hidden="true">&rsaquo;</span></div>
      <div class="body"><p>Where a company already existed in Salesforce, your record was joined to it.
      The account owner may be a DXR colleague; you are on the <strong>Account Team</strong> panel and
      your deals, contacts and history are all there. This is the group seeing one customer once.</p></div></li>
    <li data-step="b4"><div class="head"><span class="num"><span>D</span></span>
      <span class="ttl"><b>Saving is not the same as advancing</b><em>The single most useful thing to know</em></span>
      <span class="tick">Mark done</span><span class="chev" aria-hidden="true">&rsaquo;</span></div>
      <div class="body"><p>Editing a field and saving is always fine. <strong>Changing the Stage</strong>
      is what triggers the checks. Your migrated deals sit at the stage they had in HubSpot; the checks
      only apply the first time you move one forward.</p></div></li>
  </ul>
</section>

<section id="orderform">
  <h2>Creating an order form</h2>
  <p class="dek">For customers on a PO process. A temporary tool until the group-wide Pricing Desk arrives.</p>
  <ul class="steps">{''.join(ORDER)}</ul>
</section>

<section id="closing">
  <h2>Closing a deal as won</h2>
  <p class="dek">The same hand-over DXR uses: one form, and Salesforce tells Projects and Finance.</p>
  <ul class="steps">{''.join(CLOSE)}</ul>
</section>

<section id="tidy">
  <h2>Tidy your deals</h2>
  <p class="dek">Your first week. Six steps, per deal; ticks are remembered on this browser.</p>
  <ul class="steps">{''.join(TIDY)}</ul>
</section>

<section id="stages">
  <h2>What each stage actually needs</h2>
  <p class="dek">Pick a stage for the fields it demands and, for every dropdown, which options let you
    move on. Read straight from the production rules, so it matches what Salesforce will tell you.</p>
  <div class="stagepick" id="stagepick">{PICK}</div>
  <div class="stagebox" id="stagebox"></div>
  <div class="note" style="margin-top:16px"><span class="tag">The light path</span>
    <p>Cyber Essentials and Pen Testing deals under &pound;5k, and renewals, skip the MEDDPICC grades.
    They still need Service Line, Funding Route, a Next Step and the closing fields.</p></div>
</section>

<section id="tracker">
  <h2>Your list</h2>
  <p class="dek">Jot the deals you are tidying and tick each off. Kept on this browser only &mdash;
    nobody else sees it.</p>
  <div class="deals" id="deals"></div>
  <div class="addrow">
    <input type="text" id="dealname" placeholder="Deal name, as you would recognise it" aria-label="Deal name to add">
    <button type="button" id="dealadd">Add</button>
  </div>
</section>

<section id="errors">
  <h2>When it will not save</h2>
  <p class="dek">The messages you are most likely to hit, and what each means.</p>
  <div class="errs">{ERRS}</div>
  <div class="note"><span class="tag">A general rule</span>
    <p>The message appears in a red box at the <em>top</em> of the form, often scrolled out of
    sight. If a save seems to do nothing, scroll up. It is a checklist, not a telling-off.</p></div>
</section>

<section id="help">
  <h2>Help</h2>
  <p>Ask <strong>Kristian</strong> first &mdash; if one person is stuck, usually several are.</p>
  <p>If something looks wrong rather than confusing &mdash; a deal under the wrong owner, a company
    that looks duplicated, history that is missing &mdash; screenshot it and send it to SaaScend.
    Migration fixes are quickest in the first two weeks.</p>
</section>

</main>
</div>

<footer>
  <div class="wrap">
    Prepared by SaaScend for the CyberCrowd sales team, updated 2 October 2026. Every field name, dropdown
    option and pass/fail mark is read from the Salesforce production org; if the guide and the system
    disagree, the guide is wrong &mdash; tell us. Your ticks and list are stored in this browser only.
  </div>
</footer>

<script>window.__CC_STAGES__ = {json.dumps(S, separators=(",",":"))};</script>
<script>{build_cc_js.JS}</script>
</body>
</html>
'''
out = os.path.join(HERE, 'index.html')
open(out,'w',encoding='utf-8').write(HTML)
print(f"  index.html written: {len(HTML)/1024:.0f} KB · stages {len(S)} · errors {len(build_cc_data.ERRORS)}")
