# discord-bot-python

### Simple discord bot that can play music and display jokes.

Uses:
* [Discord API](https://pypi.org/project/discord.py/)
* [Jokes API](https://official-joke-api.appspot.com/random_joke)
* [youtube_dl](https://github.com/ytdl-org/youtube-dl)


### Usage
 The first step is generating the <b>token</b> and pasting it in the script.
 ``` python
 client.run('YOUR TOKEN HERE')
 ```
 
 After this step, it is ready for deployment in any server.
 
 ### Commands
 #### The prefix is '&'
 Example: &play http://url, &joke, &stop ..
 
 ``` 
 play http://any.YoutubeURL
 ```
 * Loads the url and plays the content in the General voice channel

<br>
 
``` 
pause
```
* Pauses the audio

<br>

``` 
resume
```
* Resume playback

<br>

``` 
leave
```
* Disconnect from the voice channel

<br>


``` 
 stop 
```
* Ends the current track

<br>


``` 
joke
```
* Display a random joke

<br>
