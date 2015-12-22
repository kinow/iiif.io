
from github import Github
import re

downre = re.compile("(^| |:)-1($| |:)")
upre = re.compile("(^| |:)\\+1($| |:)")
okre = re.compile("(^| )(:ok:|:ok_hand:|\\+0|-0|:\\+0:)($| )")

g = Github("azaroth42", "")
repo = g.get_repo('IIIF/iiif.io')

eds = ['azaroth42', 'jpstroop', 'zimeon', 'mikeapp', 'tomcrane']
edtd = ''.join(["<th>{0}</th>".format(x) for x in eds])

style="""
<style>
 .issuetable { cellspacing: 0; font-family: sans-serif }
 .issuetable tr td { padding: 3; border-bottom: 1px solid black; text-align: center }
 .issuetable tr	{ border-bottom: 1px solid black  }
 .issuetable tr	:first-child { text-align: left }
 .issuetable tr th { font-weight: bold; border-bottom: 2px solid black }
 .tag { font-weight: bold ; color: white; padding: 3px; border-radius: 2px; font-size: 70% }
 a { text-decoration: none; color: #5050F0; }
</style>
"""

print style
print '<table class="issuetable">'
print "<tr><th>Issue</th>{0}<th>Others</th></tr>".format(edtd)

issues = repo.get_issues(state="open")
for issue in issues:
	n = issue.number #674 or similar
	name = issue.title
	url = issue.html_url
	pr = issue.pull_request
	ispr = " <b>PR</b>" if pr else ""
	labelobs = issue.get_labels()
	lhtml = []
	labels = []
	for l in labelobs:
		col = l.color
		if int(col[0], 16) > 8 and int(col[2], 16) > 8 and int(col[4], 16) > 8:
			fcol = "black"
		else:
			fcol = "white"
		lhtml.append('<span class="tag" style="background:#{0}; color: {2}">{1}</span>'.format(col, l.name, fcol))
		labels.append(l.name)

	if 'defer' in labels:
		continue

	comments = issue.get_comments()
	response = dict(zip(eds, [None] * len(eds)))
	others = {}

	if ispr:
		# If you did the PR, you're implicitly +1
		response[issue.user.login] = {'vote': "+1", 'text': issue.body, 'url': issue.html_url}

	for comment in comments:
		who = comment.user
		login = who.login
		text = comment.body
		which = response if login in eds else others

		if upre.search(text):
			which[login] = {'vote': "+1", 'text': comment.body, 'url': comment.html_url}
		elif downre.search(text):
			which[login] = {'vote': "-1", 'text': comment.body, 'url': comment.html_url}
		elif okre.search(text):
			which[login] = {'vote': "0", 'text': comment.body, 'url': comment.html_url}
		else:
			# just text?
			continue			

	ed = []
	for login in eds:
		if response[login] != None:
			ed.append('<td><a href="{0}">{1}</a></td>'.format(response[login]['url'], response[login]['vote']))
		else:
			ed.append('<td>-</td>')		
	ed = ''.join(ed)
	other = []
	for (k, v) in others.items():
		other.append('{0}: <a href="{1}">{2}</a><br/>'.format(k, v['url'], v['vote']))
	other = ''.join(other)
	if len(name) > 50:
		name = name[:50] + "..."
	lhtml = ' '.join(lhtml)
	print '<tr><td>{3}<br/><a href="{0}">{1}</a> {2} {6}</td>{4}<td>{5}</td></tr>'.format(url, n, ispr, name, ed, other, lhtml)

print "</table>"
