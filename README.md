

### Story  
It is time to put your newly acquired Flask skills to use. Your next big task is to implement a crowdsourced Q&A site, similar to Stack Overflow.

The initial version of the site must be able to handle questions and answers. There is no need for additional functionality, such as user management or comments for questions and answers.

The management is very interested in the agile development methodologies that they recently heard about, so they are handing out a prioritized list of user stories, called a product backlog. Try to estimate how many of these stories your team can finish until the demo. As the order is important, choose from the beginning of the list as much as you can. The first four stories are the most important.  
  
<img src="https://i.ibb.co/dbwjRGk/Screenshot-21.png" alt="Screenshot-21" border="0" />


### What are you going to learn?  
Create a Flask project.

Use routes with Flask.

Use HTML and the Jinja templating engine.

CSV handling.  
  



### Tasks  
Implement the /list page that displays all questions.

<img src="https://i.ibb.co/jHcTNMH/Screenshot-22.png" alt="Screenshot-22" border="0" />

The page is available under /list.
The data is loaded and displayed from question.csv.
The questions are sorted by most recent.
Create the /question/<question_id> page that displays a question and the answers for it.

The page is available under /question/<question_id>.
There are links to the question pages from the list page.
The page displays the question title and message.
The page displays all answers to a question.
Implement a form that allows the user to add a question.

<img src="https://i.ibb.co/PjQ3VH7/Screenshot-24.png" alt="Screenshot-24" border="0" />

There is an /add-question page with a form.
The page is linked from the list page.
There is a POST form with at least title and message fields.
After submitting, the page redirects to "Display a question" page of this new question.
Implement posting a new answer.

The page URL is /question/<question_id>/new-answer.
The question detail page links to the page.
The page has a POST form with a form field called message.
Posting an answer redirects to the question detail page. The new answer is displayed on the question detail page.
Implement sorting for the question list.

The question list can be sorted by title, submission time, message, number of views, and number of votes.
The question list can be put in ascending and descending order.
The order is passed as query string parameters, such as /list?order_by=title&order_direction=desc.
Implement deleting a question.

Deleting is implemented by the /question/<question_id>/delete endpoint.
There is a deletion link on the question page.
Deleting redirects to the list of questions.
Allow the user to upload an image for a question or answer.

The forms for adding question and answer contain an "image" file field.
The user can attach an image (.jpg, .png).
The image is saved on server and displayed next to the question or the answer.
When deleting the question or answer, the image file is also deleted.
Implement editing an existing question.

There is a /question/<question_id>/edit page.
The page is linked from the question page.
There is a POST form with at least title and message fields.
The fields are pre-filled with existing question data.
After submitting, the page redirects to the "Display a question" page. The changed data is visible on the "Display a question" page.
Implement deleting an answer.

Deleting is implemented by /answer/<answer_id>/delete endpoint.
There is a deletion link on the question page, next to an answer.
Deleting redirects to the question detail page.
Implement voting on questions.

Vote numbers are displayed next to questions on the question list page.
There are "vote up/down" links next to questions on the question list page.
Voting uses /question/<question_id>/vote_up and /question/<question_id>/vote_down endpoints.
Voting up increases, voting down decreases the vote_number of the question by one.
Voting redirects to the question list.
Implement voting on answers.

Vote numbers are displayed next to answers on the question detail page.
There are "vote up/down" links next to answers.
Voting uses /answer/<answer_id>/vote_up and /answer/<answer_id>/vote_down endpoints.
Voting up increases, voting down decreases the vote_number of the answer by one.
Voting redirects to the question detail page.  
  

<br/>  

 


## Languages and Tools  
<div align="center">  
<a href="https://getbootstrap.com/docs/3.4/javascript/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/bootstrap-plain.svg" alt="Bootstrap" height="25" /></a>  
<a href="https://flask.palletsprojects.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/flask.png" alt="Flask" height="25" /></a>  
<a href="https://github.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/git-scm-icon.svg" alt="Git" height="25" /></a>  
<a href="https://en.wikipedia.org/wiki/HTML5" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/html5-original-wordmark.svg" alt="HTML5" height="25" /></a>  
<a href="https://www.python.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="Python" height="25" /></a>  
</div>  

<br/>  


## Github Stats  
<table><tr><td valign="top" width="50%">

<img src="https://github-readme-stats.vercel.app/api?username=MadalinaDumitrascu&show_icons=true&count_private=true&hide_border=true" align="left" style="width: 100%" />

</td><td valign="top" width="50%">

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=MadalinaDumitrascu&hide_border=true&layout=compact" align="left" style="width: 100%" />

</td></tr></table>  

<br/>  

  

<br/>  

![Profile views counter](https://komarev.com/ghpvc/?username=rishavanand&&style=flat-square)  
  

<br/>  


<br />

----
<div align="center">Generated using <a href="https://profilinator.rishav.dev/" target="_blank">Github Profilinator</a></div>
