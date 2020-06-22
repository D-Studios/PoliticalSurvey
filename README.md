# PoliticalSurvey

<b>This web app for this Epsilon Hacks Hackathon project by Groupuwu is hosted on:</b> <br>
http://35.247.48.245 <br>
http://35.247.48.245/results

<b>The landing page can be found on:</b><br>
https://political-survey-landing-page--harshitgupta2.repl.co/ <br>
<b>Source for the landing page:</b><br>
https://repl.it/@HarshitGupta2/Political-Survey-Landing-Page#index.html or<br>
https://github.com/KinoZampie/Political-Survey-Landing-Page

This project was inspired due to the fact that our group wanted to create a product that would store values using databases. Our group went through several ideas of which social good were focused on. After some time, we decided that having a political representation poll could be a realistic yet challenging project. Originally, the project was meant to be a political compass with only two axes (left vs. right on the x-axis and authority vs liberty on the vertical axis). However, it was decided to use 8values ( where this assesses economic, diplomatic, civil, and societal ideologies) in order to better assess what the people want.

The user first opens the project by going to the landing page. In the landing page, the user can visit other pages to understand the usage of each variable (economic, diplomatic, civil and societal) and what their values mean. From the landing page, the user can click on a link to participate in a survey. In the survey, the user answers 31 questions that ask the user political ideological questions. At the end of the survey, the user's ideology on economics, diplomacy, civil issues, and society is determined based on their answers and is sent to be stored on databases, where data is visualized on histograms to draw a picture on the ideologies of the people.

This prototype of this project was built with simple Python. Overtime, the product was improved with Flask and HTML/CSS. JSON files were used to store key value pairs and JavaScript was used to display histograms. HTML/CSS was not only used in the survey, but especially on the web pages that are viewed before visiting the survey. Google Cloud Computing Virtual Machine was used to store data on the cloud, and txt files were used to store data.

One challenge that we ran into was trying to find an efficient method to store data on the cloud. First, MongoDB was looked at to store the data. Then, MySQL was looked as another suitable method to store data. After some time, it was decided to use a Google Cloud Computing Virtual Machine. Another challenge for the project was trying to find a way to make sure a single user did not submit two answers, which was later on resolved by seeing if an entered Social Security Number on the Personal Information page was previously registered on a completion of the survey.

Our group is proud to work together efficiently without much conflict. Issues were worked on as a team and technological issues and platforms were discussed. Furthermore, we are proud to learn that it is not only important to know how to code, but how to solve technological problems by understanding what technologies should be used and what strategies should be used. We are satisfied to avoid excessive feature creep in the favor of a realistic project that can be accomplished in a realistic time-schedule. Finally, we are happy that we managed to create a working product that looks good and improves our computer science skills in general.

We learned how to effectively use GitHub to multi-task. We furthermore learned how to use local and global hosts. We acquired knowledge about how to use productivity tools like Discord and Google Docs to work together as a group. We learned how to utilize our individual strengths with each other (people with various technological backgrounds were able to work effectively together without disrupting one another). Furthermore, we learned how to debug and fix glitches together as a group.

If this product was to scale, there will probably be more features including more data analysis. So far, only histograms are shown but it would be nice to use the data for the computer to draw sensible conclusions. For example, a 95% confidence interval could be constructed on each of the variables (economic, diplomatic, civil, and societal) in order to find the range of values where most values fall into for each of the variables. In addition, there can be more specific questions regarding current issues (e.g. corporate welfare, minimum wage, immigration policies, citizenship, police funding, legalization of certain drugs, global warming, and religious freedoms). Furthermore, this application could be used by the US Census Bureau near every presidential election so presidential candidates can comprehend what the voters want in order to adjust their policies accordingly and get more votes.
