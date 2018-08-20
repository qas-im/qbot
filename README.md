# qbot

Remember back in the day when you could go online and buy things without any concerns? Well those times are long over and we now live in the era of bots. These bots are terrible and horrible creations that prevent everyday people like myself from buying things online. So if you can't beat 'em, join 'em. That's why I've made my own bot here for me and everyone to use. This bot has been generally structured using thechinatownmarket.com and will be optimized for supremenewyork.com once their website is available to use again on August 20th 2018.


### Setup

Sorry to non-OSX users but I built this program exclusively on my macbook so you might have to go a little bit further out of your way to get this set up properly. If you have a mac pretty much all you have to do is copy and paste the following commands, I added descriptions if you want an in depth.

```
pip install selenium
```

This command will install selenium, a tool used for web automation. This tool is what lets us control the web browser; e.g. going to web pages, clicking links, waiting for things to load on the page, etc.

Next you're going to want to [click this](https://chromedriver.storage.googleapis.com/index.html?path=2.41/) and choose your operating system to install ChromeDriver, a web driver for Google Chrome. A web driver essentially allows us to carry out automated actions in a browser. Selenium needs a web driver in order to work; you could also use Firefox, Safari, or whatever browser but I like Chrome. 


Lastly you'll want to unzip the file we just downloaded and run the following commands in the terminal. If you don't know how to open the terminal just press COMMAND + SPACE and search for the word "terminal". Once you're there copy and paste these commands in and press enter.

```
cd Downloads
mv chromedriver /usr/local/bin
```

The "cd Downloads" command is going to the directory on your computer that contains all of your downloads. The command after that is just moving chromedriver to a different directory on your computer called "user/local/bin". This a space in your computer commonly and optimally used for putting these types of resources. 

And that's it, you're now fully set up and ready to use my bot! (sorry for non osx people who couldn't get things set up yet. you were smart enough not to get a mac so i'm sure you're smart enough to figure it out, i believe in you)


### Usage

CURRENTLY STILL IN DEVELOPMENT SO DESCRIPTION WILL BE HERE ONCE COMPLETED


### Authors

* **Qasim Shareh** - pretty much all development


### Aknowledgements

* Shoutout to GE Digital for introducing me to the wonders of Selenium
* Shoutout to Supreme for making me victim to hypebeast culture
* Should out to my cat Petra, my sister J'smol, my mom the mayor, and my dad the doc
