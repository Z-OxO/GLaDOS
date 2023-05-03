<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
</head>
<body>
	<h1>GLaDOS Chatbot</h1>
	This is a chatbot based on the OpenAI GPT. The chatbot simulates a conversation with the character GLaDOS from the video game Portal.
	<br></br>
	<img src="https://cdn-uploads.gameblog.fr/images/actu/full/72447_gb_news.jpg">
	<h2>How to Use</h2>
	<ol>
		<li>Install the required libraries using the command: <pre><code>pip install -r requirements.txt</code></pre></li>
		<li>Create an OpenAI API key and set it in config.ini. See <a href="https://beta.openai.com/docs/authentication/api-keys">OpenAI documentation</a> for more information on how to create an API key.</li>
		<li>Run the <code>main.py</code> file using Python 3.9 or later: <pre><code>python main.py</code></pre></li>
		<li>Follow the instructions in the console to interact with the chatbot.</li>
    <li>You can change the language in config.ini.</li>
	</ol>
	<h2>Project Structure</h2>
	<p>The project has the following files:</p>
	<ul>
		<li><code>main.py</code>: The main Python file to run the chatbot.</li>
		<li><code>audio.py</code>: Contains functions to record and recognize audio input.</li>
		<li><code>text_to_speech.py</code>: Contains a function to convert text to speech using the Google Text-to-Speech API.</li>
		<li><code>README.md</code>: A markdown file with project information.</li>
		<li><code>requirements.txt</code>: A text file with the required libraries to install.</li>
	</ul>
	<h2>Credits</h2>
	<p>The GLaDOS character and Portal game are the property of Valve Corporation. This project is for educational purposes only and not affiliated with or endorsed by Valve Corporation or OpenAI.</p>
</body>
</html>

